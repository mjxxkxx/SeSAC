# --------------------------------------------
# 1. 패턴 찍는 함수들 만들어보기 
# 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid1를 짜 보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------

# write your code here 
def pyramid1(n):
    for i in range(n):
        print(' '*(n-i) + '*' * (2*i+1))

# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid2를 짜 보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

# write your code here 
def pyramid2(n):
    for i in range(n):
        print(' '*(n-1-i) + '* ' * (i+1))

# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid3를 짜 보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

# write your code here 
def pyramid3(n):
    all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
    b = []
    for char in all_smallcase_letters:
        b.append(char)

    c = [char.upper() for char in b]

    for i in range(n):
        print(' '*(n-1-i) + ' '.join(c[0:i+1]))


# -------------------------------------------- 
# 4) 피라미드 찍어보기 - 4 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid4를 짜 보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1
# --------------------------------------------

# write your code here 
def pascal(n):
    def generate_next_line(last_line):
        n = len(last_line) + 1
        
        next_line = [last_line[0]]

        for i in range(n-2):
            next_line.append(last_line[i] + last_line[i+1])

        next_line.append(last_line[n-2])

        return next_line
    
    lines = [[1], [1,1]]
    
    while len(lines) != n:
        lines.append(generate_next_line(lines[-1]))

    space = ' '

    def fill(number, digits, fill_with = '0'):
        number_digit = get_digit(number)
        return (digits - number_digit) * fill_with + str(number)

    def get_digit(number):
        # int(log_10(n))
        # 123 
        digit = 1
        
        while True:
            if number < 10:
                break 
            else:
                digit += 1 
                number = number // 10 
        
        return digit 

    # print(fill(123, 4)) # 0123
    # print(fill(123, 5)) # 00123
    # print(fill(123, 4, '|')) # |123

    max_number = max(lines[-1])
    max_digit = get_digit(max_number)

    space = ' ' * max_digit

    for idx, line in enumerate(lines):
        print((n-1-idx)*space + space.join([\
            fill(e, max_digit, ' ') for e in line]))
    
    return lines 

for line in pascal(12):
    print(line)

# --------------------------------------------
# 5) 다음 패턴을 찍는 함수 sierpinski_triangle을 짜 보세요. 
# 
# n = 2
#         *
#        * *
#       *   *
#      * * * *
#     *       * 
#    * *     * *
#   *   *   *   * 
#  * * * * * * * * 
# 
# n = 3 
#                 *
#                * *
#               *   *
#              * * * *
#             *       * 
#            * *     * *
#           *   *   *   * 
#          * * * * * * * *
#         *               *   
#        * *             * *  
#       *   *           *   * 
#      * * * *         * * * *
#     *       *       *       *  
#    * *     * *     * *     * *
#   *   *   *   *   *   *   *   * 
#  * * * * * * * * * * * * * * * *
# --------------------------------------------

# write your code here 
def triangle():
    lines = [\
      '   *    ',
      '  * *   ',
      ' *   *  ',
      '* * * * ',
    ]
    return lines 

def lstsum(l, r):
    assert len(l) == len(r)
    
    res = []
    for i in range(len(l)):
        res.append(l[i] + r[i])

    return [(a+b) for a, b in zip(l, r)]

def big_triangle():
    res = []
    res += [' ' * 4 + line + ' ' * 4 for line in triangle()]
    
    res += lstsum(triangle(), triangle())
    
    return res 

# print('\n'.join(big_triangle()).replace(' ', '0'))

def big_big_triangle():
    res = []
    res += [' ' * 8 + line for line in big_triangle()]
    
    res += lstsum(big_triangle(), big_triangle())
    
    return res 

# print('\n'.join(big_big_triangle()))

def sierpinski_triangle_list(n):
    if n == 1:
        return triangle()
    else:
        res = [' '*2**n + line + ' '*2**n for line in sierpinski_triangle_list(n-1)]
        res += lstsum(sierpinski_triangle_list(n-1), sierpinski_triangle_list(n-1))
        return res 

def sierpinski_triangle(n):
    return '\n'.join(sierpinski_triangle_list(n))

print(sierpinski_triangle(1))
print(sierpinski_triangle(2))
print(sierpinski_triangle(3))
print(sierpinski_triangle(4))

