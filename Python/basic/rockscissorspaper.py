print("### 가위, 바위, 보 게임 ###")
print("삼선승제로 먼저 이기는 사람이 승리!!!")

win1 = 0  # user1의 승리 횟수
win2 = 0  # user2의 승리 횟수

while True:
    # 사용자 입력 받기
    user1_input = input("user1 가위, 바위, 보를 입력하세요 : ")
    user2_input = input("user2 가위, 바위, 보를 입력하세요 : ")

    # 승리 조건 확인
    if (
        (user1_input == '가위' and user2_input == '보') or
        (user1_input == '바위' and user2_input == '가위') or
        (user1_input == '보' and user2_input == '바위')
    ):
        print("user1 승리")
        win1 += 1  # user1의 승리 횟수 증가
        print(f"user1 {win1}: user2 {win2}")
        print('-----------------------------------')

    elif (
        (user1_input == '가위' and user2_input == '바위') or
        (user1_input == '바위' and user2_input == '보') or
        (user1_input == '보' and user2_input == '가위')
    ):
        print("user2 승리")
        win2 += 1  # user2의 승리 횟수 증가
        print(f"user1 {win1}: user2 {win2}")
        print('-----------------------------------')

    elif user1_input == user2_input :
        print("비겼습니다!")
        print(f"user1 {win1}: user2 {win2}")
        print('-----------------------------------')

    else:
        print("잘못 입력하셨습니다.")
        print('-----------------------------------')

    # 3승 달성 시 게임 종료
    if win1 == 3:
        print("user1 3선승! 최종승리!")
        break
    elif win2 == 3:
        print("user2 3선승! 최종승리!")
        break