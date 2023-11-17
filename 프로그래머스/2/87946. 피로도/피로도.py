from itertools import permutations as p
    
def solution(k, dungeons):
    answer = -1
    arr = p(dungeons, len(dungeons))
    for route in arr:
        cur = k
        count = 0
        
        for item in route:
            if cur >= item[0]:
                cur -= item[1]
                count += 1
                if cur < 0: 
                    break
            else :
                break
        answer = max(count, answer)
    
    return answer