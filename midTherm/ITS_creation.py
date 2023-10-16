import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect('ITS_Database.db')
cur = conn.cursor()

# SQL statements for table creation

# Create "Vehicles" table
create_vehicles_sql = '''
CREATE TABLE IF NOT EXISTS Vehicles (
    VehicleID TEXT PRIMARY KEY,
    RegistrationID VARCHAR(20) NOT NULL,
    Manufacturer VARCHAR(50) NOT NULL,
    Model VARCHAR(50) NOT NULL,
    Color VARCHAR(20) NOT NULL,
    CurrentOdometer INT NOT NULL,
    PassengerCapacity INT NOT NULL
);
'''

# Create "MaintenanceRepairs" table
create_maintenance_repairs_sql = '''
CREATE TABLE IF NOT EXISTS "MaintenanceRepairs" (
    ActionID INT PRIMARY KEY,
    VehicleID TEXT,
    ActionType CHAR CHECK(ActionType IN ('M', 'R')) NOT NULL,
    Odometer INT NOT NULL,
    Cost DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    ActionDate DATE NOT NULL
);
'''

# Create "Countries" table
create_countries_sql = '''
CREATE TABLE IF NOT EXISTS Countries (
    CountryCode CHAR(2) PRIMARY KEY,
    CountryName VARCHAR(50) NOT NULL
);
'''

# Create "SpokenLanguages" table
create_spoken_languages_sql = '''
CREATE TABLE IF NOT EXISTS SpokenLanguages (
    LanguageID INT PRIMARY KEY,
    CountryCode CHAR(2),
    LanguageCode CHAR(2) NOT NULL,
    FOREIGN KEY (CountryCode) REFERENCES Countries(CountryCode)
);
'''

# Create "GameOfficials" table
create_game_officials_sql = '''
CREATE TABLE IF NOT EXISTS GameOfficials (
    OfficialID INT PRIMARY KEY,
    CountryCode CHAR(2) NOT NULL,
    IncheonCityID CHAR(8) NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Role VARCHAR(50) NOT NULL,
    PreferredLanguage CHAR(2) NOT NULL,
    FOREIGN KEY (CountryCode) REFERENCES Countries(CountryCode)
);
'''

# Create "Drivers" table
create_drivers_sql = '''
CREATE TABLE IF NOT EXISTS Drivers (
    DriverID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    LicenseNumber CHAR(18) NOT NULL,
    ClearanceLevel INT CHECK (ClearanceLevel BETWEEN 1 AND 4),
    FATLLevel INT CHECK (FATLLevel BETWEEN 1 AND 10),
    FATLQualificationDate DATE,
    STLVTLevel INT CHECK (STLVTLevel BETWEEN 1 AND 5),
    STLVTQualificationDate DATE,
    CertifyingAuthority VARCHAR(100)
);
'''

# Create "DriverBookings" table
create_driver_bookings_sql = '''
CREATE TABLE IF NOT EXISTS DriverBookings (
    BookingID INT PRIMARY KEY,
    OfficialID INT,
    DriverID INT,
    VehicleID TEXT,
    PickupLocation VARCHAR(100),
    DropOffLocation VARCHAR(100),
    LocationType TEXT CHECK(LocationType IN ('Hotel', 'Airport', 'Aquatic Center')),
    BookingReference VARCHAR(20),
    StartDateTime DATETIME NOT NULL,
    EndDateTime DATETIME NOT NULL,
    StartOdometer INT NOT NULL,
    EndOdometer INT NOT NULL,
    FOREIGN KEY (OfficialID) REFERENCES GameOfficials(OfficialID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);
'''

# Create "VehicleAvailability" table
create_vehicle_availability_sql = '''
CREATE TABLE IF NOT EXISTS VehicleAvailability (
    VehicleID TEXT PRIMARY KEY,
    IsAvailable BOOLEAN NOT NULL
);
'''

# Execute the table creation SQL statements
cur.execute(create_vehicles_sql)
cur.execute(create_maintenance_repairs_sql)
cur.execute(create_countries_sql)
cur.execute(create_spoken_languages_sql)
cur.execute(create_game_officials_sql)
cur.execute(create_drivers_sql)
cur.execute(create_driver_bookings_sql)
cur.execute(create_vehicle_availability_sql)

# Commit the changes
conn.commit()

