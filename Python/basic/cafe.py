remain = 10  # 남은 커피 수량 초기화

while True:
    if remain > 0:
        money_input = int(input("돈을 넣어주세요: "))
        if money_input >= 300:
            change = money_input - 300
            print(f"거스름돈 {change}를 주고 커피를 줍니다.")
            remain -= 1  # 커피 판매 후 남은 커피 수량 감소
           
        else:
            print("돈을 다시 돌려주고 커피를 주지 않습니다.")
            print(f"남은 커피의 양은 {remain}입니다.")
    
    elif remain == 0:
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            break