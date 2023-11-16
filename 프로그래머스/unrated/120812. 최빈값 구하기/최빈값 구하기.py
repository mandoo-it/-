from collections import Counter
def solution(array):
    answer = 0
    count = 0
    array = Counter(array)
    maxd = max(array.values())
    print(maxd)
    for i in array: 
        if array[i] == maxd:
            answer = i
            count += 1
    if count>1: 
        return -1 
        
    return answer