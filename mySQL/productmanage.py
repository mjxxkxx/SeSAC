# 라이브러리 추가
import pymysql
from tabulate import tabulate

# 데이터베이스 연결자 생성
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='ShopDB',
                       charset='utf8')

# 커서 생성
curs = conn.cursor()
print('  ')
print('===============================================')
print('==============제품 관리 프로그램===============')
print('===============================================')
print('  ')

while True:
    choice = int(input("메뉴를 선택하세요. \n \n 1.전체제품보기\n 2.제품검색\n 3.제품추가\n 4.제품수정\n 5.제품삭제\n 6.종료(exit)\n"))

    if choice == 1:  # 전체제품 보기
        sql = "select * from product;"
        curs.execute(sql)
        result = curs.fetchall()
      
        print("-" * 33)
        print("제품번호  제품명  가격     수량")
        print("-" * 33)
    
        for row in result:
            print(f"{row[0]:<9} {row[1]:<4} {row[2]:<8} {row[3]:<5}")
    
        print("-" * 33)

    elif choice == 2:  # 제품검색
        name = input('제품명을 입력하세요:')
        sql = "select * from product where pName = %s;"
        curs.execute(sql, (name,))
        result = curs.fetchone()

        if result:
            print(result)
        else:
            print("해당 제품을 찾을 수 없습니다.")

    elif choice == 3:  # 제품추가
        new_code = input('제품번호:')
        new_name = input('제품명:')
        new_price = int(input('가격:'))
        new_amount = int(input('수량:'))

        sql = "insert into product (pCode, pName, price, amount) values (%s, %s, %s, %s);"
        curs.execute(sql, (new_code, new_name, new_price, new_amount))
        conn.commit()  # 데이터베이스에 변경 사항을 커밋
        print("제품이 성공적으로 추가되었습니다.")

    elif choice == 4:  # 제품수정
        ask = int(input("수정하실 항목이 제품번호이면 1을, 아니면 2를 입력하세요:"))

        if ask == 1:
            code = input("수정하고 싶은 제품번호를 입력해주세요:")
            new_code = input("업데이트 하실 제품번호를 입력하세요:")
            sql = "update product set pCode = %s where pCode = %s;"
            curs.execute(sql, (new_code, code))
            conn.commit()
            print("제품번호가 성공적으로 업데이트되었습니다.")

        elif ask == 2:
            update_code = input("업데이트 하실 제품의 제품번호를 입력하세요:")
            update_choice = int(input("업데이트 하실 항목 (제품명(1), 가격(2), 수량(3)):"))

            if update_choice == 1:
                name = input("변경할 이름을 입력하세요:")
                sql = "update product set pName = %s where pCode = %s;"
                curs.execute(sql, (name, update_code))
                conn.commit()
                print("제품명이 성공적으로 업데이트되었습니다.")

            elif update_choice == 2:
                price = int(input("변경할 가격을 입력하세요:"))
                sql = "update product set price = %s where pCode = %s;"
                curs.execute(sql, (price, update_code))
                conn.commit()
                print("가격이 성공적으로 업데이트되었습니다.")

            elif update_choice == 3:
                amount = int(input("변경할 수량을 입력하세요:"))
                sql = "update product set amount = %s where pCode = %s;"
                curs.execute(sql, (amount, update_code))
                conn.commit()
                print("수량이 성공적으로 업데이트되었습니다.")

            else:
                print("잘못 입력하셨습니다.")

        else:
            print("잘못 입력하셨습니다.")

    elif choice == 5:  # 제품삭제
        delete_id = input("삭제하실 항목의 제품번호를 입력하세요:")
        sql = "delete from product where pCode = %s;"
        curs.execute(sql, (delete_id,))
        conn.commit()
        print("제품이 성공적으로 삭제되었습니다.")

    elif choice == 6:  # 종료
        print("시스템을 종료합니다.")
        break

    else:
        print("올바른 메뉴를 선택하세요.")

# 리소스 정리
curs.close()  # 커서 닫기
conn.close()  # 연결 닫기