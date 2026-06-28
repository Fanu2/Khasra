from datetime import datetime

from database.db import SessionLocal
from database.models import SimulationAllocation


class SimulationStorage:

    @staticmethod
    def save_simulation(
        simulation_name,
        khewat_id,
        allocations
    ):

        session = SessionLocal()

        try:

            # Remove any previous copy of this simulation
            session.query(
                SimulationAllocation
            ).filter(
                SimulationAllocation.simulation_name == simulation_name
            ).delete()

            # Save every allocation
            for parcel_id, owner_id in allocations.items():

                row = SimulationAllocation(

                    simulation_name=simulation_name,

                    khewat_id=khewat_id,

                    parcel_id=parcel_id,

                    owner_id=owner_id

                )

                session.add(row)

            session.commit()

        finally:

            session.close()

    @staticmethod
    def load_simulation(
        simulation_name
    ):

        session = SessionLocal()

        try:

            rows = (
                session.query(
                    SimulationAllocation
                )
                .filter(
                    SimulationAllocation.simulation_name == simulation_name
                )
                .all()
            )

            allocations = {}

            for row in rows:

                allocations[row.parcel_id] = row.owner_id

            return allocations

        finally:

            session.close()

    @staticmethod
    def list_simulations():
        pass

    @staticmethod
    def delete_simulation(simulation_name):
        pass