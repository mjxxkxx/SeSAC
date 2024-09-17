def get_insert_idx(res, elem, 
        cmp = lambda x, y: x if x > y else y, ):

    for i, e in enumerate(res):
        case = cmp(elem, e)
        if elem == cmp(elem, e): # elem > e:
            return i 
    
    return len(res)


def sort3_insert(lst, cmp = lambda x, y: x if x > y else y):
    res = []

    for elem in lst:
        new_idx = get_insert_idx(res, elem, cmp = cmp)
        res.insert(new_idx, elem)
    
    return res 


def merge_sort(lst, cmp = lambda x, y: x if x > y else y):
    lst1 = lst[:len(lst)//2]
    lst2 = lst[len(lst)//2:]

    left = merge_sort(lst1)
    right = merge_sort(lst2)

    
        
            
    return merge(left, right)

def merge(left, right, cmp = lambda x, y: x if x > y else y):
    res = []
    for l in left:
        for r in right:
            if l < r:
                res.append(l)
            elif l > r:
                res.append(r)
    return res 

left = [1,3,4,7]
right = [2,5,6,8,9,10,11]

def merge_schin(left, right):
    left_idx = 0 
    right_idx = 0 

    res = []

    while left_idx <= len(left)-1 and right_idx <= len(right)-1:
        print(left_idx, right_idx)
        l = left[left_idx]
        r = right[right_idx]

        if l < r:
            res.append(l)
            left_idx += 1 
        else:
            res.append(r) 
            right_idx += 1 
        
    
    res += left[left_idx:]
    res += right[right_idx:]

    return res 



print(merge_schin(left, right))






def quick_sort(lst, cmp = lambda x, y: x if x > y else y):
    return lst 

def tim_sort(lst, cmp = lambda x, y: x if x > y else y):
    return lst 