-- In the dvdrental database write a query to select all the columns from the “customer” table.
SELECT customer_id, store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active
FROM public.customer;

-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT first_name||' '||last_name as full_name
FROM public.customer;

-- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
SELECT distinct create_date
FROM customer;

-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
SELECT customer_id, store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active
FROM customer
order by first_name DESC;

-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
SELECT address, postal_code, phone
FROM address
where district = 'Texas'

-- Write a query to retrieve all movie details where the movie id is either 15 or 150.
select * from film
where film_id in (15,150)

-- Write a query which should check if your favorite movie exists in the database. 
--Have your query get the film ID, title, description, length and the rental rate, these 
--details can be found in the “film” table.
select film_ID, title, description, length, rental_rate from film
where lower(title) = lower('Gone with the wind')

-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
select film_ID, title, description, length, rental_rate from film
where lower(title) like 'go%'

-- Write a query which will find the 10 cheapest movies.
select * from film 
order by rental_rate,film_id ASC limit 10

-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.
SELECT *
FROM (
    SELECT f.*,
           ROW_NUMBER() OVER (ORDER BY rental_rate asc) AS rn
    FROM film f
) t
WHERE rn BETWEEN 11 AND 20;


-- Write a query which will join the data in the customer table and the payment table. 
--You want to get the first name and last name from the curstomer table, as well as 
--the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
select c.customer_id, first_name, last_name, amount, payment_date 
from customer c
inner join payment p on c.customer_id=p.customer_id
order by c.customer_id

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.
select * from film f
where not exists
 (select 1 from inventory i
 	where f.film_id=i.film_id)

select * from film f
left outer join inventory i on f.film_id=i.film_id
where i.film_id is null

-- Write a query to find which city is in which country.
select city, country from city c
inner join country s on s.country_id = c.country_id

-- Bonus You want to be able to see how your sellers have been doing? Write a query to get
--the customer’s id, names (first and last), the amount and the date of payment ordered by
--the id of the staff member who sold them the dvd.
select c.customer_id, first_name||' '||last_name as full_name,amount,payment_date
from customer c, payment p
where c.customer_id=p.customer_id
order by p.staff_id
