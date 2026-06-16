
from database.db import SessionLocal
from database.models import Khewat, Ownership
from services.khewat_service import KhewatService

class PartialPartitionEngine:
    @staticmethod
    def preview(source_khewat_id, owner_id, num, den):
        session=SessionLocal()
        try:
            khewat=session.get(Khewat, source_khewat_id)
            o=session.query(Ownership).filter(Ownership.khewat_id==source_khewat_id, Ownership.owner_id==owner_id).first()
            num=int(num); den=int(den)
            if den!=o.denominator: raise ValueError("Transfer denominator must match ownership denominator")
            if num<=0 or num>o.numerator: raise ValueError("Invalid transfer share")
            rem=o.numerator-num
            area=(num/den)*float(khewat.total_area)
            return {"current":f"{o.numerator}/{o.denominator}","transfer":f"{num}/{den}","remaining":f"{rem}/{den}","area":round(area,4)}
        finally: session.close()

    @staticmethod
    def execute(source_khewat_id, owner_id, num, den, new_khewat_no):
        session=SessionLocal()
        try:
            source=session.get(Khewat, source_khewat_id)
            o=session.query(Ownership).filter(Ownership.khewat_id==source_khewat_id, Ownership.owner_id==owner_id).first()
            num=int(num); den=int(den)
            if den!=o.denominator or num<=0 or num>o.numerator:
                raise ValueError("Invalid transfer share")
            area=(num/den)*float(source.total_area)
            rem=o.numerator-num
            if rem==0:
                session.delete(o)
            else:
                o.numerator=rem
                o.denominator=den
            source.total_area=max(0,float(source.total_area)-area)
            existing=session.query(Khewat).filter(Khewat.khewat_no==new_khewat_no).first()
            if existing: raise ValueError("Khewat number already exists")
            nk=KhewatService.create_khewat_in_session(session, source.village_id,new_khewat_no,"",area,
                [{"owner_id":owner_id,"numerator":num,"denominator":den}],[],
                status="PARTIAL_PARTITION",remarks="Partial Partition",allow_partial_share=True)
            
            try:
                from database.models import PartitionEvent
                ev=PartitionEvent(source_khewat_id=source.id,new_khewat_id=nk["id"],removed_area=area,remarks=f"Partial Partition {num}/{den}")
                session.add(ev)
            except Exception:
                pass
            session.commit()
            return nk
        except:
            session.rollback(); raise
        finally: session.close()
