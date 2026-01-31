-- You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
-- Find out how many films there are for each rating.
select rating, count(*)
from film
group by rating

-- Get a list of all the movies that have a rating of G or PG-13.
select * from film where rating in ('G','PG-13')

-- Filter this list further: look for only movies that are under 2 hours long, and 
--whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
select * from film 
where rating in ('G','PG-13') and length<=120 and rental_rate<=3
order by title

-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
update customer 
set last_name='Svyatlov', email='email@gmail.com'
where first_name='Victoria'

-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
update address 
set address='My address'
where address_id = (select address_id from customer where first_name='Victoria')
	