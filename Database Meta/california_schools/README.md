### Database : california_schools

#### Query : Create a database 
```
CREATE DATABASE IF NOT EXISTS california_schools;
USE california_schools;
```

#### Query : Table 1 
```
CREATE TABLE IF NOT EXISTS schools (
    CDSCode VARCHAR(20) NOT NULL PRIMARY KEY,
    NCESDist VARCHAR(50),
    NCESSchool VARCHAR(50),
    StatusType VARCHAR(50) NOT NULL,
    County VARCHAR(100) NOT NULL,
    District VARCHAR(100) NOT NULL,
    School VARCHAR(150),
    Street VARCHAR(150),
    StreetAbr VARCHAR(20),
    City VARCHAR(100),
    `Zip` VARCHAR(10),
    `State` VARCHAR(10),
    MailStreet VARCHAR(150),
    MailStrAbr VARCHAR(20),
    MailCity VARCHAR(100),
    MailZip VARCHAR(10),
    MailState VARCHAR(10),
    Phone VARCHAR(20),
    `Ext` VARCHAR(10),
    Website VARCHAR(255),
    OpenDate DATE,
    ClosedDate DATE,
    Charter TINYINT(1),
    CharterNum VARCHAR(20),
    FundingType VARCHAR(50),
    DOC VARCHAR(100) NOT NULL,
    DOCType VARCHAR(50) NOT NULL,
    SOC VARCHAR(100),
    SOCType VARCHAR(50),
    EdOpsCode VARCHAR(50),
    EdOpsName VARCHAR(100),
    EILCode VARCHAR(50),
    EILName VARCHAR(100),
    GSoffered VARCHAR(50),
    GSserved VARCHAR(50),
    `Virtual` VARCHAR(20),
    Magnet TINYINT(1),
    Latitude DECIMAL(10,6),
    `Longitude` DECIMAL(10,6),
    AdmFName1 VARCHAR(100),
    AdmLName1 VARCHAR(100),
    AdmEmail1 VARCHAR(150),
    AdmFName2 VARCHAR(100),
    AdmLName2 VARCHAR(100),
    AdmEmail2 VARCHAR(150),
    AdmFName3 VARCHAR(100),
    AdmLName3 VARCHAR(100),
    AdmEmail3 VARCHAR(150),
    LastUpdate DATE NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
#### Query : Table 2 
```
CREATE TABLE IF NOT EXISTS frpm (
    CDSCode VARCHAR(20) NOT NULL PRIMARY KEY,
    `Academic Year` VARCHAR(20),
    `County Code` VARCHAR(10),
    `District Code` INT,
    `School Code` VARCHAR(10),
    `County Name` VARCHAR(100),
    `District Name` VARCHAR(150),
    `School Name` VARCHAR(150),
    `District Type` VARCHAR(50),
    `School Type` VARCHAR(50),
    `Educational Option Type` VARCHAR(100),
    `NSLP Provision Status` VARCHAR(100),
    `Charter School (Y/N)` TINYINT(1),
    `Charter School Number` VARCHAR(20),
    `Charter Funding Type` VARCHAR(50),
    IRC INT,
    `Low Grade` VARCHAR(10),
    `High Grade` VARCHAR(10),
    `Enrollment (K-12)` DECIMAL(10,2),
    `Free Meal Count (K-12)` DECIMAL(10,2),
    `Percent (%) Eligible Free (K-12)` DECIMAL(5,2),
    `FRPM Count (K-12)` DECIMAL(10,2),
    `Percent (%) Eligible FRPM (K-12)` DECIMAL(5,2),
    `Enrollment (Ages 5-17)` DECIMAL(10,2),
    `Free Meal Count (Ages 5-17)` DECIMAL(10,2),
    `Percent (%) Eligible Free (Ages 5-17)` DECIMAL(5,2),
    `FRPM Count (Ages 5-17)` DECIMAL(10,2),
    `Percent (%) Eligible FRPM (Ages 5-17)` DECIMAL(5,2),
    `2013-14 CALPADS Fall 1 Certification Status` TINYINT(1),
    CONSTRAINT fk_frpm_schools FOREIGN KEY (CDSCode) REFERENCES schools(CDSCode)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
#### Query 3 : Table 3
```
CREATE TABLE IF NOT EXISTS satscores (
    cds VARCHAR(20) NOT NULL PRIMARY KEY,
    rtype VARCHAR(50) NOT NULL,
    sname VARCHAR(150),
    dname VARCHAR(150),
    cname VARCHAR(150),
    enroll12 INT NOT NULL,
    NumTstTakr INT NOT NULL,
    AvgScrRead INT,
    AvgScrMath INT,
    AvgScrWrite INT,
    NumGE1500 INT,
    -- PctGE1500 DECIMAL(5,2),
    CONSTRAINT fk_satscores_schools FOREIGN KEY (cds) REFERENCES schools(CDSCode)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
