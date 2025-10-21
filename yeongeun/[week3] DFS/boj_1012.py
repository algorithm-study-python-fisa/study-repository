# 유기농 배추
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# DFS 함수 정의
def dfs(x, y):
    visited[y][x] = True # 방문 처리
    # 상하좌우 방향 탐색
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 밭 범위 안인지 확인
        if 0 <= nx < M and 0 <= ny < N:
            # 배추가 있고 방문 안 했으면 재귀 호출
            if field[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

# 테스트 케이스 수 입력
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 개수

    # 배추밭 초기화 (0으로 채움)
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    # 배추 위치 입력받아 표시
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    worm_count = 0  # 필요한 지렁이 수

    # 모든 좌표 확인
    for y in range(N):
        for x in range(M):
            # 배추 있고 방문 안 했다면 DFS 수행 후 지렁이 수 증가
            if field[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                worm_count += 1

    print(worm_count)