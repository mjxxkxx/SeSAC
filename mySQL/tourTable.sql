-- create database tourDB;

use tourDB;

-- tourTable 테이블 데이터 조회하기
select * from tourTable;

-- 1. 시도명을 한번만 출력
select distinct 시도명 from tourTable;

select 시도명 from tourTable
group by 시도명;

-- 2. 경기도의 관광지 정보 검색
select * from tourTable 
where 주소 like '경기%';

select * from tourTable 
where 시도명 = '경기도';

-- 3. 쇼핑 분야의 관광지 수 계산
select count(*) as '쇼핑' from tourTable 
where 중분류 like '쇼핑';

-- 4. 각 분야 별 관광지 수 계산
select 중분류, count(*) as '관광지 수' from tourTable
group by 중분류;

-- 5. 테마공원의 이름 및 주소 검색
select 관광지명, 주소 from tourTable 
where 소분류 = '테마공원';

-- 6. 검색건수가 60만 건 이상인 관광지 수 계산
select 소분류, count(*) as '관광지 수' from tourTable 
where 검색건수 >= 600000
group by 소분류;

-- 7. 가장 인기가 없는 관광지부터 인기가 많은 순으로 조회
select * from tourTable 
order by 검색건수;

-- 8. 10개의 관광지 정보만 조회
select * from tourTable
Limit 10;