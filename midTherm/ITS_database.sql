SET check_function_bodies = false
;

CREATE TABLE "Countries"(
"CountryCode" char(2) NOT NULL, "CountryName" char(50) NOT NULL,
  CONSTRAINT "Countries_pkey" PRIMARY KEY("CountryCode")
);

CREATE TABLE "DriverBookings"(
  "BookingID" integer NOT NULL,
  "OfficialID" integer NOT NULL,
  "DriverID" integer NOT NULL,
  "VehicleID" text NOT NULL,
  "PickupLocation" varchar(100),
  "DropOffLocation" varchar(100),
  "LocationType" text CHECK("LocationType" IN ('Hotel', 'Airport', 'Aquatic Center')),
  "BookingReference" varchar(20),
  "StartDateTime" time NOT NULL,
  "EndDateTime" time NOT NULL,
  "StartOdometer" integer NOT NULL,
  "EndOdometer" integer NOT NULL,
  CONSTRAINT "DriverBookings_pkey" PRIMARY KEY("BookingID")
);

CREATE TABLE "Drivers"(
  "DriverID" integer NOT NULL,
  "Name" varchar(100) NOT NULL,
  "LicenseNumber" char(18) NOT NULL,
  "ClearanceLevel" integer CHECK(ClearanceLevel BETWEEN 1 AND 4),
  "FATLLevel" integer CHECK(ClearanceLevel BETWEEN 1 AND 10),
  "FATLQualificationDate" date,
  "STLVTLevel" integer CHECK(ClearanceLevel BETWEEN 1 AND 5),
  "STLVTQualificationDate" date,
  "CertifyingAuthority" varchar(100),
  CONSTRAINT "Drivers_pkey" PRIMARY KEY("DriverID")
);

CREATE TABLE "GameOfficials"(
  "OfficialID" integer NOT NULL,
  "CountryCode" char(2) NOT NULL,
  "IncheonCityID" char(8) NOT NULL,
  "FirstName" varchar(50) NOT NULL,
  "LastName" varchar(50) NOT NULL,
  "Role" varchar(50) NOT NULL,
  "PreferredLanguage" char(2) NOT NULL,
  CONSTRAINT "GameOfficials_pkey" PRIMARY KEY("OfficialID")
);

CREATE TABLE "MaintenanceRepairs"(
  "ActionID" integer NOT NULL,
  "Vehicles_VehicleID" text NOT NULL,
  "ActionType" char CHECK("ActionType" IN ('M', 'R')) NOT NULL,
  "Odometer" integer NOT NULL,
  "Cost" integer(10, 2) NOT NULL,
  "Description" text,
  "ActionDate" date NOT NULL,
  CONSTRAINT "MaintenanceRepairs_pkey" PRIMARY KEY("ActionID")
);

CREATE TABLE "SpokenLanguages"(
  "LanguageID" integer NOT NULL,
  "CountryCode" char(2) NOT NULL,
  "LanguageCode" integer NOT NULL,
  CONSTRAINT "SpokenLanguages_pkey" PRIMARY KEY("LanguageID")
);

CREATE TABLE "VehicleAvailability"
  ("VehicleID" text NOT NULL, "IsAvailable" boolean NOT NULL);

CREATE TABLE "Vehicles"(
  "VehicleID" text NOT NULL,
  "RegistrationID" varchar(20) NOT NULL,
  "Manufacturer" varchar(50) NOT NULL,
  "Model" varchar(50) NOT NULL,
  "Color" varchar(50) NOT NULL,
  "CurrentOdometer" integer NOT NULL,
  "PassengerCapacity" integer NOT NULL,
  CONSTRAINT "Vehicles_pkey" PRIMARY KEY("VehicleID")
);

ALTER TABLE "MaintenanceRepairs"
  ADD CONSTRAINT "MaintenanceRepairs_Vehicles_VehicleID_fkey"
    FOREIGN KEY ("Vehicles_VehicleID") REFERENCES "Vehicles" ("VehicleID");

ALTER TABLE "SpokenLanguages"
  ADD CONSTRAINT "SpokenLanguages_CountryCode_fkey"
    FOREIGN KEY ("CountryCode") REFERENCES "Countries" ("CountryCode");

ALTER TABLE "GameOfficials"
  ADD CONSTRAINT "GameOfficials_CountryCode_fkey"
    FOREIGN KEY ("CountryCode") REFERENCES "Countries" ("CountryCode");

ALTER TABLE "DriverBookings"
  ADD CONSTRAINT "DriverBookings_OfficialID_fkey"
    FOREIGN KEY ("OfficialID") REFERENCES "GameOfficials" ("OfficialID");

ALTER TABLE "DriverBookings"
  ADD CONSTRAINT "DriverBookings_DriverID_fkey"
    FOREIGN KEY ("DriverID") REFERENCES "Drivers" ("DriverID");

ALTER TABLE "DriverBookings"
  ADD CONSTRAINT "DriverBookings_VehicleID_fkey"
    FOREIGN KEY ("VehicleID") REFERENCES "Vehicles" ("VehicleID");

ALTER TABLE "VehicleAvailability"
  ADD CONSTRAINT "VehicleAvailability_VehicleID_fkey"
    FOREIGN KEY ("VehicleID") REFERENCES "Vehicles" ("VehicleID");
