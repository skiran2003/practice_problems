create database flights_data;

use flights_data;

-- Loading data from csv to mysql
 create table if not exists flights(
 id INT primary key,
 airline varchar(30),
 flight varchar(20),
 source_city varchar(30),
 departure_time varchar(30),
 stops varchar(20),
 arrival_time varchar(30),
 destination_city varchar(30),
 class varchar(20),
 duration float,
 days_left int,
 price int);
 
 -- Fetching first 10 rows from data
 select * from flights
 limit 10;
 
 -- Counting the number of records imported from dataset (71534 records)
 select count(*) from flights; 
 
--  Fetching top 5 cheapest flights
select * from flights
order by price
limit 5;

/* Normalization of the table
The table does not have multivalued records hence it is already in 1NF
Normalizing the table to 2NF and 3NF
*/
-- ---------------------------------------------------------------------
drop table airlines;

create table if not exists airlines(
airline_id int auto_increment primary key,
airline varchar(30));

insert into airlines(airline)
select distinct airline from flights;

select * from airlines;
-- ---------------------------------------------------------------------
create table if not exists flight_numbers(
flight_id varchar(20) primary key,
airline_id int,
FOREIGN KEY (airline_id) references airlines(airline_id));

insert into flight_numbers(airline_id,flight_id)
select distinct a.airline_id,f.flight from flights f
join airlines a on a.airline=f.airline;

select * from flight_numbers;

-- ---------------------------------------------------------------------
create table flight_class(
class_id int auto_increment primary key,
class varchar(20));

insert ignore into flight_class(class)
select distinct class from flights;

select * from flight_class;

-- ---------------------------------------------------------------------
create table if not exists time_slots(
slot_id int auto_increment primary key,
time_slot varchar(20));

insert into time_slots(time_slot)
select distinct departure_time from flights
union
select distinct arrival_time from flights;

select * from time_slots;
-- ----------------------------------------------------------------------
create table if not exists cities(
city_id int auto_increment primary key,
city_name varchar(30));

insert into cities(city_name)
select distinct source_city from flights
union
select distinct destination_city from flights;

select * from cities;
-- ------------------------------------------------------------------------
-- Creating a table to insert normalized data

create table flights_info(
id int auto_increment primary key,
airline_id int,
flight_id varchar(20),
source_cityid int,
destination_cityid int,
stops int,
departure_timeslot int,
arrival_timeslot int,
class_id int,
duration float,
days_left int,
price int,
foreign key (airline_id) references airlines(airline_id),
foreign key (flight_id) references flight_numbers(flight_id),
foreign key (source_cityid) references cities(city_id),
foreign key (destination_cityid) references cities(city_id),
foreign key (departure_timeslot) references time_slots(slot_id),
foreign key (arrival_timeslot) references time_slots(slot_id),
foreign key (class_id) references flight_class(class_id)
);

alter table flights_info
modify column stops varchar(20);

-- Inserting normalized data into the new table
insert into flights_info(airline_id,flight_id,source_cityid,destination_cityid,stops,departure_timeslot,arrival_timeslot,class_id,duration,days_left,price)
select 
a.airline_id,
fn.flight_id,
sc.city_id,
dc.city_id,
f.stops,
dt.slot_id,
art.slot_id,
cl.class_id,
f.duration,
f.days_left,
f.price
from flights f
join airlines a on a.airline=f.airline
join flight_numbers fn on fn.flight_id=f.flight
join cities sc on sc.city_name=f.source_city
join cities dc on dc.city_name=f.destination_city
join time_slots dt on dt.time_slot=f.departure_time
join time_slots art on art.time_slot=f.arrival_time
join flight_class cl on cl.class=f.class;

-- Checking the inserted records 
select * from flights_info
where stops='zero'
limit 10;

-- Creating a procedure to find shortest journey between two cities
drop procedure if exists fastest_flights;
delimiter &&
create procedure fastest_flights(source varchar(20),destination varchar(20))
begin
select sc.city_name as source_city,
dc.city_name as destination_city,
min(fi.duration) as shortest_time_journey
from flights_info fi
join cities sc on fi.source_cityid=sc.city_id
join cities dc on fi.destination_cityid=dc.city_id
where sc.city_name=source and dc.city_name=destination
group by sc.city_name,dc.city_name;
end &&
delimiter ;

call fastest_flights('Delhi','Hyderabad');

-- Finding the cheapest flights of each airline
select a.airline,fn.flight_id, fi.price, sc.city_name as Source, dc.city_name as Destination
from flights_info fi
join airlines a on fi.airline_id=a.airline_id
join cities sc on sc.city_id=fi.source_cityid
join cities dc on dc.city_id=fi.destination_cityid
join flight_numbers fn on fn.airline_id=a.airline_id
join
(select airline_id,min(price) as min_price from flights_info
group by airline_id) as cheapest on fi.airline_id=cheapest.airline_id and fi.price=cheapest.min_price;

-- Creating a procedure to select flights with price less than given amount
create procedure sorting_prices(p_price int)
select a.airline,fi.flight_id,fi.price from flights_info fi
join airlines a on a.airline_id=fi.airline_id
where price < p_price;

call sorting_prices(5000);