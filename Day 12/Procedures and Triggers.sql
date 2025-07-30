use havingclause_practice;

-- Write a stored procedure that takes a customer ID as input and returns the customer's name from the Customers table.
create procedure customer_names(id INT)
	select name from customers
    where customer_id = id;
    
call customer_names(1);

-- Triggers
delimiter $$
create trigger quantity_check
before
insert
on order_items
for each row
begin
	if new.quantity<0 then set new.quantity=0;
	end if;
end;

# Checking the created Trigger

insert into order_items(order_item_id,order_id,product_id,quantity)
values(110,105,1008,-9);

select * from order_items