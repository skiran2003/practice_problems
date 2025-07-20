USE sample;
SELECT * FROM cricketers;
-- ALTER TABLE cricketers ADD UNIQUE(playername); -- Defining Primary Key after creating a table
DESCRIBE cricketers;  -- Describes about the fields in a table
SELECT DISTINCT team FROM cricketers; -- Fetches distinct values from a table without duplicates
SELECT * FROM cricketers ORDER BY role; -- Sorts the elements in order
SELECT * FROM cricketers ORDER BY team,role; -- Sorts the elements of 'team' column first and then sorts the elements of 'role' column
SELECT * FROM cricketers ORDER BY team DESC; -- Sorts the Column team in reverse alphabetic order(descending order) 
SELECT * FROM cricketers WHERE team='India' AND role LIKE 'b%'; -- Fetches all the elements of the table with team name 'India' and role name starting with b
SELECT * FROM cricketers WHERE role='batter' OR role='bowler'; -- Filters the values when either of the conditions are True
SELECT * FROM cricketers WHERE NOT team='Sri Lanka'; -- Filters values when condition is not True
UPDATE cricketers SET role='Wk,Batter' WHERE playername='Dhoni';
UPDATE cricketers SET role='Wk,Batter' WHERE playername='Sangakkara';
UPDATE cricketers SET role='Wk,Batter' WHERE playername='A B Devilliers';
