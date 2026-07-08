\# Haryana Partition Manager Architecture



\## Layered Design



GUI



↓



Services



↓



Repositories



↓



ORM



↓



SQLite



\---



\## Presentation Layer



Responsible for



\- windows

\- dialogs

\- widgets

\- navigation



No business rules.



No SQL.



\---



\## Service Layer



Responsible for



\- validation



\- ownership rules



\- partition rules



\- calculations



\- transactions



\---



\## Repository Layer



Responsible only for



\- loading



\- saving



\- deleting



\- searching



No business decisions.



\---



\## Persistence Layer



SQLAlchemy ORM



SQLite



Future compatible with PostgreSQL.



\---



\## Business Entities



Village



Owner



Khewat



Parcel



Ownership



Partition Case



Allocation



History



Documents



\---



\## Future Identity Strategy



Every entity



UUID



Business Numbers



Village



Hadbast



Khewat



Khewat Number



Parcel



Khasra Number



These remain visible to users.



UUID remains internal.



\---



\## Transactions



Partition



Merge



Ownership Change



Allocation



must execute atomically.



Commit only after complete success.



Rollback on failure.

