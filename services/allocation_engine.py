class AllocationEngine:
    """
    Temporary in-memory partition simulation.

    No database updates are made until the user
    presses the Commit button.
    """

    def __init__(self):

        # parcel_id -> owner_id
        self.allocations = {}

    def allocate(self, parcel_id, owner_id):
        """Allocate a parcel to an owner."""
        self.allocations[parcel_id] = owner_id

    def unallocate(self, parcel_id):
        """Remove an allocation."""
        self.allocations.pop(parcel_id, None)

    def is_allocated(self, parcel_id):
        """Return True if parcel is already allocated."""
        return parcel_id in self.allocations

    def get_owner(self, parcel_id):
        """Return allocated owner id."""
        return self.allocations.get(parcel_id)

    def clear(self):
        """Clear the entire simulation."""
        self.allocations.clear()

    def get_all_allocations(self):
        """Return all allocations."""
        return self.allocations.copy()

    def allocation_count(self):
        """Return number of allocated parcels."""
        return len(self.allocations)
    
    def remove(self, parcel_id):

        """
        Remove an allocation for a parcel.
        """

        if parcel_id in self.allocations:
            del self.allocations[parcel_id]

    def set_allocations(self, allocations):

        self.allocations = allocations.copy()