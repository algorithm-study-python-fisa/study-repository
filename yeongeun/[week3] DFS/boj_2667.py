# 단지 번호 붙이기
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 상, 하, 좌, 우 방향
directions = [(0,1), (0,-1), (1,0), (-1,0)]

# DFS 함수 정의
def dfs(x, y):
    visited[y][x] = True
    count = 1 # 현재 집 1개 카운트
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 지도 범위 안이고, 집이 있으며, 아직 방문하지 않았다면 탐색
        if 0 <= nx < N and 0 <= ny < N:
            if field[ny][nx] == 1 and not visited[ny][nx]:
                count += dfs(nx, ny)
    return count

# 지도 크기 입력
N = int(input().strip())
field = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

complex_counts = [] # 각 단지별 집 수 저장

# 전체 지도 탐색
for y in range(N):
    for x in range(N):
        if field[y][x] == 1 and not visited[y][x]:
            # 새로운 단지를 발견하면 DFS 수행
            house_count = dfs(x, y)
            complex_counts.append(house_count)

# 결과 출력
complex_counts.sort()
print(len(complex_counts))
for cnt in complex_counts:
    print(cnt)