CREATE TABLE Stock (
StockID INTEGER AUTO_INCREMENT,
StockName VARCHAR(20),
StockType VARCHAR(20),
CompName VARCHAR(20) NOT NULL,
SharePrice FLOAT(2) NOT NULL,
NO_OF_AVAIL_SHARES INTEGER NOT NULL,
PRIMARY KEY (StockID),
UNIQUE (StockName,CompName)
);



CREATE TABLE Trader (
UserId INTEGER AUTO_INCREMENT,
FirstName VARCHAR(20) NOT NULL,
LastName VARCHAR(20),
PhoneNO VARCHAR(10) NOT NULL,
EmailID VARCHAR(40) NOT NULL,
Passwd VARCHAR(20) NOT NULL,
City VARCHAR(20),
State VARCHAR(20),
PRIMARY KEY (UserId),
UNIQUE (EmailID,PhoneNO)
);


CREATE TABLE Login (
EmailID VARCHAR(20) NOT NULL,
Passwd VARCHAR(20) NOT NULL,
UserId INTEGER,
Timestamp_		DATETIME DEFAULT NOW() NOT NULL,
PRIMARY KEY (EmailID),
FOREIGN KEY (UserId) REFERENCES Trader(UserId)
);

CREATE TABLE Trades (
	TradeId			INTEGER AUTO_INCREMENT,
	StockID      	INTEGER,
	TradeType		VARCHAR(4) NOT NULL,
	NumOfShares		INTEGER NOT NULL,
    UserPrice       float(2) NOT NULL,
    SharePrice      float(2) NOT NULL,
-- 	CusAccNum		INTEGER DEFAULT 0,
	Timestamp_		DATETIME DEFAULT NOW() NOT NULL,
	UserId			INTEGER,
	PRIMARY KEY (TradeId),
	UNIQUE (StockID, Timestamp_, UserId),
	FOREIGN KEY (StockID) REFERENCES Stock (StockID)
		ON DELETE SET NULL
		ON UPDATE CASCADE,
-- 	FOREIGN KEY (CusAccNum) REFERENCES Account_ (AccNum)
-- 		ON DELETE SET NULL	
-- 		ON UPDATE CASCADE,
	FOREIGN KEY (UserId) REFERENCES Trader (UserId)
		ON DELETE SET NULL
		ON UPDATE CASCADE
);



CREATE TABLE Account_ (
	AccNum			INTEGER  UNIQUE,
	AccHolderName		VARCHAR(30),
	IFSC_Code		VARCHAR(16),
	AccBalance			INTEGER ,
    UserId 			INTEGER AUTO_INCREMENT,
	PRIMARY KEY (UserId),
	FOREIGN KEY (UserId) REFERENCES Trader(UserId)
);
 
 

CREATE TABLE Portfolio (
	UserId INTEGER,
    StockID      INTEGER,
    CompName   VARCHAR(20) ,
    MyShares 	INTEGER DEFAULT 0,
	PRIMARY KEY (UserId, StockID),
	FOREIGN KEY (StockID) REFERENCES Stock(StockID),
    FOREIGN KEY (UserId) REFERENCES Trader(UserId)
    

);

-- drop table Portfolio;

-- drop table Trades;
-- drop table Stock;
-- drop table Account_;
-- drop table Trader;
-- drop table Login;


-- show tables;
