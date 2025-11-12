### Query : Database 
```
CREATE DATABASE IF NOT EXISTS debit_card_specializing;
USE debit_card_specializing;
```
#### Query : Table 1
```
CREATE TABLE customers (
    CustomerID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Segment VARCHAR(100) NULL,
    Currency VARCHAR(10) NULL
);
```
#### Query : Table 2
```
CREATE TABLE gasstations (
    GasStationID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ChainID INT NULL,
    Country VARCHAR(100) NULL,
    Segment VARCHAR(100) NULL
);
```
#### Query : Table 3
```
CREATE TABLE products (
    ProductID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Description TEXT NULL
);
```
#### Query : Table 4
```
CREATE TABLE transactions_1k (
    TransactionID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Date DATE NULL,
    Time TIME NULL,
    CustomerID INT NULL,
    CardID INT NULL,
    GasStationID INT NULL,
    ProductID INT NULL,
    Amount INT NULL,
    Price DECIMAL(10,2) NULL,
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (GasStationID) REFERENCES gasstations(GasStationID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (ProductID) REFERENCES products(ProductID) ON UPDATE CASCADE ON DELETE SET NULL
);
```
#### Query : Table 5 
```
CREATE TABLE yearmonth (
    CustomerID INT NOT NULL,
    Date CHAR(7) NOT NULL, -- Format: YYYY-MM
    Consumption DECIMAL(10,2) NULL,
    PRIMARY KEY (Date, CustomerID),
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID) ON UPDATE CASCADE ON DELETE CASCADE
);
```
