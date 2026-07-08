\# Haryana Partition Manager (HPM)



\# Functional Workflow Specification



Version: 1.0



\---



\# Purpose



The Haryana Partition Manager (HPM) is a workflow-driven desktop application for conducting partition proceedings based on the Haryana Land Revenue Act and the Punjab Land Revenue Act (as applicable in Haryana).



The objective of HPM is to assist revenue officials in preparing a legally valid partition proposal while preserving the integrity of Jamabandi records.



HPM is \*\*not\*\* merely a database application.



It is a digital implementation of the official partition procedure.



\---



\# Overall Workflow



Create Case

&#x20;       ↓

Select Village

&#x20;       ↓

Select Jamabandi

&#x20;       ↓

Load Existing Revenue Records

&#x20;       ↓

Review Existing Holdings

&#x20;       ↓

Prepare Allocation

&#x20;       ↓

Validate Allocation

&#x20;       ↓

Generate New Khewats

&#x20;       ↓

Generate New Ownership

&#x20;       ↓

Generate Reports

&#x20;       ↓

Close Case



\---



\# Stage 1 — Create Partition Case



Purpose



Create a new partition proceeding.



Input



• Case Number

• Case Type

• Order Date

• Revenue Officer

• Remarks



Output



Empty Partition Case



\---



\# Stage 2 — Select Village



Purpose



Associate the case with one revenue village.



Input



Village



Validation



Village must exist.



Village cannot change afterwards.



\---



\# Stage 3 — Select Jamabandi



Purpose



Choose the Jamabandi on which partition is to be carried out.



Validation



Only one Jamabandi per case.



\---



\# Stage 4 — Load Existing Records



Load



• Owners

• Khewats

• Khasras

• Ownership

• Cultivation



Nothing is editable.



This is the frozen source dataset.



\---



\# Stage 5 — Allocation Workspace



Purpose



Prepare proposed partition.



Operations



Allocate parcel



Split parcel



Merge parcel



Transfer ownership



Create new holdings



\---



\# Stage 6 — Validation



Validate



Total Area



Total Shares



Ownership



Parcel duplication



Unallocated parcels



Duplicate ownership



Every validation must pass before generation.



\---



\# Stage 7 — Generation



Generate



New Khewats



New Ownership



New Parcel Mapping



New Revenue Structure



Generation is repeatable.



\---



\# Stage 8 — Reports



Generate



Draft Partition Order



Khewat Register



Owner Register



Parcel Register



Allocation Register



Summary Report



\---



\# Stage 9 — Close Case



Freeze the generated structure.



Archive workflow.



Prevent accidental modification.



