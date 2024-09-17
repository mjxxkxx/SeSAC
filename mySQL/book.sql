-- create database BookDB;
use BookDB;
/* create table Testtable(
	col_1 int,
-- -- col_2 varchar(20),
-- -- col_3 datetime
);-*/
-- drop table Testtable;

/* create table Book(
	bookid int,
-- -- bookname varchar(20),
-- -- publisher varchar(20),
-- -- price int
);

insert into Book(bookid, bookname, publisher, price)
values(100, '데이터베이스', '한빛아카데미', 27000);
insert into Book(bookid, bookname, publisher, price)
values(101, '파이썬', '한빛아카데미', 22000);
insert into Book(bookid, bookname, publisher, price)
values(102, 'JSP 프로그래밍', '생능출판사', 26000);
insert into Book(bookid, bookname, publisher, price)
values(103, '자바스크립트', '길벗', 45000);
insert into Book(bookid, bookname, publisher, price)
values(104, '데이터베이스 배움터', '생능출판사', 30000);
insert into Book(bookid, bookname, publisher, price)
values(105, 'HTML 기초', '한빛아카데미', 37000);
insert into Book(bookid, bookname, publisher, price)
values(106, '파이썬 데이터분석', '이지스퍼블리싱', 25000);
insert into Book(bookid, bookname, publisher, price)
values(107, 'Chat GPT', '생능출판사', 29000);
insert into Book(bookid, bookname, publisher, price)
values(108, 'ReactJS', '이지스퍼블리싱', 41000);
insert into Book(bookid, bookname, publisher, price)
values(109, '홈페이지 만들기 기초', '한빛아카데미', 32000);
insert into Book(bookid, bookname, publisher, price)
values(110, '데이터 시각화', '생능출판사', 27000);*/

-- 'Book' 테이블에 저장된 전체 데이터 조회
select * from Book;

-- 'Book' 테이블에 저장된 bookname만 조회
select bookname from book;

select publisher from book;

-- 'Book' 테이블에 저장된 bookname만 조회
select bookname, publisher from book;

-- 'Book' 테이블에 저장된 publisher만 조회
select publisher from book;

-- 'Book' 테이블에 저장된 bookname, publisher를 조회
select bookname, publisher from book;

select publisher, bookname from book;

-- 가격이 25,000원 이상인 책 정보 검색
select * from Book where price > 25000;

select * from Book where price >= 30000;

-- 가격이 10,000원 이상 25,000원 이하인 책 정보 검색
select * from Book where price between 10000 and 25000;

-- 출판사가 '길벗' 또는 '생능출판사'인 책 정보 검색
select * from Book where publisher in('길벗','생능출판사');

-- 출판사가 '길벗' 또는 '생능출판사'가 아닌 책 정보 검색
select * from Book where publisher not in('길벗', '생능출판사');

-- '데이터베이스'를 출간한 출판사 검색
select publisher from book where bookname like '데이터베이스';

-- 책 이름에 '데이터베이스'가 포함된 책 이름과 출판사 검색
select bookname, publisher from book where bookname like '%데이터베이스%';

select bookname, publisher from book where bookname like '데이터베이스%';

select bookname, publisher from book where bookname like '%데이터베이스';

-- 왼쪽 두 번째 위치에 '이'라는 문자를 갖는 책 이름을 검색
select bookname from book where bookname like '_이%';

-- 출판사가 '길벗' 또는 '생능출판사'인 책 정보 검색
select * from book where publisher = '길벗' or publisher = '생능출판사';

-- 데이터 관련 도서 중, 가격이 30,000원 이상인 책 검색
select * from book where bookname like '%데이터%' and price >= 30000;

-- 2-1 제목이 '프로그래밍'으로 끝나는 책 정보 검색
select bookname, price from book where bookname like '%프로그래밍';

-- 2-2 제목이 '데이터'로 시작하면서 6자인 책 정보 검색
select * from book where bookname like '데이터___';

-- 2-3 제목의 세 번째 글자가 '터'인 책 정보 검색
select * from book where bookname like '%__터%';

-- 2-4 '한빛아카데미'의 도서 중 '데이터' 관련된 책 정보 검색
select * from book where bookname like '%데이터%' and publisher = '한빛아카데미';

-- 도서를 이름순으로 검색(오름차순)
select * from book order by bookname asc;

-- 도서를 이름순으로 검색(오름차순)
select * from book order by bookname;

-- 도서를 가격순으로 검색(오름차순)
select * from book order by price;

-- 도서를 이름순으로 검색(내림차순)
select * from book order by bookname desc;

