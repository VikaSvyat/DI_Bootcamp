select count(distinct first_name||last_name) from actors

SELECT pg_get_serial_sequence('actors', 'actor_id');

SELECT last_value FROM actors_actor_id_seq;

insert into actors 
values ( nextval('actors_actor_id_seq'),'Audrey','Hepburn','04-05-1929',1)

insert into actors (first_name,last_name,age,number_oscars)
values ( 'Audrey','Hepburn','04-05-1929',1)

select * from actors

