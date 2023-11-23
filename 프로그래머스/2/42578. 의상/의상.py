from collections import defaultdict 
def solution(clothes):
    answer = 1
    arr = defaultdict(int)
    for name, category in clothes:
        arr[category] += 1
    for item in arr:
        answer *= (arr[item]+1)
    return answer-1