-- 도서를 가격순으로 검색(내림차순)
select * from book order by price desc;

-- 전체 도서 가격의 합 출력
select sum(price) from book;

-- 전체 도서 가격의 합 출력 - 열 제목 추가
select sum(price) as '가격 총합' from book;

-- 전체 도서들의 평균 가격 출력
select avg(price) as '평균 가격' from book;

-- 도서의 총 개수 출력
select count(*) as '총 개수' from book;

select count(price) as '총 개수' from book;

-- 최저가 도서 계산
select min(price) as '최저가' from book;

-- 최고가 도서 계산
select max(price) as '최고가' from book;

-- 4-1 데이터베이스 관련 책 가격의 총액 계산
select sum(price) as '총액' from book 
where bookname like '%데이터베이스%';

-- 4-2 출판사가 '한빛아카데미'인 책의 개수 출력
select count(*) as '한빛아카데미' from book 
where publisher = '한빛아카데미';

-- 각 출판사별 도서 금액의 총합 계산
select publisher, sum(price) from book 
group by publisher;

-- 출판사를 기준으로 그룹화 후, '생능출판사'의 데이터만 검색하여 도서 금액의 총합 계산
select publisher, sum(price) from book 
group by publisher 
having publisher = '생능출판사';

-- 출판사를 기준으로 그룹화 후, 가격이 20,000원 이상인 도서만 검색하여 도서 금액의 총합 계산
select publisher, sum(price) from book 
where price >= 20000 
group by publisher;

-- 4-3 출판사 별로 가격이 30,000원 이상인 도서의 총 수량을 계산
select publisher, count(*) as '도서수량' from book 
where price >= 30000 
group by publisher;

-- 4-4 출판사 별로 가격이 30,000원 이상인 도서의 총 수량을 계산 총 수량이 두 권 이상인 출판사만 조회
select publisher, count(*) as '도서수량' from book 
where price >= 30000 
group by publisher
having count(*) >= 2;

-- 출판사 이름의 중복을 제거하여 검색
select distinct publisher from book;

-- 책의 가격을 23,000원으로 수정
update Book set price = 23000 where bookid = 101;

-- varchar(10) 자료형을 가진 isbn 속성 추가
alter table Book add isbn varchar(10);
select * from book;

-- Book 테이블의 isbn 속성의 데이터 타입을 INT로 변경
alter table book modify isbn int;

-- Book 테이블의 isbn 속성의 이름을 '일련번호'로 변경
alter table book change isbn 일련번호;

-- Book 테이블의 일련번호 속성을 삭제
alter table book drop column 일련번호;

-- 기본키(primary key)

-- newBook 테이블 생성하기 bookid를 기본키로 지정
create table newBook(
	bookid int primary key,
    bookname varchar(20),
    publisher varchar(20),
    price int
);

-- 데이터 삽입하기
/*insert into newBook(bookid, bookname, publisher, price)
values(100, '데이터베이스', '한빛아카데미', 27000);

-- primary 에러발생
insert into newBook(bookid, bookname, publisher, price)
values(100, '프로그래밍', '한빛아카데미', 30000); 기본키로 저장됐어서 중복으로 저장 못해!

-- 기본키는 null값을 가질 수 없다
insert into newBook(bookid, bookname, publisher, price)
values(null, '데이터 시각화', '생능출판사', 27000);*/

select * from newBook;

-- 실습 NOT NULL

-- 테이블 속성 변경하기 : bookname과 publisher에 null을 들어가지 못하도록 하는 함수!

-- alter 함수는 계속적으로 저장되는 함수임

alter table newBook modify bookname varchar(20) NOT NULL;

alter table newBook modify publisher varchar(20) NOT NULL;

alter table newBook modify publisher varchar(20) NULL;
-- 이후 이전에 실행가능했던 아래의 쿼리를 실행할 수 없음 : 
-- 설정하기전 디폴트 값은 null 허용
/*
insert into newBook(bookid, bookname, publisher, price) 
values(101, null, null, 25000);
-- 위의 bookname, publisher에 null이 들어가있는 이유 : 
-- bookid는 primary key를 지정해줬지만, name과 publisher는 키를 입력하지 않았기때문에 null이 들어갈 수 있음 

insert into newBook(bookid, bookname, publisher, price) 
values(102, '데이터시각화', '생능출판사', 25000);
*/

select * from newBook;

-- 테이블 속성 변경하기 : price 속성의 기본값을 10,000원으로 지정
alter table newBook modify price INT default 10000;

