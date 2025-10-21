# 유기농 배추(BFS 풀이)

from collections import deque

def bfs(field, visited, y, x, M, N):
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque([(y, x)])

    visited[y][x] = True
    while queue:
        # 현재 y, x를 최신화
        current_y, current_x = queue.popleft()
        for i in range(4):
            ny = current_y + dy[i]
            nx = current_x + dx[i]
            # field의 범위를 넘지 않으며
            if 0 <= nx < M and 0 <= ny < N:
                # 양배추가 있고, 방문하지 않았다면
                if field[ny][nx] == 1 and not visited[ny][nx]:
                    # True 할당
                    visited[ny][nx] = True
                    # 해당 좌표 queue에 append
                    queue.append((ny,nx))


# Test Case 입력 부

case = int(input())

for i in range(case):
    
    M, N, K = map(int, input().split())
    
    cabbage_array = []
    
    # 양배추 있는 배열 받는 부분
    for _ in range(K):

        row = list(map(int, input().split()))
        
        cabbage_array.append(row)

    # 0으로 초기화

    field = [[0] * M for _ in range(N)]

    # False로 방문 배열 초기화
    visited = [[False] * M for _ in range(N)]

    # 양배추 있는 배열만 1로
    for x, y in cabbage_array:
        field[y][x] = 1    

    # 배열하지 않은 배열 False로 채우고, 방문한 배열 1


    # 정의된 bfs로 M,N과 입력된 
    # 배추흰지렁이 count
    count = 0

    for y in range(N):
        for x in range(M):
            if field[y][x] and not visited[y][x]:
                count += 1
                bfs(field, visited, y, x, M, N)

    print(count)
    
