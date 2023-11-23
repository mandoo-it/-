def solution(progresses, speeds):
    answer = []
    arr = []
    for progress, speed in zip(progresses, speeds) :
        haveTo = 100 - progress
        if int(haveTo % speed) == 0:
            arr.append(int(haveTo/speed))
        else :
            arr.append(int(haveTo/speed) + 1) 

    prev = arr[0]
    count = 1
    
    for i in arr[1:]:
        if i <= prev:
            count += 1
        else:
            answer.append(count)
            prev = i
            count = 1
    answer.append(count)
   
    return answer