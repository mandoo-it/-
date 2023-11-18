import sys
from collections import deque


def bfs():
    while move:
        cur = move.popleft()
        if cur == sister:
            print(visited[cur])
            return
        for item in (cur-1, cur+1, cur*2):
            if 0 <= item <= 100000 and not visited[item]:
                visited[item] = visited[cur] + 1
                move.append(item)



subin, sister = map(int, input().split())
visited = [0] * 100001
move = deque()
move.append(subin)
bfs()
