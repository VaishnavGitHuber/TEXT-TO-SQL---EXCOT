#### Query : Database 
```
CREATE DATABASE IF NOT EXISTS european_football_2;
USE european_football_2;
```
#### Query : Table 1
```
CREATE TABLE Country (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);
```
#### Query : Table 2
```
CREATE TABLE League (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    country_id INT,
    name VARCHAR(100) UNIQUE,
    FOREIGN KEY (country_id)
        REFERENCES Country(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);
```
#### Query : Table 3
```
CREATE TABLE Player (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_api_id INT UNIQUE,
    player_name VARCHAR(100),
    player_fifa_api_id INT UNIQUE,
    birthday DATE,
    height INT,
    weight INT
);
```
#### Query : Table 4
```
CREATE TABLE Player_Attributes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_fifa_api_id INT,
    player_api_id INT,
    date DATE,
    overall_rating INT,
    potential INT,
    preferred_foot VARCHAR(10),
    attacking_work_rate VARCHAR(50),
    defensive_work_rate VARCHAR(50),
    crossing INT,
    finishing INT,
    heading_accuracy INT,
    short_passing INT,
    volleys INT,
    dribbling INT,
    curve INT,
    free_kick_accuracy INT,
    long_passing INT,
    ball_control INT,
    acceleration INT,
    sprint_speed INT,
    agility INT,
    reactions INT,
    balance INT,
    shot_power INT,
    jumping INT,
    stamina INT,
    strength INT,
    long_shots INT,
    aggression INT,
    interceptions INT,
    positioning INT,
    vision INT,
    penalties INT,
    marking INT,
    standing_tackle INT,
    sliding_tackle INT,
    gk_diving INT,
    gk_handling INT,
    gk_kicking INT,
    gk_positioning INT,
    gk_reflexes INT,
    FOREIGN KEY (player_fifa_api_id)
        REFERENCES Player(player_fifa_api_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (player_api_id)
        REFERENCES Player(player_api_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
```
#### Query : Table 5
```
CREATE TABLE Team (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    team_api_id INT UNIQUE,
    team_fifa_api_id INT,
    team_long_name VARCHAR(100),
    team_short_name VARCHAR(20)
);
```
#### Query : Table 6
```
CREATE TABLE Team_Attributes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    team_fifa_api_id INT,
    team_api_id INT,
    date DATE,
    buildUpPlaySpeed INT,
    buildUpPlaySpeedClass VARCHAR(50),
    buildUpPlayDribbling INT,
    buildUpPlayDribblingClass VARCHAR(50),
    buildUpPlayPassing INT,
    buildUpPlayPassingClass VARCHAR(50),
    buildUpPlayPositioningClass VARCHAR(50),
    chanceCreationPassing INT,
    chanceCreationPassingClass VARCHAR(50),
    chanceCreationCrossing INT,
    chanceCreationCrossingClass VARCHAR(50),
    chanceCreationShooting INT,
    chanceCreationShootingClass VARCHAR(50),
    chanceCreationPositioningClass VARCHAR(50),
    defencePressure INT,
    defencePressureClass VARCHAR(50),
    defenceAggression INT,
    defenceAggressionClass VARCHAR(50),
    defenceTeamWidth INT,
    defenceTeamWidthClass VARCHAR(50),
    defenceDefenderLineClass VARCHAR(50),
    FOREIGN KEY (team_fifa_api_id)
        REFERENCES Team(team_fifa_api_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (team_api_id)
        REFERENCES Team(team_api_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
```
#### Query : Table 7
```
CREATE TABLE Match (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    country_id INT,
    league_id INT,
    season VARCHAR(20),
    stage INT,
    date DATE,
    match_api_id INT UNIQUE,
    home_team_api_id INT,
    away_team_api_id INT,
    home_team_goal INT,
    away_team_goal INT,
    -- player coordinate data
    home_player_X1 INT, home_player_X2 INT, home_player_X3 INT, home_player_X4 INT, home_player_X5 INT,
    home_player_X6 INT, home_player_X7 INT, home_player_X8 INT, home_player_X9 INT, home_player_X10 INT, home_player_X11 INT,
    away_player_X1 INT, away_player_X2 INT, away_player_X3 INT, away_player_X4 INT, away_player_X5 INT,
    away_player_X6 INT, away_player_X7 INT, away_player_X8 INT, away_player_X9 INT, away_player_X10 INT, away_player_X11 INT,
    home_player_Y1 INT, home_player_Y2 INT, home_player_Y3 INT, home_player_Y4 INT, home_player_Y5 INT,
    home_player_Y6 INT, home_player_Y7 INT, home_player_Y8 INT, home_player_Y9 INT, home_player_Y10 INT, home_player_Y11 INT,
    away_player_Y1 INT, away_player_Y2 INT, away_player_Y3 INT, away_player_Y4 INT, away_player_Y5 INT,
    away_player_Y6 INT, away_player_Y7 INT, away_player_Y8 INT, away_player_Y9 INT, away_player_Y10 INT, away_player_Y11 INT,
    -- player ids
    home_player_1 INT, home_player_2 INT, home_player_3 INT, home_player_4 INT, home_player_5 INT,
    home_player_6 INT, home_player_7 INT, home_player_8 INT, home_player_9 INT, home_player_10 INT, home_player_11 INT,
    away_player_1 INT, away_player_2 INT, away_player_3 INT, away_player_4 INT, away_player_5 INT,
    away_player_6 INT, away_player_7 INT, away_player_8 INT, away_player_9 INT, away_player_10 INT, away_player_11 INT,
    goal TEXT, shoton TEXT, shotoff TEXT, foulcommit TEXT, card TEXT, `cross` TEXT, corner TEXT, possession TEXT,
    -- betting odds
    B365H DECIMAL(6,3), B365D DECIMAL(6,3), B365A DECIMAL(6,3),
    BWH DECIMAL(6,3), BWD DECIMAL(6,3), BWA DECIMAL(6,3),
    IWH DECIMAL(6,3), IWD DECIMAL(6,3), IWA DECIMAL(6,3),
    LBH DECIMAL(6,3), LBD DECIMAL(6,3), LBA DECIMAL(6,3),
    PSH DECIMAL(6,3), PSD DECIMAL(6,3), PSA DECIMAL(6,3),
    WHH DECIMAL(6,3), WHD DECIMAL(6,3), WHA DECIMAL(6,3),
    SJH DECIMAL(6,3), SJD DECIMAL(6,3), SJA DECIMAL(6,3),
    VCH DECIMAL(6,3), VCD DECIMAL(6,3), VCA DECIMAL(6,3),
    GBH DECIMAL(6,3), GBD DECIMAL(6,3), GBA DECIMAL(6,3),
    BSH DECIMAL(6,3), BSD DECIMAL(6,3), BSA DECIMAL(6,3),
    FOREIGN KEY (country_id) REFERENCES Country(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (league_id) REFERENCES League(id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (home_team_api_id) REFERENCES Team(team_api_id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (away_team_api_id) REFERENCES Team(team_api_id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (home_player_1) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_2) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_3) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_4) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_5) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_6) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_7) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_8) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_9) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_10) REFERENCES Player(player_api_id),
    FOREIGN KEY (home_player_11) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_1) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_2) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_3) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_4) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_5) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_6) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_7) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_8) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_9) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_10) REFERENCES Player(player_api_id),
    FOREIGN KEY (away_player_11) REFERENCES Player(player_api_id)
);
```
