from database.db import SessionLocal
from database.models import Ownership, Khasra


class ValidationEngine:

    @staticmethod
    def calculate_required_areas(khewat_id):

        session = SessionLocal()

        try:

            owners = (
                session.query(Ownership)
                .filter(Ownership.khewat_id == khewat_id)
                .all()
            )

            khasras = (
                session.query(Khasra)
                .filter(Khasra.khewat_id == khewat_id)
                .all()
            )

            total_area = sum(k.area for k in khasras)

            results = []

            for ownership in owners:

                # share_text example: "1551/26728"
                numerator, denominator = map(
                    int,
                    ownership.share_text.split("/")
                )

                required_area = (
                    total_area * numerator / denominator
                )

                results.append({

                    "owner_id": ownership.owner.id,
                    "owner_name": ownership.owner.owner_name,
                    "share": ownership.share_text,
                    "required_area": round(required_area, 2)

                })

            return results

        finally:

            session.close()

    @staticmethod
    def validate_allocations(khewat_id, allocations):

        session = SessionLocal()

        try:

            owners = ValidationEngine.calculate_required_areas(khewat_id)

            results = []

            for owner in owners:

                allocated_area = 0.0

                for parcel_id, owner_id in allocations.items():

                    if owner_id != owner["owner_id"]:
                        continue

                    khasra = session.query(Khasra).filter(
                        Khasra.id == parcel_id
                    ).first()

                    if khasra:
                        allocated_area += khasra.area

                difference = round(
                    allocated_area - owner["required_area"],
                    2
                )

                if abs(difference) <= 1:
                    status = "OK"

                elif difference > 0:
                    status = "EXCESS"

                else:
                        status = "SHORT"

                results.append({

                    "owner_name": owner["owner_name"],
                    "share": owner["share"],
                    "required_area": owner["required_area"],
                    "allocated_area": round(allocated_area, 2),
                    "difference": difference,
                    "status": status

                })

            return results

        finally:

            session.close()