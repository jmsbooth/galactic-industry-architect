-- Initialize the EVE Online Industry Planning Database

-- Create Users Table
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Email VARCHAR(100)
);

-- Create Blueprints Table
CREATE TABLE Blueprints (
    BlueprintID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    TypeID INTEGER NOT NULL,
    MaterialEfficiency INTEGER,
    TimeEfficiency INTEGER
);

-- Create Materials Table
CREATE TABLE Materials (
    MaterialID SERIAL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Volume FLOAT
);

-- Create BlueprintMaterials Table
CREATE TABLE BlueprintMaterials (
    BlueprintID INTEGER REFERENCES Blueprints(BlueprintID),
    MaterialID INTEGER REFERENCES Materials(MaterialID),
    Quantity INTEGER NOT NULL,
    PRIMARY KEY(BlueprintID, MaterialID)
);

-- Create Stations Table
CREATE TABLE Stations (
    StationID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100)
);

-- Create MiningActivities Table
CREATE TABLE MiningActivities (
    ActivityID SERIAL PRIMARY KEY,
    UserID INTEGER REFERENCES Users(UserID),
    AsteroidType VARCHAR(50),
    StartTime TIMESTAMP,
    EndTime TIMESTAMP,
    QuantityMined INTEGER
);

-- Create IndustryJobs Table
CREATE TABLE IndustryJobs (
    JobID SERIAL PRIMARY KEY,
    BlueprintID INTEGER REFERENCES Blueprints(BlueprintID),
    StationID INTEGER REFERENCES Stations(StationID),
    StartTime TIMESTAMP,
    EndTime TIMESTAMP,
    Status VARCHAR(50)
);

-- Create PlanetaryInteraction Table
CREATE TABLE PlanetaryInteraction (
    ProjectID SERIAL PRIMARY KEY,
    UserID INTEGER REFERENCES Users(UserID),
    PlanetType VARCHAR(50),
    Structure VARCHAR(100),
    StartTime TIMESTAMP,
    EndTime TIMESTAMP,
    ProductionRate INTEGER
);

-- Create Groups Table
CREATE TABLE Groups (
    GroupID SERIAL PRIMARY KEY,
    GroupName VARCHAR(100) NOT NULL
);

-- Create ItemTypes Table
CREATE TABLE ItemTypes (
    TypeID SERIAL PRIMARY KEY,
    TypeName VARCHAR(100) NOT NULL,
    GroupID INTEGER REFERENCES Groups(GroupID)
);
