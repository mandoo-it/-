def dfs(graph, start, visited):
    visited[start] = True
    count = 1

    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)

    return count


n = int(input())  
m = int(input())  

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n + 1)
result = dfs(graph, 1, visited) - 1 

print(result)
