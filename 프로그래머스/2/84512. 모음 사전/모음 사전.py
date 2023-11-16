
from itertools import product

def solution(word) :
    target = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1, 6) :
        tmp=list(map("".join, product(target, repeat=i)))
        print(tmp)
        arr+=tmp
        # if tmp==word:
        #     break;
    arr.sort()
    for i in range(len(arr)):
        if arr[i]==word:
            return i+1
