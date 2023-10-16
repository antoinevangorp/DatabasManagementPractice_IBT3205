SET check_function_bodies = false
;

CREATE TABLE "DEPARTEMENT"(
  dnumber integer NOT NULL,
  dname integer,
  mgrssn integer NOT NULL,
  CONSTRAINT "DEPARTEMENT_pkey" PRIMARY KEY(dnumber)
);

CREATE TABLE "DEPARTMENT_LOCATIONS"
  (dnumber integer NOT NULL, "LOCATIONS_dlocation" integer NOT NULL);

CREATE TABLE "DEPENDENT"(
  dependentname text NOT NULL,
  essn integer NOT NULL,
  sex char,
  bdate timestamp,
  relationship text,
  CONSTRAINT "DEPENDENT_pkey" PRIMARY KEY(dependentname)
);

CREATE TABLE "DriversAssignments"(
  "AssignmentID" integer NOT NULL,
  "AssignmentData" date,
  "EMPLOYEE_ssn" integer NOT NULL,
  "Vehicles_VehicleID" integer NOT NULL,
  CONSTRAINT "DriversAssignments_pkey" PRIMARY KEY("AssignmentID")
);

CREATE TABLE "EMPLOYEE"(
  ssn integer NOT NULL,
  "superssn (FK)" integer NOT NULL,
  fname text,
  minit integer,
  lname text,
  address text,
  bdate timestamp,
  salary float8,
  sex char(M,W,X),
  dno integer NOT NULL,
  CONSTRAINT "EMPLOYEE_pkey" PRIMARY KEY(ssn)
);

CREATE TABLE "LOCATIONS"
  (dlocation integer NOT NULL, CONSTRAINT "LOCATIONS_pkey" PRIMARY KEY(dlocation))
  ;

CREATE TABLE "TransportationsAssignments"(
  "AssignmentID" integer NOT NULL,
  "LocationDepart" integer NOT NULL,
  "LocationEnd" integer NOT NULL,
  CONSTRAINT "TransportationsAssignments_pkey" PRIMARY KEY("AssignmentID")
);

CREATE TABLE "Vehicles"(
  "VehicleID" integer NOT NULL,
  "CurentLocation" integer,
  "LicensePlate" text NOT NULL,
  CONSTRAINT "Vehicles_pkey" PRIMARY KEY("VehicleID")
);

CREATE TABLE "VehiclesAssignments"(
  "AssignmentID" integer NOT NULL,
  "AssignmentData" date,
  "ServicID" integer NOT NULL,
  "Vehicles_VehicleID" integer NOT NULL,
  CONSTRAINT "VehiclesAssignments_pkey" PRIMARY KEY("AssignmentID")
);

ALTER TABLE "EMPLOYEE"
  ADD CONSTRAINT "EMPLOYEE_superssn (FK)_fkey"
    FOREIGN KEY ("superssn (FK)") REFERENCES "DEPARTEMENT" (dnumber);

ALTER TABLE "EMPLOYEE"
  ADD CONSTRAINT ssn_fkey FOREIGN KEY (dno) REFERENCES "EMPLOYEE" (ssn);

ALTER TABLE "DEPARTEMENT"
  ADD CONSTRAINT "DEPARTEMENT_mgrssn_fkey"
    FOREIGN KEY (mgrssn) REFERENCES "EMPLOYEE" (ssn);

ALTER TABLE "DEPARTMENT_LOCATIONS"
  ADD CONSTRAINT "DEPARTMENT_LOCATIONS_dnumber_fkey"
    FOREIGN KEY (dnumber) REFERENCES "DEPARTEMENT" (dnumber);

ALTER TABLE "DEPARTMENT_LOCATIONS"
  ADD CONSTRAINT "DEPARTMENT_LOCATIONS_LOCATIONS_dlocation_fkey"
    FOREIGN KEY ("LOCATIONS_dlocation") REFERENCES "LOCATIONS" (dlocation);

ALTER TABLE "DEPENDENT"
  ADD CONSTRAINT "DEPENDENT_essn_fkey"
    FOREIGN KEY (essn) REFERENCES "EMPLOYEE" (ssn);

ALTER TABLE "TransportationsAssignments"
  ADD CONSTRAINT "TransportationsAssignments_LocationDepart_fkey"
    FOREIGN KEY ("LocationDepart") REFERENCES "LOCATIONS" (dlocation);

ALTER TABLE "TransportationsAssignments"
  ADD CONSTRAINT "TrensportationsAssignments_LOCATIONS_dlocation_fkey1"
    FOREIGN KEY ("LocationEnd") REFERENCES "LOCATIONS" (dlocation);

ALTER TABLE "Vehicles"
  ADD CONSTRAINT "Vehicles_CurentLocation_fkey"
    FOREIGN KEY ("CurentLocation") REFERENCES "LOCATIONS" (dlocation);

ALTER TABLE "VehiclesAssignments"
  ADD CONSTRAINT "VehiclesAssignments_ServicID_fkey"
    FOREIGN KEY ("ServicID")
      REFERENCES "TransportationsAssignments" ("AssignmentID");

ALTER TABLE "VehiclesAssignments"
  ADD CONSTRAINT "VehiclesAssignments_Vehicles_VehicleID_fkey"
    FOREIGN KEY ("Vehicles_VehicleID") REFERENCES "Vehicles" ("VehicleID");

ALTER TABLE "DriversAssignments"
  ADD CONSTRAINT "DriversAssignments_EMPLOYEE_ssn_fkey"
    FOREIGN KEY ("EMPLOYEE_ssn") REFERENCES "EMPLOYEE" (ssn);

ALTER TABLE "DriversAssignments"
  ADD CONSTRAINT "DriversAssignments_Vehicles_VehicleID_fkey"
    FOREIGN KEY ("Vehicles_VehicleID") REFERENCES "Vehicles" ("VehicleID");
