### Database : codebase_community
#### Query : Database 
```
CREATE DATABASE IF NOT EXISTS codebase_community;
USE codebase_community;
```
#### Query : Table 1
```
CREATE TABLE users (
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Reputation INT NULL,
    CreationDate DATETIME NULL,
    DisplayName VARCHAR(255) NULL,
    LastAccessDate DATETIME NULL,
    WebsiteUrl TEXT NULL,
    Location TEXT NULL,
    AboutMe TEXT NULL,
    Views INT NULL,
    UpVotes INT NULL,
    DownVotes INT NULL,
    AccountId INT NULL,
    Age INT NULL,
    ProfileImageUrl TEXT NULL
);
```
#### Query : Table 2
```
CREATE TABLE posts (
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PostTypeId INT NULL,
    AcceptedAnswerId INT NULL,
    CreationDate DATETIME NULL,
    Score INT NULL,
    ViewCount INT NULL,
    Body TEXT NULL,
    OwnerUserId INT NULL,
    LastActivityDate DATETIME NULL,
    Title TEXT NULL,
    Tags TEXT NULL,
    AnswerCount INT NULL,
    CommentCount INT NULL,
    FavoriteCount INT NULL,
    LastEditorUserId INT NULL,
    LastEditDate DATETIME NULL,
    CommunityOwnedDate DATETIME NULL,
    ParentId INT NULL,
    ClosedDate DATETIME NULL,
    OwnerDisplayName VARCHAR(255) NULL,
    LastEditorDisplayName VARCHAR(255) NULL,
    FOREIGN KEY (LastEditorUserId) REFERENCES users(Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (OwnerUserId) REFERENCES users(Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ParentId) REFERENCES posts(Id) ON UPDATE CASCADE ON DELETE CASCADE
);
```
#### Query : Table 3
```
CREATE TABLE comments (
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PostId INT NULL,
    Score INT NULL,
    Text TEXT NULL,
    CreationDate DATETIME NULL,
    UserId INT NULL,
    UserDisplayName VARCHAR(255) NULL,
    FOREIGN KEY (PostId) REFERENCES posts(Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (UserId) REFERENCES users(Id) ON UPDATE CASCADE ON DELETE CASCADE
);
```
#### Query : Table 4 
```
CREATE TABLE postHistory (
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PostHistoryTypeId INT NULL,
    PostId INT NULL,
    RevisionGUID VARCHAR(255) NULL,
    CreationDate DATETIME NULL,
    UserId INT NULL,
    Text TEXT NULL,
    Comment TEXT NULL,
    UserDisplayName VARCHAR(255) NULL,
    FOREIGN KEY (PostId) REFERENCES posts(Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (UserId) REFERENCES users(Id) ON UPDATE CASCADE ON DELETE CASCADE
);
```
#### Query : Table 5
```
CREATE TABLE postLinks (
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CreationDate DATETIME NULL,
    PostId INT NULL,
    RelatedPostId INT NULL,
    LinkTypeId INT NULL,
    FOREIGN KEY (PostId) REFERENCES posts(Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (RelatedPostId) REFERENCES posts(Id) ON UPDATE CASCADE ON DELETE CASCADE
);
```
#### Query : Table 6
```
CREATE TABLE tags (
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    TagName VARCHAR(255) NULL,
    Count INT NULL,
    ExcerptPostId INT NULL,
    WikiPostId INT NULL,
    FOREIGN KEY (ExcerptPostId) REFERENCES posts(Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (WikiPostId) REFERENCES posts(Id) ON UPDATE CASCADE ON DELETE CASCADE
);
```
#### Query : Table 7
```
CREATE TABLE badges (
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    UserId INT NULL,
    Name VARCHAR(255) NULL,
    Date DATETIME NULL,
    FOREIGN KEY (UserId) REFERENCES users(Id) ON UPDATE CASCADE ON DELETE CASCADE
);
```
#### Query : Table 8 
```
CREATE TABLE votes (
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PostId INT NULL,
    VoteTypeId INT NULL,
    CreationDate DATETIME NULL,
    UserId INT NULL,
    BountyAmount INT NULL,
    FOREIGN KEY (PostId) REFERENCES posts(Id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (UserId) REFERENCES users(Id) ON UPDATE CASCADE ON DELETE CASCADE
);
```
