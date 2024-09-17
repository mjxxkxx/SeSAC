-- create database StudentDB;
use StudentDB;
create table StudentInfo(
	id int,
    name varchar(20),
    age int,
    address varchar(20),
    course varchar(20)
); 

/*
insert into StudentInfo(id, name, age, address, course)
values(1, '문종헌', 24, '서울', '영어');
insert into StudentInfo(id, name, age, address, course)
values(2, '오한솔', 22, '부산', '수학');
insert into StudentInfo(id, name, age, address, course)
values(3, '정국철', 25, '서울', '음악');
insert into StudentInfo(id, name, age, address, course)
values(4, '박기석', 27, '대전', '국어');
insert into StudentInfo(id, name, age, address, course)
values(5, '안창범', 20, '광주', '수학');
insert into StudentInfo(id, name, age, address, course)
values(6, '박홍진', 22, '부산', '컴퓨터');
insert into StudentInfo(id, name, age, address, course)
values(7, '공지훈', 28, '강원', '국어');
insert into StudentInfo(id, name, age, address, course)
values(8, '정희성', 30, '제주', '음악');
insert into StudentInfo(id, name, age, address, course)
values(9, '이봉림', 34, '대전', '영어');
insert into StudentInfo(id, name, age, address, course)
values(10, '김현우', 21, '서울', '컴퓨터');*/


select id, name from StudentInfo;

-- 3-1 나이가 30 이상인 학생 정보 검색
select * from StudentInfo where age >= 30;

-- 3-2 '컴퓨터'를 수강하는 학생 정보 검색
select * from StudentInfo where course = '컴퓨터';

-- 3-3 이름이 '박기석'인 학생 정보 검색
select * from StudentInfo where name = '박기석';

-- 3-4 나이가 20~25살 사이인 학생 정보 검색
select * from StudentInfo where age between 20 and 25;

-- 3-5 나이가 28살이거나 34살인 학생 정보 검색
select * from StudentInfo where age in (28, 34);

-- 3-6 성이 '김'씨인 학생 정보 검색
select * from StudentInfo where name like '김%';

-- 3-7 이름의 두번째 글자가 '지'이고, 그 뒤는 무엇이든 관계없는 학생 정보 검색
select * from StudentInfo where name like '_지%';

-- 3-8 나이를 기준으로 오름차순 정렬하여 검색
select * from StudentInfo order by age asc;

-- 3-9 나이가 많은 사람부터 적은 사람 순으로 순차적으로 검색
select * from StudentInfo order by age desc;

-- 4-5 학생들의 나이 총 합 계산
select sum(age) as '나이총합' from StudentInfo;

-- 4-7 '컴퓨터'를 수강하는 학생들의 평균 나이 계산
select avg(age) as '평균 나이' from StudentInfo where course = '컴퓨터';

-- 4-8 '영어'과목을 수강하는 학생 수를 계산
select count(*) as '수강인원' from StudentInfo where course = '영어';

-- 4-9 각 지역별 학생 수를 계산
select address, count(*) as '수강인원' from StudentInfo 
group by address;

-- 4-10 각 지역별 학생들의 평균 나이를 계산
select address, avg(age) as '평균 나이' from StudentInfo 
group by address;

-- 4-11 과목별 평균 나이가 25세 이상인 과목명과 학생 수를 계산
select course, count(*) as '수강생수' from StudentInfo
group by course 
having avg(age) >= 25;

-- 4-6 
select distinct course from student;

-- 5-1 '박기석'학생의 주소를 '제주'로 변경
update StudentInfo set address = '제주' where name = '박기석';

-- 5-2 id가 10인 학생을 삭제
delete from StudentInfo where id = 10;
select * from StudentInfo;

-- 5-3 학생 정보 테이블에 새로운 속성 추가
alter table StudentInfo add score varchar(2);
select * from StudentInfo;

-- 5-4 각 학생의 score 속성에 학점 값 삽입 순서대로 A, B, A, C, B, D, A, C, D, A 입력
update StudentInfo set score = 'A' where id = 1;
update StudentInfo set score = 'B' where id = 2;
update StudentInfo set score = 'A' where id = 3;
update StudentInfo set score = 'C' where id = 4;
update StudentInfo set score = 'B' where id = 5;
update StudentInfo set score = 'D' where id = 6;
update StudentInfo set score = 'A' where id = 7;
update StudentInfo set score = 'C' where id = 8;
update StudentInfo set score = 'D' where id = 9;
update StudentInfo set score = 'A' where id = 10;

-- 5-5 각 학점 별 학생 수 계산
select score, count(*) as '학생수' from StudentInfo group by score;

-- 5-6 '컴퓨터'또는 '영어' 과목을 수강하는 학생의 이름 및 과목명 
select name, course from StudentInfo where course in ('컴퓨터', '영어');
