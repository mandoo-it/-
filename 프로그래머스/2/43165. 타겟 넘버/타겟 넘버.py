def solution(numbers, target):
    answer = [0] 
    
    for i in numbers:
        temp = []
        for item in answer : 
            temp.append(item + i)
            temp.append(item - i)
        answer = temp
    return answer.count(target)