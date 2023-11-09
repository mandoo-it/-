from collections import defaultdict

def dfs(start, routes, path):
    while routes[start]:
        dfs(routes[start].pop(0), routes, path)
    path.append(start)
    print(path)

def solution(tickets):
    routes = defaultdict(list)  # 출발지를 key로, 도착지를 값으로 가지는 딕셔너리

    # 티켓을 출발지를 기준으로 정렬하여 그래프 생성
    for start, end in tickets:
        routes[start].append(end)
        routes[start].sort()  # 알파벳 역순으로 정렬
    print(routes)

    path = []  # 경로를 담을 리스트
    dfs("ICN", routes, path)  # DFS 시작

    return path[::-1]  # 경로를 역순으로 반환
