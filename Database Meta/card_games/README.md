### Database : card_games 

#### Query : Database 
```
CREATE DATABASE IF NOT EXISTS card_games;
USE card_games;
```

#### Query : Table 1(sets)
```
CREATE TABLE IF NOT EXISTS sets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    baseSetSize INT,
    block VARCHAR(100),
    booster TEXT,
    code VARCHAR(50) NOT NULL UNIQUE,
    isFoilOnly TINYINT(1) DEFAULT 0 NOT NULL,
    isForeignOnly TINYINT(1) DEFAULT 0 NOT NULL,
    isNonFoilOnly TINYINT(1) DEFAULT 0 NOT NULL,
    isOnlineOnly TINYINT(1) DEFAULT 0 NOT NULL,
    isPartialPreview TINYINT(1) DEFAULT 0 NOT NULL,
    keyruneCode VARCHAR(50),
    mcmId INT,
    mcmIdExtras INT,
    mcmName VARCHAR(100),
    mtgoCode VARCHAR(50),
    name VARCHAR(150),
    parentCode VARCHAR(50),
    releaseDate DATE,
    tcgplayerGroupId INT,
    totalSetSize INT,
    type VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
#### Query : Table 2(cards)
```
CREATE TABLE IF NOT EXISTS cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    artist TEXT,
    asciiName TEXT,
    availability TEXT,
    borderColor TEXT,
    cardKingdomFoilId TEXT,
    cardKingdomId TEXT,
    colorIdentity TEXT,
    colorIndicator TEXT,
    colors TEXT,
    convertedManaCost DECIMAL(10,2),
    duelDeck TEXT,
    edhrecRank INT,
    faceConvertedManaCost DECIMAL(10,2),
    faceName TEXT,
    flavorName TEXT,
    flavorText TEXT,
    frameEffects TEXT,
    frameVersion TEXT,
    hand TEXT,
    hasAlternativeDeckLimit TINYINT(1) DEFAULT 0 NOT NULL,
    hasContentWarning TINYINT(1) DEFAULT 0 NOT NULL,
    hasFoil TINYINT(1) DEFAULT 0 NOT NULL,
    hasNonFoil TINYINT(1) DEFAULT 0 NOT NULL,
    isAlternative TINYINT(1) DEFAULT 0 NOT NULL,
    isFullArt TINYINT(1) DEFAULT 0 NOT NULL,
    isOnlineOnly TINYINT(1) DEFAULT 0 NOT NULL,
    isOversized TINYINT(1) DEFAULT 0 NOT NULL,
    isPromo TINYINT(1) DEFAULT 0 NOT NULL,
    isReprint TINYINT(1) DEFAULT 0 NOT NULL,
    isReserved TINYINT(1) DEFAULT 0 NOT NULL,
    isStarter TINYINT(1) DEFAULT 0 NOT NULL,
    isStorySpotlight TINYINT(1) DEFAULT 0 NOT NULL,
    isTextless TINYINT(1) DEFAULT 0 NOT NULL,
    isTimeshifted TINYINT(1) DEFAULT 0 NOT NULL,
    keywords TEXT,
    layout TEXT,
    leadershipSkills TEXT,
    life TEXT,
    loyalty TEXT,
    manaCost TEXT,
    mcmId TEXT,
    mcmMetaId TEXT,
    mtgArenaId TEXT,
    mtgjsonV4Id TEXT,
    mtgoFoilId TEXT,
    mtgoId TEXT,
    multiverseId TEXT,
    name TEXT,
    number TEXT,
    originalReleaseDate DATE,
    originalText TEXT,
    originalType TEXT,
    otherFaceIds TEXT,
    power TEXT,
    printings TEXT,
    promoTypes TEXT,
    purchaseUrls TEXT,
    rarity TEXT,
    scryfallId TEXT,
    scryfallIllustrationId TEXT,
    scryfallOracleId TEXT,
    setCode VARCHAR(50),
    side TEXT,
    subtypes TEXT,
    supertypes TEXT,
    tcgplayerProductId TEXT,
    text TEXT,
    toughness TEXT,
    type TEXT,
    types TEXT,
    uuid VARCHAR(100) NOT NULL UNIQUE,
    variations TEXT,
    watermark TEXT,
    FOREIGN KEY (setCode) REFERENCES sets(code)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
#### Query : Table 3(foreign_data)
```
CREATE TABLE IF NOT EXISTS foreign_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flavorText TEXT,
    language VARCHAR(50),
    multiverseid INT,
    name TEXT,
    text TEXT,
    type TEXT,
    uuid VARCHAR(100),
    FOREIGN KEY (uuid) REFERENCES cards(uuid)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
#### Query : Table 4(legalities)
```
CREATE TABLE IF NOT EXISTS legalities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    format VARCHAR(100),
    status VARCHAR(50),
    uuid VARCHAR(100),
    FOREIGN KEY (uuid) REFERENCES cards(uuid)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
#### Query : Table 5(rulings)
```
CREATE TABLE IF NOT EXISTS rulings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    text TEXT,
    uuid VARCHAR(100),
    FOREIGN KEY (uuid) REFERENCES cards(uuid)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
#### Query : Table 6(set_translations)
```
CREATE TABLE IF NOT EXISTS set_translations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    language VARCHAR(50),
    setCode VARCHAR(50),
    translation TEXT,
    FOREIGN KEY (setCode) REFERENCES sets(code)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
