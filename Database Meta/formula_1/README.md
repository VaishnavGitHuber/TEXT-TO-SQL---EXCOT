#### Query : Database 
```
CREATE DATABASE IF NOT EXISTS formula_1;
USE formula_1;
```
#### Query : Table 1
```
CREATE TABLE seasons (
    year INT NOT NULL PRIMARY KEY,
    url VARCHAR(255) NOT NULL UNIQUE
);
```
#### Query : Table 2
```
CREATE TABLE circuits (
    circuitId INT AUTO_INCREMENT PRIMARY KEY,
    circuitRef VARCHAR(100) NOT NULL DEFAULT '',
    name VARCHAR(255) NOT NULL DEFAULT '',
    location VARCHAR(255),
    country VARCHAR(100),
    lat DECIMAL(10,6),
    lng DECIMAL(10,6),
    alt INT,
    url VARCHAR(255) NOT NULL UNIQUE
);
```
#### Query : Table 3
```
CREATE TABLE constructors (
    constructorId INT AUTO_INCREMENT PRIMARY KEY,
    constructorRef VARCHAR(100) NOT NULL DEFAULT '',
    name VARCHAR(255) NOT NULL UNIQUE,
    nationality VARCHAR(100),
    url VARCHAR(255) NOT NULL
);
```
#### Query : Table 4
```
CREATE TABLE drivers (
    driverId INT AUTO_INCREMENT PRIMARY KEY,
    driverRef VARCHAR(100) NOT NULL DEFAULT '',
    number INT,
    code VARCHAR(10),
    forename VARCHAR(100) NOT NULL DEFAULT '',
    surname VARCHAR(100) NOT NULL DEFAULT '',
    dob DATE,
    nationality VARCHAR(100),
    url VARCHAR(255) NOT NULL UNIQUE
);
```
#### Query : Table 5
```
CREATE TABLE status (
    statusId INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(100) NOT NULL DEFAULT ''
);
```
#### Query : Table 6
```
CREATE TABLE races (
    raceId INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL,
    round INT NOT NULL,
    circuitId INT NOT NULL,
    name VARCHAR(255) NOT NULL DEFAULT '',
    date DATE NOT NULL DEFAULT '0000-00-00',
    time VARCHAR(50),
    url VARCHAR(255) UNIQUE,
    FOREIGN KEY (year) REFERENCES seasons(year),
    FOREIGN KEY (circuitId) REFERENCES circuits(circuitId)
);
```
#### Query : Table 7
```
CREATE TABLE constructorResults (
    constructorResultsId INT AUTO_INCREMENT PRIMARY KEY,
    raceId INT NOT NULL,
    constructorId INT NOT NULL,
    points DECIMAL(10,2),
    status VARCHAR(50),
    FOREIGN KEY (raceId) REFERENCES races(raceId),
    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId)
);
```
#### Query : Table 8
```
CREATE TABLE constructorStandings (
    constructorStandingsId INT AUTO_INCREMENT PRIMARY KEY,
    raceId INT NOT NULL,
    constructorId INT NOT NULL,
    points DECIMAL(10,2) NOT NULL DEFAULT 0,
    position INT,
    positionText VARCHAR(10),
    wins INT NOT NULL DEFAULT 0,
    FOREIGN KEY (raceId) REFERENCES races(raceId),
    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId)
);
```
#### Query : Table 9
```
CREATE TABLE driverStandings (
    driverStandingsId INT AUTO_INCREMENT PRIMARY KEY,
    raceId INT NOT NULL,
    driverId INT NOT NULL,
    points DECIMAL(10,2) NOT NULL DEFAULT 0,
    position INT,
    positionText VARCHAR(10),
    wins INT NOT NULL DEFAULT 0,
    FOREIGN KEY (raceId) REFERENCES races(raceId),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);
```
#### Query : Table 10
```
CREATE TABLE qualifying (
    qualifyId INT AUTO_INCREMENT PRIMARY KEY,
    raceId INT NOT NULL,
    driverId INT NOT NULL,
    constructorId INT NOT NULL,
    number INT NOT NULL DEFAULT 0,
    position INT,
    q1 VARCHAR(20),
    q2 VARCHAR(20),
    q3 VARCHAR(20),
    FOREIGN KEY (raceId) REFERENCES races(raceId),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId),
    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId)
);
```
#### Query : Table 11
```
CREATE TABLE results (
    resultId INT AUTO_INCREMENT PRIMARY KEY,
    raceId INT NOT NULL,
    driverId INT NOT NULL,
    constructorId INT NOT NULL,
    number INT,
    grid INT NOT NULL DEFAULT 0,
    position INT,
    positionText VARCHAR(10) NOT NULL DEFAULT '',
    positionOrder INT NOT NULL DEFAULT 0,
    points DECIMAL(10,2) NOT NULL DEFAULT 0,
    laps INT NOT NULL DEFAULT 0,
    time VARCHAR(50),
    milliseconds INT,
    fastestLap INT,
    rank INT DEFAULT 0,
    fastestLapTime VARCHAR(20),
    fastestLapSpeed VARCHAR(20),
    statusId INT NOT NULL,
    FOREIGN KEY (raceId) REFERENCES races(raceId),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId),
    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId),
    FOREIGN KEY (statusId) REFERENCES status(statusId)
);
```
#### Query : Table 12
```
CREATE TABLE lapTimes (
    raceId INT NOT NULL,
    driverId INT NOT NULL,
    lap INT NOT NULL,
    position INT,
    time VARCHAR(20),
    milliseconds INT,
    PRIMARY KEY (raceId, driverId, lap),
    FOREIGN KEY (raceId) REFERENCES races(raceId),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);
```
#### Query : Table 13
```
CREATE TABLE pitStops (
    raceId INT NOT NULL,
    driverId INT NOT NULL,
    stop INT NOT NULL,
    lap INT NOT NULL,
    time VARCHAR(20) NOT NULL,
    duration VARCHAR(20),
    milliseconds INT,
    PRIMARY KEY (raceId, driverId, stop),
    FOREIGN KEY (raceId) REFERENCES races(raceId),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);
```
