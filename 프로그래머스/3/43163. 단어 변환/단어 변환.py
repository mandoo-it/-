from collections import deque

def bfs(begin, target, words):
    que = deque()
    que.append((begin, 0))
    visited = {begin}
    
    while que: 
        cur = que.popleft()
        # print()
        if cur[0] == target: 
               return cur[1]
        for item in words:
            if item not in visited:
                count = 0
                for i, j in zip(item, cur[0]):
                    if i != j:
                        count += 1
                if count <= 1 :
                    que.append((item, cur[1] + 1))
                    visited.add(item)
               
    return 0 
               
def solution(begin, target, words):
    answer = 0
    return bfs(begin, target, words)