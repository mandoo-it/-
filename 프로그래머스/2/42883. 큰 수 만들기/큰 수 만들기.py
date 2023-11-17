def solution(number, k):
    answer = ''
    result_len = len(number) - k
    arr = [0] * (result_len)
    idx = 0
    
    for i in range(len(number)):
        while idx > 0 and k > 0 and arr[idx - 1] < int(number[i]):
            idx -= 1
            k -= 1

        if idx < result_len:
            arr[idx] = int(number[i])
            idx += 1
            
    for num in arr:
        answer += str(num)

    return answer