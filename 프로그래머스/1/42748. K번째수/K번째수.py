def solution(array, commands):
    answer = []
    for item in commands:
        arr = array[item[0] -1 : item[1]]
        arr.sort()
        answer.append(arr[item[2]-1])
    return answer