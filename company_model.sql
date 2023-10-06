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

CREATE TABLE "EMPLOYEE"(
  ssn integer NOT NULL,
  "superssn (FK)" integer,
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

CREATE TABLE "EMPLOYEE_PROJECT"
  (ssn integer NOT NULL, "PROJECT_pnumber" integer NOT NULL, hours integer);

CREATE TABLE "LOCATIONS"
  (dlocation integer NOT NULL, CONSTRAINT "LOCATIONS_pkey" PRIMARY KEY(dlocation))
  ;

CREATE TABLE "PROJECT"(
  pnumber integer NOT NULL,
  pname text,
  plocation text,
  dnum integer NOT NULL,
  CONSTRAINT "PROJECT_pkey" PRIMARY KEY(pnumber)
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

ALTER TABLE "PROJECT"
  ADD CONSTRAINT "PROJECT_dnum_fkey"
    FOREIGN KEY (dnum) REFERENCES "DEPARTEMENT" (dnumber);

ALTER TABLE "DEPENDENT"
  ADD CONSTRAINT "DEPENDENT_essn_fkey"
    FOREIGN KEY (essn) REFERENCES "EMPLOYEE" (ssn);

ALTER TABLE "EMPLOYEE_PROJECT"
  ADD CONSTRAINT "EMPLOYEE_PROJECT_ssn_fkey"
    FOREIGN KEY (ssn) REFERENCES "EMPLOYEE" (ssn);

ALTER TABLE "EMPLOYEE_PROJECT"
  ADD CONSTRAINT "EMPLOYEE_PROJECT_PROJECT_pnumber_fkey"
    FOREIGN KEY ("PROJECT_pnumber") REFERENCES "PROJECT" (pnumber);
