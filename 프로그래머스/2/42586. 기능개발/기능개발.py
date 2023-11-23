def solution(progresses, speeds):
    answer = []
    arr = []
    for progress, speed in zip(progresses, speeds) :
        haveTo = 100 - progress
        if int(haveTo % speed) == 0:
            arr.append(int(haveTo/speed))
        else :
            arr.append(int(haveTo/speed) + 1) 

    cnt = 1
    prev_day = arr[0]

    for day in arr[1:]:
        if prev_day >= day:  # 이전 작업보다 현재 작업이 오래 걸릴 경우
            cnt += 1
        else:  # 현재 작업이 더 빨리 완료될 경우
            answer.append(cnt)
            cnt = 1
            prev_day = day

    answer.append(cnt)  # 마지막 작업 배포
   
    return answer