def dfs(arr, visited, i):
    visited[i] = True;
    count = 1
    for item in arr[i]: 
        if not visited[item]:
            count += dfs(arr, visited, item)
    return count
        
def solution(n, wires):
    answer = []
    arr = [[] for _ in range(n+1)]
    # visited = []

    for item in wires:
        arr[item[0]].append(item[1])
        arr[item[1]].append(item[0])
    
    for item in wires:
        arr[item[0]].remove(item[1])
        arr[item[1]].remove(item[0])
        visited = [False] * (n+1)
        
        for i in range(1, n+1) :
            if not visited[i]:
                cnt = dfs(arr, visited, i)
                print(visited)
        print(cnt)
        
        answer.append(abs((n - cnt) - cnt))
        
        arr[item[0]].append(item[1])
        arr[item[1]].append(item[0])
        
        print(answer)
    
    return min(answer)