-- 기본 값 확인
/*
insert into newBook(bookid, bookname, publisher) 
values (103, '프로그래밍','한빛아카데미');
select * from newBook;

-- default 10000을 지정하지 않았을 때의 기본 값은 default null
insert into newBook(bookid, bookname, publisher,price) 
values (104, '프로그래밍','한빛아카테미',null);
select * from newBook;
*/

-- 기존 데이터 모두 제거 후 입력

delete from newBook;

-- 아래의 항목 추가해 두기 : ppt 2.SQL 111p
/*
insert into newBook (bookid, bookname, publisher, price) 
values (100, '데이터베이스', '한빛아카데미', 27000);
insert into newBook (bookid, bookname, publisher, price) 
values (101, '파이썬', '한빛아카데미', 22000);
insert into newBook (bookid, bookname, publisher, price) 
values (102, 'JSP 프로그래밍', '생능출판사', 26000);
insert into newBook (bookid, bookname, publisher, price) 
values (103, '자바스크립트', '길벗', 45000);
insert into newBook (bookid, bookname, publisher, price) 
values (104, '데이터베이스배움터', '생능출판사', 30000);
insert into newBook (bookid, bookname, publisher, price) 
values (105, 'HTML 기초', '한빛아카데미', 37000);
insert into newBook (bookid, bookname, publisher, price) 
values (106, '파이썬데이터', '이지스퍼블리싱', 25000);
insert into newBook (bookid, bookname, publisher, price) 
values (107, 'Chat GPT', '생능출판사', 29000);
insert into newBook (bookid, bookname, publisher, price) 
values (108, 'ReactJS', '이지스퍼블리싱', 41000);
insert into newBook (bookid, bookname, publisher, price) 
values (109, '홈페이지만들기', '한빛아카데미', 32000);
insert into newBook (bookid, bookname, publisher, price) 
values (110, '데이터시각화', '생능출판사', 27000);
*/

-- 외래키 (Foreign Key) : 다른 릴레이션(테이블)의 기본키를 참조하는 속성 - 연결고리를 만들어 놓는 것
-- create table 테이블 이름(
--         속성이름1 데이터타입 primary key,
--         속성이름2 데이터타입,
--         속성이름3 데이터타입,
--         foreign key(속성이름2) references 참초할테이블이름(속성이름)
-- );

-- newOrders 테이블 생성 /ppt 2.SQL 114p
/*
create table newOrders(
	orderid varchar(10)    primary key,
	bookid int NOT NULL,
	member varchar(10) NOT NULL,
	address varchar(20) NOT NULL,
	foreign key(bookid) references newBook(bookid)
);

select * from newOrders;

-- newOrders 테이블에 데이터 입력 
insert into newOrders(orderid, bookid, member, address) 
values('p001',102,'정수아','서울');

-- newOrders 테이블에 2번째 데이터 입력 
-- 오류의 이유 : bookid(여기서 120)가 참조테이블에 존재하지 않음
insert into newOrders(orderid, bookid, member, address) 
values('p002',120,'정수아','서울');

-- newBook(참조테이블)의 데이터 삭제하기
delete from newBook where bookid=102; */

/* 참조 테이블의 데이터까지 한번에 삭제하고 싶다면 외래키를 지정할때, on delete cascade옵션을 추가하면 됨
foreign key(속성이름) references 참조할테이블 이름(속성이름)on delete cascade
*/

/*
-- newOrders 삭제 후 다시 입력 --
delete from newOrders;

insert into newOrders(orderid, bookid, member, address) 
values ('p001', 102, '오한솔', '경기');
insert into newOrders(orderid, bookid, member, address) 
values ('p002', 107, '김현우', '서울');
insert into newOrders(orderid, bookid, member, address) 
values ('p003', 103, '박홍진', '부산');
insert into newOrders(orderid, bookid, member, address) 
values ('p004', 102, '김현우', '서울');
insert into newOrders(orderid, bookid, member, address) 
values ('p005', 104, '문종헌', '대전');
insert into newOrders(orderid, bookid, member, address) 
values ('p006', 105, '김현우', '서울');
insert into newOrders(orderid, bookid, member, address) 
values ('p007', 103, '이봉림', '부산');
insert into newOrders(orderid, bookid, member, address) 
values ('p008', 102, '정희성', '경기');
insert into newOrders(orderid, bookid, member, address) 
values ('p009', 107, '오한솔', '경기');
insert into newOrders(orderid, bookid, member, address) 
values ('p010', 103, '김현우', '서울');
*/
 /*
두 테이블 연결하여 ordertable에서 책에 대한 정보 검색 : 조인 

조인 : SELECT 테이블이름.열이름 FROM 참조할 테이블이름1, 테이블이름2 
WHERE 조건 AND 테이블1.b = 테이블2.b(테이블1과 테이블2의 어떠한 열은 같다!)
3개 이상의 테이블 사용도 가능, 테이블이름.열이름에서 테이블이름은 필수가 아니긴하지만 이해 및 가독성을 위해 작성해줌
(두 테이블의 열이름이 같은 경우는 반드시 작성해야함)

select A.a,B.d from A, B 
where 조건 and A.b = B.b;

select a,d from A, B 
where A.b = B.b */

