import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key= lambda x : (x[1], x[0]))

ans = 0
end = 0

for item in arr:
    if item[0] >= end:
        ans += 1 
        end = item[1]
        
print(ans)
        
        
            
    