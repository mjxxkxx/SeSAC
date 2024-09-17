import random 

# --------------------------------------------
# 1. max / min 구현하기 
#
# cmp라는 함수를 이용한 min/max 구현하기. 
# cmp는 두 원소 중 더 큰 것을 반환하는 함수. 
# --------------------------------------------

def my_max(lst, cmp=lambda x, y: x):
    max_elem = lst[0]                      
    for e in lst[1:]:                   
        # if cmp(max_elem,e) == e: 
        #     max_elem = e
        max_elem = cmp(e, max_elem)
    return max_elem 

l = [(1,2), (3,4), (5,-3), (2,-5)] 
my_max(l, cmp = lambda x, y: x if sum(x) > sum(y) else y)
my_max(l, cmp = lambda x, y: x if x[0] > y[0] else y)

def my_min(lst, cmp = lambda x, y: x):
    min_elem = lst[0]                      
    # for x, y in lst[1:]:                   
    #     if cmp(min_elem,(x,y)) == (x, y): 
    #         min_elem = (x, y)
    for e in lst[1:]:                   
        if cmp(min_elem, e) == min_elem: 
            min_elem = e
    return min_elem

my_min(l, cmp = lambda x, y: x if x[0] > y[0] else y)

# --------------------------------------------
# 2. sort 구현하기 
# 
# 1) 그냥 순서대로 오름차순으로 정렬하기 
# 나
def find_insert_index(res, e):
    for idx, elem in enumerate(res):
        if elem < e:
            return idx 
    return len(res)

def sort1(lst):
    first_elem = lst[0]
    res = []
    res.append(first_elem)
    
    for e in lst[1:]:
        idx = find_insert_index(res, e)
        res.insert(idx, e)

    return res

# 쌤
def sort1(lst):
    res = []
    n = len(lst)
    while len(res) < n:
        res.append(my_min(lst, cmp = lambda x, y:x if x>y else y))
        lst.remove(my_min(lst, cmp = lambda x, y:x if x>y else y))
    return res 

# 태진
def sort1(lst):
    n = len(lst)
    for i in range(n):
      for j in range(0,n-i-1):
        if lst[j] > lst[j+1]:
          lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

# 2) 오름차순, 내림차순으로 정렬하기 
def left_append(lst, elem):
    lst.insert(0,elem)
    return lst
    
def sort2(lst, upper_to_lower = True):
    res = []
    n = len(lst)
    while len(res) < n:
        if upper_to_lower:
            res.append(my_max(lst, cmp = lambda x, y:x if x>y else y))
        else:
            res = left_append(res, my_max(lst, cmp = lambda x, y:x if x>y else y))
        lst.remove(my_max(lst, cmp = lambda x, y:x if x>y else y))
    return res

# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
'''
def sort3_min(lst, upper_to_lower = True, cmp = lambda x,y:x):
    res = []
    c = [e for e in lst]
    n = len(lst)
    
    while len(res) < n:
        m = my_min(c, cmp) 
        if not upper_to_lower:
            res.append(m) 
        else:
            res = [m] + res
        c.remove(m) 
        
    return res

def sort3_insert(lst, upper_to_lower = True, cmp = lambda x,y:x):
    res = []

    for elem in lst:
        new_idx = get_insert_idx(res, elem, upper_to_lower = upper_to_lower, cmp = cmp)
        res.insert(new_idx, elem)
    
    return res
'''

def left_append(lst, elem):
    lst.insert(0,elem)
    return lst

def sort3(lst, upper_to_lower = True, cmp = lambda x, y: x):
    res = []
    n = len(lst)
    while len(res) < n:
        if upper_to_lower:
            res.append(my_max(lst, cmp = cmp))
        else:
            res = left_append(res, my_max(lst, cmp = cmp))
        lst.remove(my_max(lst, cmp = cmp))
    return res
# sort3(l, cmp = lambda x, y: x if x > y else y)

# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기 
def sort4(lst, upper_to_lower = True, cmp = lambda x, y: x):
    max_elem = lst[0]                      
    for e in lst[1:]:                   
        if cmp(max_elem, e) == e: 
            max_elem = e
            return max_elem
        elif cmp(max_elem, e) == e == max_elem:
            return 'same value'

# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기 
'''
def sort5_min(lst, upper_to_lower = True, cmp = lambda x, y: x, tie_breaker = lambda x, y: random.choice([x,y])):
    res = []
    c = [e for e in lst]
    n = len(lst)
    
    while len(res) < n:
        m = my_min(c, cmp, tie_breaker = tie_breaker) 
        if not upper_to_lower:
            res.append(m) 
        else:
            res = [m] + res
        c.remove(m) 
        
    return res

def sort5_insert(lst, upper_to_lower = True, cmp = lambda x, y: x, tie_breaker = lambda x, y: random.choice([x,y])):
    res = []

    for elem in lst:
        new_idx = get_insert_idx(res, elem, upper_to_lower = upper_to_lower, cmp = cmp, tie_breaker = tie_breaker)
        res.insert(new_idx, elem)
    
    return res 


tuple_lst = [ (1,3),(1,2), (1,5), (1,4),(2,3), (5,3), (19, 2), (6, 100)]
print(sort5_insert(tuple_lst, cmp = my_compare, tie_breaker = lambda x, y: x if x[1] > y[1] else y))
'''

def sort5(lst, upper_to_lower = True, cmp = lambda x, y: x, tie_breaker = lambda x, y: random.choice([x,y])):
    res = []
    n = len(lst)

    while len(res) < n:
        if upper_to_lower:
            res.append(my_max(lst, cmp = cmp))
        else:
            res = left_append(res, my_max(lst, cmp = cmp))
        lst.remove(my_max(lst, cmp = cmp))
        
    return res


lst = [(1, 3), (2, 4), (2,5), (3, 10), (3,5)]

def compare(x, y):
    if x[0] > y[0]: return x 
    elif x[0] < y[0]: return y
    else: return 'same value' 
def compare(x, y):
    if x[0] > y[0]: return x 
    elif x[0] < y[0]: return y
    else: return 'same value' 

sort5(lst, cmp = compare, tie_breaker = lambda x, y: x if x[1] > y[1] else y)



# --------------------------------------------
# os_file_concept.py 해보고 올 것 
# --------------------------------------------

# --------------------------------------------
# 3. safe pickle load/dump 만들기 
# 
# 일반적으로 pickle.load를 하면 무조건 파일을 읽어와야 하고, dump는 써야하는데 반대로 하면 굉장히 피곤해진다. 
# 이런 부분에서 pickle.load와 pickle.dump를 대체하는 함수 safe_load, safe_dump를 짜 볼 것.  
# hint. 말만 어렵고 문제 자체는 정말 쉬운 함수임.
# --------------------------------------------

def safe_load(pickle_path):
    pass 

def safe_dump(pickle_path):
    pass 


# --------------------------------------------
# 4. 합성함수 (추후 decorator)
# 
# 1) 만약 result.txt 파일이 없다면, 함수의 리턴값을 result.txt 파일에 출력하고, 만약 있다면 파일 내용을 읽어서 
#    '함수를 실행하지 않고' 리턴하게 하는 함수 cache_to_txt를 만들 것. txt 파일은 pickle_cache 폴더 밑에 만들 것.  
# 2) 함수의 실행값을 input에 따라 pickle에 저장하고, 있다면 pickle.load를 통해 읽어오고 없다면 
#    실행 후 pickle.dump를 통해 저장하게 하는 함수 cache_to_pickle을 만들 것. pickle 파일은 pickle_cache 폴더 밑에 만들 것. 
# 3) 함수의 실행값을 함수의 이름과 input에 따라 pickle에 저장하고, 2)와 비슷하게 진행할 것. pickle 파일은 pickle_cache 폴더 밑에, 각 함수의 이름을 따서 만들 것 
# --------------------------------------------

def cache_to_txt(function):
    pass 

def cache_to_pickle(function):
    pass 