-- 김현우가 주문한 책 이름과 가격
select newBook.bookname, newBook.price 
from newBook, newOrders 
where newOrders.member = '김현우' and newBook.bookid = newOrders.bookid;

-- 실습2 : 2개의 테이블을 이용한 조인 검색 (운송장 번호 출력)
select * from newBook;
select * from newOrders;

select newOrders.orderid, newOrders.member, newBook.bookname, newBook.price, newOrders.address 
from newBook, newOrders 
where newOrders.bookid = newBook.bookid;

-- 문자열 연결하기 : concat
select concat('data', 'base');

-- bookname과 publisher 연결하기
select concat(bookname, ' : ', publisher) from Book;

-- 대소문자 변경하기 : lower(소문자), upper(대문자)
select lower('Database SQL'), upper('Database SQL');

-- 영어 문자열 길이 반환하기 : length
select length('Databsae SQL');

-- 한글 문자열 길이 반환하기 : 한글 한글자가 3byte
select length('데이터베이스');

-- 정확한 문자열 길이 반환하기 : char_length(자릿수)
select char_length('데이터베이스');

-- 문자열 왼쪽 공백 제거하기 : ltrim
select ltrim('       데이터베이스       ');

-- 문자열 오른쪽 공백 제거하기 : rtrim
select rtrim('       데이터베이스       ');

-- 문자열 양쪽 공백 제거하기 : trim
select trim('       데이터베이스       ');

-- 문자열 변경하기 : replace(열 또는 문자, 변경하려는 문자, 변경문자)
select replace('데이터베이스 프로그래밍', '데이터베이스', '웹');

-- DBMS 시스템상의 오늘 날짜를 반환 : sysdate / now / current_date / current_time
select sysdate();
select now();
select current_date();
select current_time();
select month('2024-07-25 10:28:02');
select day('2024-07-25 10:28:02');
select hour('2024-07-25 10:28:02');

-- 날짜 차이 계산하기 : datediff(기준날짜, 비교날짜)
select datediff('2024-10-12', '2024-07-25');

-- 날짜 더하기 : adddate(기준날짜, 숫자)
select adddate('2024-10-12', 10);

-- 절댓값 계산하기 : abs(숫자)
select abs(-80), abs(80);

-- 반올림한 값을 구하기 : round(숫자, 자릿수)
select round(12.678, 1);

-- 6-1 도서 제목에 '데이터'가 포함된 도서를 'Data'로 변경한 후 도서 목록을 출력
select replace(bookname, '데이터', 'Data')
bookname, publisher, price from Book;

-- 6-2 한빛아카데미에서 출판한 도서의 제목과 제목의 문자 수, 바이트 수를 출력
select bookname as '제목', 
char_length(bookname)as '문자수', 
length(bookname) as '바이트수' from Book 
where publisher = '한빛아카데미';

-- 6-3  Book 테이블에 새로운 속성 추가주문 날짜 : orderdate(DATE타입)
alter table Book 
add orderdate date;
select * from Book;

-- 6-4 각 도서에 주문 날짜 데이터 추가 후, 목록을 출력
update book set orderdate = '2024-05-12' where bookid = 100;
update book set orderdate = '2024-05-04' where bookid = 101;
update book set orderdate = '2024-06-02' where bookid = 102;
update book set orderdate = '2024-06-10' where bookid = 103;
update book set orderdate = '2024-05-12' where bookid = 104;
update book set orderdate = '2024-04-12' where bookid = 105;
update book set orderdate = '2024-03-15' where bookid = 106;
update book set orderdate = '2024-05-12' where bookid = 107;
update book set orderdate = '2024-06-07' where bookid = 108;
update book set orderdate = '2024-04-26' where bookid = 109;
update book set orderdate = '2024-05-28' where bookid = 110;

-- 6-5 주문일로부터 10일 후 매출을 확정한다고 할 때, 각 주문의 확정 일자를 계산
select bookid as '주문번호', orderdate as '주문일자',
adddate(orderdate, 10) as '확정일자'
from book;