# Sample data for "Vehicles" table
sample_vehicle_data = '''
INSERT INTO Vehicles (VehicleID, RegistrationID, Manufacturer, Model, Color, CurrentOdometer, PassengerCapacity)
VALUES ('V1000', '2001 ABC', 'Volvo', 'XC90 SE', 'Silver', 4350, 4),
       ('V1001', '2006 AFD', 'Kia', 'K7', 'Black', 2195, 4),
       ('V1002', '2021 AHR', 'Tesla', '2020 F', 'White', 509, 4),
       ('V1003', '2020 DXF', 'Ford', 'Transit', 'Silver', 974, 2);
'''

# Sample data for "Countries" table
sample_countries_data = '''
INSERT INTO Countries (CountryCode, CountryName)
VALUES ('KR', 'South Korea'),
       ('US', 'United States'),
       ('CN', 'China');
'''

# Sample data for "SpokenLanguages" table
sample_languages_data = '''
INSERT INTO SpokenLanguages (LanguageID, CountryCode, LanguageCode)
VALUES (1, 'KR', 'KO'),
       (2, 'US', 'EN'),
       (3, 'CN', 'ZH');
'''

# Sample data for "GameOfficials" table
sample_officials_data = '''
INSERT INTO GameOfficials (OfficialID, CountryCode, IncheonCityID, FirstName, LastName, Role, PreferredLanguage)
VALUES (1, 'KR', 'INC12345', 'Ji-Sung', 'Park', 'Referee', 'KO'),
       (2, 'US', 'INC67890', 'John', 'Smith', 'Referee', 'EN');
'''

# Sample data for "Drivers" table
sample_drivers_data = '''
INSERT INTO Drivers (DriverID, Name, LicenseNumber, ClearanceLevel, FATLLevel, FATLQualificationDate, STLVTLevel, STLVTQualificationDate, CertifyingAuthority)
VALUES (1, 'Hye-Jin Kim', '123456789012345678', 3, 7, '2021-05-15', 4, '2022-02-20', 'Korean DMV'),
       (2, 'Robert Johnson', '987654321098765432', 2, 5, '2020-08-10', 3, '2021-12-05', 'US DMV');
'''

# Sample data for "DriverBookings" table
sample_booking_data = '''
INSERT INTO DriverBookings (BookingID, OfficialID, DriverID, VehicleID, PickupLocation, DropOffLocation, LocationType, BookingReference, StartDateTime, EndDateTime, StartOdometer, EndOdometer)
VALUES (1, 1, 1, 'V1000', 'Incheon Hotel', 'Incheon Airport', 'Hotel', 'REF12345', '2023-10-01 08:00', '2023-10-01 12:00', 4350, 4370),
       (2, 2, 2, 'V1001', 'Incheon Airport', 'Incheon Aquatic Center', 'Airport', 'REF67890', '2023-10-02 09:30', '2023-10-02 13:30', 2195, 2210);
'''

# Sample data for "VehicleAvailability" table
sample_availability_data = '''
INSERT INTO VehicleAvailability (VehicleID, IsAvailable)
VALUES ('V1000', 1),
       ('V1001', 0),
       ('V1002', 1),
       ('V1003', 1);
'''

# Sample data for "MaintenanceRepairs" table
sample_maintenance_repairs_data = '''
INSERT INTO MaintenanceRepairs (ActionID, VehicleID, ActionType, Odometer, Cost, Description, ActionDate)
VALUES (1, 'V1000', 'M', 4300, 300.00, 'Routine maintenance', '2023-09-15'),
       (2, 'V1001', 'R', 2150, 750.50, 'Engine repair', '2023-08-20');
'''


# Execute the sample data insertion SQL statements
cur.execute(sample_vehicle_data)
cur.execute(sample_countries_data)
cur.execute(sample_languages_data)
cur.execute(sample_officials_data)
cur.execute(sample_drivers_data)
cur.execute(sample_booking_data)
cur.execute(sample_availability_data)
cur.execute(sample_maintenance_repairs_data)

# Commit the changes
conn.commit()

# Function to print the contents of a table
def print_table_contents(table_name):
    print(f"Contents of the '{table_name}' table:")
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("")

# Print the contents of each table
print_table_contents('Vehicles')
print_table_contents('MaintenanceRepairs')
print_table_contents('Countries')
print_table_contents('SpokenLanguages')
print_table_contents('GameOfficials')
print_table_contents('Drivers')
print_table_contents('DriverBookings')
print_table_contents('VehicleAvailability')

# Close the cursor and connection
cur.close()
conn.close()