#-------------------------------------------------------------------
'''
def triangle(n):
    width = 4 * 2**n
    half_of_width = 2*2**n
    print(' ' * (half_of_width-1) + '*')

    for j in range (1, (half_of_width)):
        j_remainder = j % 4
        print(' ' * (half_of_width - 2*j) + '*' + ' '* (2*(j_remainder)-1) + '*')
    print(' '* (4*(n-1)-1) + '* ' * (half_of_width))
    for i in range ((half_of_width)+1, width -1):
        remainder = i % 4
        print(' ' * (width-i-2) + '*' + ' '* (remainder+1)+'*'+' '*(2**(n+1)-(width-i-2)-(remainder+1)-(remainder+1)-2) +'*'+' '*(remainder) + '*')
    print('* '* (width))
def sierpinski_triangle(n):
    for i in range(n+2):
        print(' '*(n+1-i) + '*' + ' '*(n-2) * (i+1))
        for j in range(n):

def triangle(n):
    width = 4 * 2**(n-1)
    half_of_width = 2*2**(n-1)
    print(' ' * (half_of_width-1) + '*')

    for j in range (1,(half_of_width)-1):
        j_remainder = j % 4
        print(' ' * (half_of_width - 2*j) + '*' + ' '*(2*j-1) + '*')
    print(' '* (4*(n-1)-1) + '* ' * (half_of_width))
    for i in range ((half_of_width)+1, width -1):
        remainder = i % 4
        print(' ' * (width-i-2) + '*' + ' '* (2*remainder-1)+'*'+' '*(2**(n+1)-(width-i-2)-(2*remainder-1)-(2*remainder-1)-2) +'*'+' '*(2*remainder-1) + '*')
    print('* '* (width))

'''
# --------------------------------------------
# 2. 여러 리스트 관련 함수들 구현해보기 
#
# 아래 함수들은 대부분 itertools에 있는 함수들임. 
# itertools를 쓰지 말고 구현해 볼 것.  
#
# 1) accumulate(lst, function = lambda x, y : x+y)
# 
# lst의 각 원소들에 대해서, function을 누적하여 적용한 리스트를 반환. 
# lst -> [lst[0], f(lst[0], lst[1]), f(lst[2], f(lst[1], lst[0])), ...] 
# --------------------------------------------

# write your code here 
def accumulate(lst, function = lambda x, y: x+y):
    pass

# --------------------------------------------
# 2) batched(lst, n)
# 
# lst의 원소들을 n개의 인접한 원소들끼리 묶은 리스트를 반환. 
# ex) batched([1,2,3,4,5], 2) 
#     >> [(1,2), (3,4), (5,)]
# ex) batched(['a', 'b', 1, 3, 6, 1, 3, 7], 3) 
#     >> [('a', 'b', 1), (3, 6, 1), (1, 3, 7)]
# --------------------------------------------

# write your code here 
def batched(lst, n):
    pass

# --------------------------------------------
# 3) product(args)
# 
# list들의 list args를 받아서, 각각의 리스트에서 하나씩의 원소를 뽑은 튜플들의 리스트를 반환. 
# ex) product([[1,2,3], [4,5,6])
#     >> [(1,4), (1,5), (1,6), 
#         (2,4), (2,5), (2,6), 
#         (3,4), (3,5), (3,6),] 
# --------------------------------------------

# write your code here 
def product(args):
    pass

# --------------------------------------------
# 4) permutations(lst, r) 
#
# lst 안의 원소들 r개로 이루어진 permutation의 리스트를 반환. 
# permutation이란, 순서를 가지면서 중복을 허용하지 않는 부분집합을 의미함. 
# 즉 여기서는 1,2와 2,1은 다르고, 1,1은 허용되지 않음. 
# ex) permutations([1,2,3,4,5], 2)
#     >> [(1,2), (1,3), (1,4), (1,5), 
#         (2,1), (2,3), (2,4), (2,5), 
#         (3,1), (3,2), (3,4), (3,5), 
#         (4,1), (4,2), (4,3), (4,5), 
#         (5,1), (5,2), (5,3), (5,4),]
# --------------------------------------------

# write your code here 
def permutations(lst, r):
    pass

# --------------------------------------------
# 5) combination(lst, r) 
#
# lst 안의 원소들 r개로 이루어진 combination의 리스트를 반환. 
# combination이란, 순서를 가지지 않으면서 중복을 허용하지 않는 부분집합을 의미함. 
# 즉 여기서는 1,2와 2,1은 같고, 1,1은 허용되지 않음. 
# ex) combination([1,2,3,4,5], 2)
#     >> [(1,2), (1,3), (1,4), (1,5), 
#         (2,3), (2,4), (2,5), 
#         (3,4), (3,5), 
#         (4,5), ]
# --------------------------------------------

# write your code here 
def combination(lst, r):
    pass

# --------------------------------------------
# 6) combination_with_duplicate(lst, r)
#
# lst 안의 원소들 r개로 이루어진 중복을 허용하는 combination의 리스트를 반환. 
# ex) combination_with_duplicate([1,2,3,4,5], 2)
#     >> [(1,1), (1,2), (1,3), (1,4), (1,5), 
#         (2,2), (2,3), (2,4), (2,5), 
#         (3,3), (3,4), (3,5), 
#         (4,4), (4,5),
#         (5,5), ]
# --------------------------------------------

# write your code here 
def combination_with_duplicate(lst, r):
    pass

    


