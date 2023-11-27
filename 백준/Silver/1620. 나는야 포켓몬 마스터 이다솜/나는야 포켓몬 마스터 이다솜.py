import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name_arr = dict()
num_arr = dict()

for i in range(1, n+1):
    wo = input().rstrip()
    name_arr[wo] = i
    num_arr[i] = wo

for i in range(m):
    word = input().rstrip()
    if word.isnumeric():
        print(num_arr[int(word)])
    else:
        print(name_arr[word])
