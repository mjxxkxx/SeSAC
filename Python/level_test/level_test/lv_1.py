all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'

# --------------------------------------------
# 1. list/tuple 기초 예제들 
# 
# a는 1,2,3이 들어간 튜플, 
# b는 a부터 z까지 모든 알파벳 소문자가 들어간 리스트가 되도록 만들어보세요. 
# b를 만들 때 위에 주어진 all_smallcase_letters와 for loop를 사용해도 좋고, 손으로 다 쳐도 좋습니다. 
# --------------------------------------------

a = (1,2,3)
b = []
for char in all_smallcase_letters:
    b.append(char)

# --------------------------------------------
# 2. dict 기초 예제 
# 
# 1) upper_to_lower
#
# upper_to_lower은 모든 대문자 알파벳(ex. A)을 key로 가지고, 대응하는 소문자 알파벳(ex. a)을 value로 가지는 dict입니다. 
# 위에서 만든 b와 for loop를 이용해서 upper_to_lower을 만들어보세요. 
# 
# 2) lower_to_upper
#
# upper_to_lower과 반대로 된 dict를 만들어보세요. 
# 
# 3) alpha_to_number
# 
# 소문자 알파벳 각각을 key, 몇 번째 알파벳인지를 value로 가지는 dict를 만들어보세요. 
# 위 all_smallcase_letters와 enumerate함수를 사용하세요. 
# 알파벳 순서는 1부터 시작합니다. ex) alpha_to_number['a'] = 1
# 
# 4) number_to_alphabet 
#
# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요. 

# --------------------------------------------
# 1) upper_to_lower
b = []
for char in all_smallcase_letters:
    b.append(char)
c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for key, value in zip (c,b):
    print(f"Key: {key}, Value: {value}")

# ----------------------------------------------------
# 2) lower_to_upper
b = []
for char in all_smallcase_letters:
    b.append(char)
c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for key, value in zip (b,c):
    print(f"Key: {key}, Value: {value}")

#-------------------------------------------------------
# 3) alpha_to_number
b = [char for char in all_smallcase_letters]

for index, char in enumerate(b, start=1):
    print(f"Key: {char}, Value: {index}")

#-------------------------------------------------------
# 4) number_to_alphabet 
# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요.
all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
number_to_alphabet = {}

for index, char in enumerate(all_smallcase_letters, start=1):
    number_to_alphabet[index] = (char, char.upper())

print(number_to_alphabet)

# --------------------------------------------
# 3. 주어진 문자열의 대소문자 바꾸기 
#
# 위 2에서 만든 dict들을 이용하여, 아래 문제들을 풀어보세요. 

alphabet = {
    'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
    'i': 'I', 'j': 'J', 'k': 'K', 'l': 'aL', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P',
    'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
    'y': 'Y', 'z': 'Z'
}

# 1) 주어진 문자열을 모두 대문자로 바꾼 문자열을 만들어보세요.

# M1)
a = 'absdf123SAFDSDF'
a_converted_upper = ''

for char in a:
    if char in alphabet: 
        a_converted_upper += alphabet[char]
    else:
        a_converted_upper += char  
        
print("Uppercase Conversion:", a_converted_upper)

# M2) 
all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
b = [char for char in all_smallcase_letters]
c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

a = 'absdf123SAFDSDF'
a_upper = ''

for char in a:
    if char in b:
        a_upper += char.upper()
    else:
        a_upper += char

print(a_upper)

# 2) 주어진 문자열을 모두 소문자로 바꾼 문자열을 만들어보세요.

# M1)
all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
b = [char for char in all_smallcase_letters]
c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

a = 'absdf123SAFDSDF'
a_lower = ''

for char in a:
    if char in c:
        a_lower += char.lower()
    else:
        a_lower += char

print(a_lower)

# M2)
reversed_alphabet = {value: key for key, value in alphabet.items()}
a_converted_lower = '' 

for char in a:
    if char in reversed_alphabet: 
        a_converted_lower += reversed_alphabet[char]
    else:
        a_converted_lower += char 

print("Lowercase Conversion:", a_converted_lower)


# 3) 주어진 문자열에서 대문자는 모두 소문자로, 소문자는 모두 대문자로 바꾼 문자열을 만들어보세요.
a = 'absdf123SAFDSDF'
a_converted = ''

for char in a:
    if char in alphabet: 
        a_converted += alphabet[char]
    elif char in reversed_alphabet:
        a_converted += reversed_alphabet[char]
    else:
        a_converted += char  

print("upsidedown:", a_converted)

# 4) 주어진 문자열이 모두 알파벳이면 True, 아니면 False를 출력하는 코드를 짜보세요.
def contains_digit(s):
    for char in s:
        if '0' <= char <= '9':
            return False  
    return True 

print(contains_digit(a))

# --------------------------------------------
# 4. 다양한 패턴 찍어보기 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음 패턴을 프린트해보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------
for i in range(5):
    print(' '*(4-i) + '*' * (2*i+1))

# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음 패턴을 프린트해보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

for i in range(5):
    print(' '*(4-i) + '* ' * (i+1))

# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음 패턴을 프린트해보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------
all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
b = []
for char in all_smallcase_letters:
    b.append(char)

c = [char.upper() for char in b]

for i in range(5):
    print(' '*(4-i) + ' '.join(c[0:i+1]))


# --------------------------------------------
# 4) 피라미드 찍어보기 - 4 
# 
# 다음 패턴을 프린트해보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1
# --------------------------------------------
def pascal(n):
    def generate_next_line(last_line):
        next_line = [1]
        for i in range(len(last_line) - 1):
            next_line.append(last_line[i] + last_line[i + 1])
        next_line.append(1)
        return next_line
    
    lines = [[1], [1, 1]]
    
    while len(lines) < n:
        lines.append(generate_next_line(lines[-1]))
    
    max_number = max(max(line) for line in lines)
    max_digit = len(str(max_number))
    space = ' ' * (max_digit + 1)
    
    for idx, line in enumerate(lines):
        print((n - 1 - idx) * space + space.join(f"{num:>{max_digit}}" for num in line))
    
    return lines

for line in pascal(12):
    print(line)


# --------------------------------------------
# 5) 다음 패턴을 찍어보세요. 
# 
# *         *         * 
#   *       *       *   
#     *     *     *     
#       *   *   *       
#         * * *         
#           *           
#         * * *         
#       *   *   *       
#     *     *     *     
#   *       *       *   
# *         *         * 
# --------------------------------------------

for i in range(5):
    print(' '*(2*i) + '*' + ' '*(9-2*i)+ '*' + ' '*(9-2*i) + '*')
print('          ' + '*' + '          ')
for i in range(5):
    print(' '*(9-2*i) + '*' + ' '*(2*i)+ '*' + ' '*(2*i) + '*')

