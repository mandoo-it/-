import numpy as np

def solution(answers):
    answer = []
    arr = []
    nump = []
    arr.append(np.tile(np.array([1, 2, 3, 4, 5]), len(answers)))
    arr.append(np.tile(np.array([ 2, 1, 2, 3, 2, 4, 2, 5]), len(answers)))
    arr.append(np.tile(np.array([ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]), len(answers)))
    
    for i in range(len(arr)) :
        count = 0
        for n1, n2 in zip(arr[i], answers):
            print(n1, n2)
            if n1 == n2:
                count += 1
        nump.append(count)
    
    max_score = max(nump)
    for i in range(len(nump)):
        if nump[i] == max_score:
            answer.append(i + 1)
    
    return sorted(answer)