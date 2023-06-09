-- Info table creation, holds individual info
CREATE TABLE info (
    ID VARCHAR(10) PRIMARY KEY,
    age INTEGER NOT NULL,
    sex VARCHAR(10) NOT NULL,
    bmi FLOAT NOT NULL,
    children INTEGER NOT NULL,
    smoker VARCHAR(3) NOT NULL
);

CREATE TABLE charges (
    ID VARCHAR(10) PRIMARY KEY,
    region VARCHAR(20) NOT NULL,
    charges FLOAT NOT NULL
);