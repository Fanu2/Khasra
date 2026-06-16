from fractions import Fraction

from database.db import SessionLocal
from database.models import Khewat, Ownership, Khasra
from services.khewat_service import KhewatService
from services.ownership_engine import OwnershipEngine


class PartitionEngine:

    @staticmethod
    def partition(
        source_khewat_id,
        selected_owner_ids,
        selected_khasra_ids,
        new_khewat_no,
        new_khatauni_no="",
        remarks="",
        partition_share=None
    ):

        session = SessionLocal()

        try:

            source = session.get(Khewat, source_khewat_id)

            ownerships = session.query(Ownership).filter(
                Ownership.khewat_id == source_khewat_id
            ).all()

            selected_ownerships = [
                o for o in ownerships
                if o.owner_id in selected_owner_ids
            ]

            remaining_ownerships = [
                o for o in ownerships
                if o.owner_id not in selected_owner_ids
            ]

            khasras = session.query(Khasra).filter(
                Khasra.khewat_id == source_khewat_id
            ).all()

            selected_khasras = [
                k for k in khasras
                if k.id in selected_khasra_ids
            ]

            selected_area = sum(k.area for k in selected_khasras)
            remaining_area = source.total_area - selected_area

            ownership_data = []

            # Partial share mode
            if partition_share and len(selected_ownerships) == 1:

                ownership = selected_ownerships[0]

                transfer_share = Fraction(
                    partition_share[0],
                    partition_share[1]
                )

                old_share = Fraction(
                    ownership.numerator,
                    ownership.denominator
                )

                if transfer_share > old_share:
                    raise ValueError(
                        "Partition share exceeds owner's share."
                    )

                ownership_data.append({
                    "owner_id": ownership.owner_id,
                    "numerator": transfer_share.numerator,
                    "denominator": transfer_share.denominator
                })

                remaining_share = old_share - transfer_share

                if remaining_share == 0:
                    session.delete(ownership)
                else:
                    ownership.numerator = remaining_share.numerator
                    ownership.denominator = remaining_share.denominator

                    remaining_ownerships.append(ownership)

            else:

                selected_shares = {}

                for item in selected_ownerships:
                    selected_shares[item.owner_id] = Fraction(
                        item.numerator,
                        item.denominator
                    )

                selected_shares = OwnershipEngine.normalize_shares(
                    selected_shares
                )

                for owner_id, share in selected_shares.items():
                    ownership_data.append({
                        "owner_id": owner_id,
                        "numerator": share.numerator,
                        "denominator": share.denominator
                    })

                for ownership in selected_ownerships:
                    session.delete(ownership)

            khasra_data = [
                {
                    "khasra_no": k.khasra_no,
                    "area": k.area
                }
                for k in selected_khasras
            ]

            new_khewat = KhewatService.create_khewat_in_session(
                session=session,
                village_id=source.village_id,
                khewat_no=new_khewat_no,
                khatauni_no=new_khatauni_no,
                total_area=selected_area,
                ownerships=ownership_data,
                khasras=khasra_data,
                status="PARTITIONED",
                remarks=remarks
            )

            for k in selected_khasras:
                session.delete(k)

            if not partition_share:
                remaining_shares = {}

                for item in remaining_ownerships:
                    remaining_shares[item.owner_id] = Fraction(
                        item.numerator,
                        item.denominator
                    )

                if remaining_shares:
                    remaining_shares = OwnershipEngine.normalize_shares(
                        remaining_shares
                    )

                    for item in remaining_ownerships:
                        share = remaining_shares[item.owner_id]
                        item.numerator = share.numerator
                        item.denominator = share.denominator

            source.total_area = remaining_area

            session.commit()

            return {
                "id": new_khewat["id"],
                "khewat_no": new_khewat["khewat_no"]
            }

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
