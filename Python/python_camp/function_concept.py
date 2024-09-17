# --------------------------------------------
# 1. 함수의 다양한 입력들 살펴보기 
#
# 1) input이 없는 함수 
# 2) input이 여러 개 있는 함수 
# 3) input이 정해지지 않은 갯수만큼 있는 함수 
# --------------------------------------------

def pi():
    pi = 3.14159
    return f"{pi:.2f}"
 
lst = [1,2,3,4,5]
def left_append(lst, elem):
    lst.insert(0,elem)
    return lst

# left_append(lst,0)

def left_extend(lst, *elem):
    """lst의 왼쪽에 정해지지 않은 갯수의 elem을 넣고 lst를 반환하는 함수 
    """
    lst.insert(0,elem)
    return lst

# --------------------------------------------
# 2. 함수의 call stack 알아보기 
# 
# 1) 아래 함수 b()를 실행할 때, 실행된 함수의 순서는?
# --------------------------------------------

def a():
    return pi()

def b():
    return a()

b() -> a() -> pi()

# --------------------------------------------
# 2) 아래 함수 c()를 실행할 때, 실행된 함수의 순서와 각 함수의 input은? 
# --------------------------------------------

def c(lst):
    print(lst[0])

    return c(lst[1:]) 

c(list(range(10)))
0
1
2
3
4
5
6
7
8
9
[] index error
