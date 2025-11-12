### Database : financial
```
CREATE DATABASE IF NOT EXISTS financial;
USE financial;
```
#### Query : Table 1
```
CREATE TABLE district (
    district_id INT NOT NULL PRIMARY KEY,
    A2 VARCHAR(255) NOT NULL,
    A3 VARCHAR(255) NOT NULL,
    A4 VARCHAR(255) NOT NULL,
    A5 VARCHAR(255) NOT NULL,
    A6 VARCHAR(255) NOT NULL,
    A7 VARCHAR(255) NOT NULL,
    A8 INT NOT NULL,
    A9 INT NOT NULL,
    A10 DECIMAL(10,2) NOT NULL,
    A11 INT NOT NULL,
    A12 DECIMAL(10,2),
    A13 DECIMAL(10,2) NOT NULL,
    A14 INT NOT NULL,
    A15 INT,
    A16 INT NOT NULL
);
```
#### Query : Table 2
```
CREATE TABLE client (
    client_id INT NOT NULL PRIMARY KEY,
    gender VARCHAR(10) NOT NULL,
    birth_date DATE NOT NULL,
    district_id INT NOT NULL,
    FOREIGN KEY (district_id) REFERENCES district(district_id)
);
```
#### Query : Table 3
```
CREATE TABLE account (
    account_id INT NOT NULL PRIMARY KEY,
    district_id INT NOT NULL,
    frequency VARCHAR(50) NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (district_id) REFERENCES district(district_id)
);
```
#### Query : Table 4
```
CREATE TABLE disp (
    disp_id INT NOT NULL PRIMARY KEY,
    client_id INT NOT NULL,
    account_id INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account(account_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);
```
#### Query : Table 5
```
CREATE TABLE card (
    card_id INT NOT NULL PRIMARY KEY,
    disp_id INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    issued DATE NOT NULL,
    FOREIGN KEY (disp_id) REFERENCES disp(disp_id)
);
```
#### Query : Table 6
```
CREATE TABLE loan (
    loan_id INT NOT NULL PRIMARY KEY,
    account_id INT NOT NULL,
    date DATE NOT NULL,
    amount INT NOT NULL,
    duration INT NOT NULL,
    payments DECIMAL(10,2) NOT NULL,
    status VARCHAR(10) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account(account_id)
);
```
#### Query : Table 7
```
CREATE TABLE `order` (
    order_id INT NOT NULL PRIMARY KEY,
    account_id INT NOT NULL,
    bank_to VARCHAR(50) NOT NULL,
    account_to INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    k_symbol VARCHAR(50) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account(account_id)
);
```
#### Query : Table 8
```
CREATE TABLE trans (
    trans_id INT NOT NULL PRIMARY KEY,
    account_id INT NOT NULL,
    date DATE NOT NULL,
    type VARCHAR(50) NOT NULL,
    operation VARCHAR(50),
    amount DECIMAL(10,2) NOT NULL,
    balance DECIMAL(10,2) NOT NULL,
    k_symbol VARCHAR(50),
    bank VARCHAR(50),
    account INT,
    FOREIGN KEY (account_id) REFERENCES account(account_id)
);
```
