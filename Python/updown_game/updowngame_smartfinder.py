import random 

small_max_num = 10
max_num = 10000000
small_random_int = random.randint(0, small_max_num)
print('small random int', small_random_int)
random_int = random.randint(0, max_num)
print('random int', random_int)
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

def smart_finder(f, min_input=0, max_input=100):
    while min_input <= max_input:
        mid = (min_input + max_input) // 2
        res = f(mid)
        print(res)
        if res is True:
            return mid  # Found the correct number
        elif res == 'up':
            min_input = mid + 1  # Search in the upper half
        elif res == 'down':
            max_input = mid - 1  # Search in the lower half
        else:
            return -1  # Invalid response from the game function
    
    return -1  # Number not found within the given range

if __name__ == '__main__':

    from time import time 

    begin = time()

    random_int = random.randint(0, max_num)  
   
    # random_int를 새로 생성하여 문제 방지
    # 여기서 random_int를 메인 블록에서 다시 생성하고 
    # 이를 사용해 updown_game_medium 함수를 실행합니다. 
    # 이렇게 하면 random_int가 naive_finder 함수 내에서 
    # 일관되게 사용되어 올바른 값을 찾을 수 있게 됩니다.
    
    print(smart_finder(updown_game_medium, min_input=0, max_input=max_num))
    end = time()

    print(end - begin)