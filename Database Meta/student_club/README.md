### Query : Database 
```
CREATE DATABASE IF NOT EXISTS student_club;
USE student_club;
```
### Query : Table 1
```
CREATE TABLE IF NOT EXISTS zip_code (
    zip_code INT PRIMARY KEY,
    type VARCHAR(50),
    city VARCHAR(100),
    county VARCHAR(100),
    state VARCHAR(100),
    short_state VARCHAR(10)
) ENGINE=InnoDB;
```
### Query : Table 2
```
CREATE TABLE IF NOT EXISTS major (
    major_id VARCHAR(50) PRIMARY KEY,
    major_name VARCHAR(100),
    department VARCHAR(100),
    college VARCHAR(100)
) ENGINE=InnoDB;
```
### Query : Table 3
```
CREATE TABLE IF NOT EXISTS member (
    member_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(150),
    position VARCHAR(100),
    t_shirt_size VARCHAR(10),
    phone VARCHAR(20),
    zip INT,
    link_to_major VARCHAR(50),
    FOREIGN KEY (link_to_major) REFERENCES major(major_id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (zip) REFERENCES zip_code(zip_code)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;
```
### Query : Table 4
```
CREATE TABLE IF NOT EXISTS event (
    event_id VARCHAR(50) PRIMARY KEY,
    event_name VARCHAR(150),
    event_date DATE,
    type VARCHAR(100),
    notes TEXT,
    location VARCHAR(150),
    status VARCHAR(50)
) ENGINE=InnoDB;
```
### Query : Table 5
```
CREATE TABLE IF NOT EXISTS attendance (
    link_to_event VARCHAR(50),
    link_to_member VARCHAR(50),
    PRIMARY KEY (link_to_event, link_to_member),
    FOREIGN KEY (link_to_event) REFERENCES event(event_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (link_to_member) REFERENCES member(member_id)
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;
```
### Query : Table 6
```
CREATE TABLE IF NOT EXISTS budget (
    budget_id VARCHAR(50) PRIMARY KEY,
    category VARCHAR(100),
    spent DECIMAL(10,2),
    remaining DECIMAL(10,2),
    amount DECIMAL(10,2),
    event_status VARCHAR(50),
    link_to_event VARCHAR(50),
    FOREIGN KEY (link_to_event) REFERENCES event(event_id)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;
```
### Query : Table 7
```
CREATE TABLE IF NOT EXISTS expense (
    expense_id VARCHAR(50) PRIMARY KEY,
    expense_description TEXT,
    expense_date DATE,
    cost DECIMAL(10,2),
    approved VARCHAR(10),
    link_to_member VARCHAR(50),
    link_to_budget VARCHAR(50),
    FOREIGN KEY (link_to_budget) REFERENCES budget(budget_id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (link_to_member) REFERENCES member(member_id)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;
```
### Query : Table 8
```
CREATE TABLE IF NOT EXISTS income (
    income_id VARCHAR(50) PRIMARY KEY,
    date_received DATE,
    amount DECIMAL(10,2),
    source VARCHAR(150),
    notes TEXT,
    link_to_member VARCHAR(50),
    FOREIGN KEY (link_to_member) REFERENCES member(member_id)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;
```
