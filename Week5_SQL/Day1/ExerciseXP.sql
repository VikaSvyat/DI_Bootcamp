create table items as 
(select 1 as id, 'Small Desk' as item_name, 100 as price
union select 2, 'Large desk',  300  
union select 3, 'Fan', 80 )

create table customers as
(select 1 as id, 'Greg' as cname, 'Jones' as surname
union all select 2, 'Sandra' ,'Jones'
union all select 3, 'Scott' ,'Scott'
union all select 4, 'Trevor' ,'Green'
union all select 5, 'Melanie' ,'Johnson')

select id, item_name, to_char(price, '999G999D99') from items
union all
select id,cname,surname from customers

select * from items
where price > 80

select * from items
where price <=300

select id,cname,surname from customers
where surname = 'Smith'

select id,cname,surname from customers
where surname = 'Jones'

select id,cname,surname from customers
where surname != 'Scott'