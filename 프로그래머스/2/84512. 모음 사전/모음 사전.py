def dfs(alpa, cur, ans, count):
    count[0] += 1
    
    if cur == ans:
        return count[0]-1
    if len(cur) == 5: 
        return 
    for i in range(0, 5):
        found = dfs(alpa, cur+alpa[i], ans, count)
        if found is not None:
            return found
def solution(word):
    # count = 0
    alpa = ['A', 'E', 'I', 'O', 'U']
    
    # for i in range(0, len(word)):
    
    return dfs(alpa, "", word, [0])