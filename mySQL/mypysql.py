# 라이브러리 추가
import pymysql

# 연결자 생성
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root',
                       db = 'ShopDB',
                       charset = 'utf8')
                
# 커서 생성
curs = conn.cursor()

# # SQL문 실행
# sql = 'select * from product'
# curs.execute(sql)

# # 모든 데이터 가져오기
# result = curs.fetchall()

# # result 타입 확인
# print(type(result))

# # 출력
# for data in result:
#     print(data)

# # 2줄의 데이터만 가져오기
# result = curs.fetchmany(2)

# # 출력
# for data in result:
#     print(data)

# # 1줄의 데이터만 가져오기
# result = curs.fetchone()

# # 출력
# print(result)

# # 데이터 1개 가져오기
# result = curs.fetchone()
# print("데이터출력:", result)

# # 모든 데이터 가져오기
# result = curs.fetchall()
# print("데이터출력:", result)

# # SQL문 실행
# sql = "insert into product(pCode, pName, price, amount) values('p0005', '핸드폰', 800000, 5)"
# curs.execute(sql)

# # 실습
# sql = "update product set price = 50000 where pcode = 'p0003' "
# curs.execute(sql)
# result = curs.fetchall()
# print(result)

# # 실습
# sql = "delete from product where pCode = 'p0005'"
# curs.execute(sql)
# result = curs.fetchall()
# print(result)

# # 실습
# sql = "select * from product where pCode = %s"
# curs.execute(sql,('p0002'))

# result = curs.fetchone()
# print(result)

# # 동적 SQL 만들기 - 1
# # 가격이 50만원~100만원 사이의 제품을 검색
# sql = "select * from product where price between %s and %s"
# curs.execute(sql, (500000,1000000))
# result = curs.fetchall()
# print(result)

# # 동적 SQL 만들기 - 2
# # 가격이 10만원 미만인 제품들의 평균가와 수량의 합을 계산
# sql = "select avg(price), sum(amount) from product where price < %s"
# curs.execute(sql, (100000,))
# result = curs.fetchall()
# print(result)

# # commit 실행
# conn.commit()

# # 데이터베이스 연결 종료
# conn.close()