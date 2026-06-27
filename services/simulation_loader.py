from database.db import SessionLocal
from database.models import Village, Khewat, Khasra


class SimulationLoader:

    @staticmethod
    def get_villages():

        session = SessionLocal()

        try:

            villages = (
                session.query(Village)
                .order_by(Village.village_name)
                .all()
            )

            return villages

        finally:

            session.close()
  
    @staticmethod
    def get_khewats(village_id):

        session = SessionLocal()

        try:
            

            khewats = (
                session.query(Khewat)
                .filter(Khewat.village_id == village_id)
                .order_by(Khewat.khewat_no)
                .all()
            )

            

            for k in khewats:
                print(
                    f"ID={k.id}, "
                    f"Khewat={k.khewat_no}, "
                    f"Village ID={k.village_id}"
                )

            return khewats

        finally:
            session.close()

    @staticmethod
    def get_khasras(khewat_id):

        session = SessionLocal()

        try:

            return (
                session.query(Khasra)
                .filter(Khasra.khewat_id == khewat_id)
                .order_by(Khasra.khasra_no)
                .all()
            )

        finally:

            session.close() 