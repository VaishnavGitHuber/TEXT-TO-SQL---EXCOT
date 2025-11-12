#### Query : Database 
```
CREATE DATABASE IF NOT EXISTS superhero;
USE superhero;
```
#### Query : Table 1
```
CREATE TABLE IF NOT EXISTS alignment (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    alignment VARCHAR(50) DEFAULT NULL
) ENGINE=InnoDB;
```
#### Query : Table 2
```
CREATE TABLE IF NOT EXISTS attribute (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    attribute_name VARCHAR(100) DEFAULT NULL
) ENGINE=InnoDB;
```
#### Query : Table 3
```
CREATE TABLE IF NOT EXISTS colour (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    colour VARCHAR(50) DEFAULT NULL
) ENGINE=InnoDB;
```
#### Query : Table 4
```
CREATE TABLE IF NOT EXISTS gender (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    gender VARCHAR(50) DEFAULT NULL
) ENGINE=InnoDB;
```
#### Query : Table 5
```
CREATE TABLE IF NOT EXISTS publisher (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    publisher_name VARCHAR(100) DEFAULT NULL
) ENGINE=InnoDB;
```
#### Query : Table 6
```
CREATE TABLE IF NOT EXISTS race (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    race VARCHAR(100) DEFAULT NULL
) ENGINE=InnoDB;
```
#### Query : Table 7
```
CREATE TABLE IF NOT EXISTS superhero (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    superhero_name VARCHAR(100) DEFAULT NULL,
    full_name VARCHAR(150) DEFAULT NULL,
    gender_id INT DEFAULT NULL,
    eye_colour_id INT DEFAULT NULL,
    hair_colour_id INT DEFAULT NULL,
    skin_colour_id INT DEFAULT NULL,
    race_id INT DEFAULT NULL,
    publisher_id INT DEFAULT NULL,
    alignment_id INT DEFAULT NULL,
    height_cm INT DEFAULT NULL,
    weight_kg INT DEFAULT NULL,
    FOREIGN KEY (alignment_id) REFERENCES alignment(id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (eye_colour_id) REFERENCES colour(id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (hair_colour_id) REFERENCES colour(id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (skin_colour_id) REFERENCES colour(id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (gender_id) REFERENCES gender(id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (race_id) REFERENCES race(id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (publisher_id) REFERENCES publisher(id)
        ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB;
```
#### Query : Table 8
```
CREATE TABLE IF NOT EXISTS superpower (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    power_name VARCHAR(100) DEFAULT NULL
) ENGINE=InnoDB;
```
#### Query : Table 9
```
CREATE TABLE IF NOT EXISTS hero_attribute (
    hero_id INT DEFAULT NULL,
    attribute_id INT DEFAULT NULL,
    attribute_value INT DEFAULT NULL,
    FOREIGN KEY (hero_id) REFERENCES superhero(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (attribute_id) REFERENCES attribute(id)
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;
```
#### Query : Table 10
```
CREATE TABLE IF NOT EXISTS hero_power (
    hero_id INT DEFAULT NULL,
    power_id INT DEFAULT NULL,
    FOREIGN KEY (hero_id) REFERENCES superhero(id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (power_id) REFERENCES superpower(id)
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;
```
