-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
select * from items order by price ASC

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
select * from items where price >= 80 order by price DESC

-- The first 3 customers in alphabetical order of the first name (A-Z) – 
-- exclude the primary key column from the results.
select cname,surname from customers order by cname ASC LIMIT 3

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
select surname from customers order by surname DESC 


