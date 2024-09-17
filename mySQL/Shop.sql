-- create database ShopDB;
use ShopDB;

create table product(
	pCode varchar(10),
    pName varchar(20),
    price int,
    amount int
);

insert into product (pCode, pName, price, amount) 
values ('p0001', '노트북', 1000000, 3);
insert into product (pCode, pName, price, amount) 
values ('p0002', '마우스', 10000, 20);
insert into product (pCode, pName, price, amount) 
values ('p0003', '키보드', 30000, 15);
insert into product (pCode, pName, price, amount) 
values ('p0004', '모니터', 500000, 10);

select * from product;