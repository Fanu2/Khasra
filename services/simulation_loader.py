from database.db import SessionLocal
from database.models import Village


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