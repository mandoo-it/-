from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    idx_arr = deque(list(range(n)))
    # print(arr[0])
    count = 0
    while True:
        if arr[0] == max(arr):
            count += 1
            if idx_arr[0] == m:
                print(count)
                break
            else:
                arr.popleft()
                idx_arr.popleft()
        else:
            arr.append(arr.popleft())
            idx_arr.append(idx_arr.popleft())





