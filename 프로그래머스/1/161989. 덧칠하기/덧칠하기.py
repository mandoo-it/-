def solution(n, m, section):
    answer, current = 0, 0
    
    for s in section:
        if s >= current:
            current = m + s
            answer += 1
            # print(current , answer)
    return answer