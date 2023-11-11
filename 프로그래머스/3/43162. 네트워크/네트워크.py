from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(n, computers, visited, i)
            answer += 1

    return answer

def bfs(n, computers, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()

        for i in range(n):
            if computers[current][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

# Example
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
