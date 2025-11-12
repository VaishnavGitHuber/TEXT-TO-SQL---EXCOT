### Database : toxicology
```
CREATE DATABASE IF NOT EXISTS toxicology;
USE toxicology;
```
#### Query : Table 1
```
CREATE TABLE IF NOT EXISTS molecule (
    molecule_id VARCHAR(64) NOT NULL,
    label VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (molecule_id)
) ENGINE=InnoDB;
```
#### Query : Table 2
```
CREATE TABLE IF NOT EXISTS atom (
    atom_id VARCHAR(64) NOT NULL,
    molecule_id VARCHAR(64) DEFAULT NULL,
    element VARCHAR(10) DEFAULT NULL,
    PRIMARY KEY (atom_id),
    FOREIGN KEY (molecule_id) REFERENCES molecule(molecule_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE=InnoDB;
```
#### Query : Table 3
```
CREATE TABLE IF NOT EXISTS bond (
    bond_id VARCHAR(64) NOT NULL,
    molecule_id VARCHAR(64) DEFAULT NULL,
    bond_type VARCHAR(20) DEFAULT NULL,
    PRIMARY KEY (bond_id),
    FOREIGN KEY (molecule_id) REFERENCES molecule(molecule_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE=InnoDB;
```
#### Query : Table 4
```
CREATE TABLE IF NOT EXISTS connected (
    atom_id VARCHAR(64) NOT NULL,
    atom_id2 VARCHAR(64) NOT NULL,
    bond_id VARCHAR(64) DEFAULT NULL,
    PRIMARY KEY (atom_id, atom_id2),
    FOREIGN KEY (atom_id) REFERENCES atom(atom_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (atom_id2) REFERENCES atom(atom_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (bond_id) REFERENCES bond(bond_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;
```
