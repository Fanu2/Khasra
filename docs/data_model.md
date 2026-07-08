\# Haryana Partition Manager (HPM)



\# Domain Model Specification



Version 1.0



\---



\# Philosophy



HPM is not database-driven.



HPM is domain-driven.



The domain model represents the legal partition process.



The database is merely a persistence mechanism.



\---



\# Aggregate Root



PartitionCase



A Partition Case owns every object created during partition proceedings.



Everything belongs to one Partition Case.



\---



\# Entity



\## PartitionCase



Purpose



Represents one legal partition proceeding.



Attributes



• UUID

• Case Number

• Case Type

• Order Number

• Order Date

• Revenue Officer

• Village

• Jamabandi

• Status

• Created Date

• Modified Date



Owns



Existing Revenue Records



Allocations



Generated Records



Reports



Audit Log



\---



\# Entity



\## Village



Purpose



Reference village.



Immutable after case creation.



\---



\# Entity



\## Jamabandi



Purpose



Source Jamabandi used for partition.



Immutable.



\---



\# Entity



\## Existing Khewat



Purpose



Represents an existing khewat.



Contains



Owners



Parcels



Shares



\---



\# Entity



\## Existing Owner



Purpose



Owner from source Jamabandi.



Contains



Share



Possession



\---



\# Entity



\## Existing Parcel



Purpose



Existing khasra.



Contains



Area



Land Use



Possession



\---



\# Entity



\## Allocation



Purpose



Represents proposed allocation.



Links



Existing Parcel



↓



Generated Khewat



↓



Generated Owner



\---



\# Entity



\## Generated Khewat



Purpose



Represents a newly generated khewat.



Contains



Owners



Generated Parcels



Area



\---



\# Entity



\## Generated Ownership



Purpose



Ownership after partition.



Contains



Owner



Share



Generated Khewat



\---



\# Entity



\## Validation Result



Purpose



Stores validation outcome.



Contains



Errors



Warnings



Information



\---



\# Entity



\## Report



Purpose



Generated output.



Types



Draft Order



Owner Register



Khewat Register



Parcel Register



Allocation Register



Summary Report



\---



\# Relationships



PartitionCase



↓



Village



↓



Jamabandi



↓



Existing Khewats



↓



Existing Owners



↓



Existing Parcels



↓



Allocations



↓



Generated Khewats



↓



Generated Ownership



↓



Reports



\---



\# Guiding Principle



Nothing exists outside a Partition Case.



Every operation belongs to exactly one case.



