'''
6층짜리 건물이 있다. 사용자가 가고싶은 층을 선택하면, 
사용자가 서 있는 층에서 목적지가 이동하는 경로(층)를 출력하세요.
- 사용자는 1-6층 버튼만 누를 수 있다.
- 사용자가 현재 엘레베이터가 서 있는 층을 선택하면 다른 층을 선택하라는 메세지가 출력된다.
- 목적지에 도착하면 프로그램 종료
'''
import time  # time 모듈을 임포트합니다.

destination = int(input("가고자 하는 층 입력: "))
now = int(input("현재 위치 입력: "))

# 무한 루프 설정
while True:
    if destination > now:
        # 현재 위치를 1층씩 올라가면서 출력
        now += 1  # 현재 층수 증가
        print(f"현재 층은 {now}층입니다.")
        
        # 목적지 층에 도착하면 멈춤
        if now == destination:
            print(f"{destination}층에 도착했습니다. 안녕히 가세요")
            break
    
    elif destination < now:
        # 현재 위치를 1층씩 내려가면서 출력
        now -= 1  # 현재 층수 감소
        print(f"현재 층은 {now}층입니다.")
        
        # 목적지 층에 도착하면 멈춤
        if now == destination:
            print(f"{destination}층에 도착했습니다. 안녕히 가세요")
            break
    
    else:  # 현재 층과 목적지가 같을 때
        print("다른 층(1~6)을 눌러주세요.")
        break

    time.sleep(1)  # 1초 동안 대기합니다.