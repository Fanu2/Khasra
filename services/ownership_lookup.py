from database.db import SessionLocal
from database.models import Ownership


class OwnershipLookup:

    @staticmethod
    def get_joint_owners(khewat_id):

        session = SessionLocal()

        try:

            print(f"Looking up owners for Khewat ID: {khewat_id}")

            owners = (
                session.query(Ownership)
                .filter(Ownership.khewat_id == khewat_id)
                .all()
            )

            print(f"Ownership records found: {len(owners)}")

            for ownership in owners:
                print(
                    f"Owner: {ownership.owner.owner_name} | "
                    f"Share: {ownership.share_text}"
                )

            return owners

        except Exception as e:

            print(f"OwnershipLookup Error: {e}")
            return []

        finally:

            session.close()