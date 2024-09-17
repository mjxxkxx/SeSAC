import random

small_max_num = 10
max_num = 10000000
small_random_int = random.randint(0, small_max_num)
random_int = random.randint(0, max_num)
random_float = random.uniform(0, max_num)

def updown_game_easy(guess):
    if guess > small_random_int:
        return 'down'
    elif guess < small_random_int:
        return 'up'
    return guess == small_random_int

def updown_game_medium(guess):
    if guess > random_int:
        return 'down'
    elif guess < random_int:
        return 'up'
    return guess == random_int

def updown_game_hard(guess):
    if guess - random_float > 0.001:
        return 'down'
    elif guess - random_float < -0.001:
        return 'up'
    return abs(random_float - guess) < 0.001


def naive_finder(f, lst = list(range(100000000))):
    for i in lst:
        res = f(i)
        # print(res)
        if res == True:  
            return i
    return -1

if __name__ == '__main__':

    from time import time 

    begin = time()

    random_int = random.randint(0, max_num)  
    # random_int를 새로 생성하여 문제 방지
    # 여기서 random_int를 메인 블록에서 다시 생성하고 
    # 이를 사용해 updown_game_medium 함수를 실행합니다. 
    # 이렇게 하면 random_int가 naive_finder 함수 내에서 
    # 일관되게 사용되어 올바른 값을 찾을 수 있게 됩니다.
    
    print(naive_finder(updown_game_medium, list(range(max_num + 1))))
    end = time()

    print(end - begin)