from collections import deque
diry = [-1, 1, 0, 0]
dirx = [ 0, 0,-1, 1]

def bfs(i, j):
    que = deque([(i, j)])
    visited[i][j] = 1
    count = 1
    while que:
        cy, cx = que.popleft()
        for d in range(4):
            ny = cy + diry[d]
            nx = cx + dirx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[cy][cx] + 1
                    que.append((ny, nx))
                    count += 1

    return count

n, m, k = map(int, input().split())
arr = [[0 for _ in range(m)]for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
res =  - 1000
for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == -1:
            res = max(res, bfs(i, j) )
print(res)
