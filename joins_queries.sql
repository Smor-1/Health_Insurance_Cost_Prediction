-- JOIN STATEMENT
-- CREATE TABLE full_data AS
SELECT i.ID, i.age, i.sex, i.bmi, i.children, i.smoker, c.region, c.charges
INTO full_data
FROM info as i 
INNER JOIN charges as c 
ON (i.ID = c.ID);

DROP TABLE full_data;

SELECT * FROM info;

SELECT * FROM charges;

SELECT * FROM full_data;