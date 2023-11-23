def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i, item in enumerate(citations):
        if i >= item :
            return i
    return len(citations) 


#6 5 3 1 0

# 0 1 2 3 4