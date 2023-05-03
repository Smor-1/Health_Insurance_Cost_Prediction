-- JOIN STATEMENT
CREATE TABLE full_ AS
SELECT info.ID, age, sex, bmi, children, region, charges
FROM info
INNER JOIN charges
ON info.ID = charges.ID;

DROP TABLE full_info;

SELECT * FROM info;

SELECT * FROM charges;

SELECT * FROM full;