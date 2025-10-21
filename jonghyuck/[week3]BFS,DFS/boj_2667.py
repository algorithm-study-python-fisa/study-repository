from collections import deque

N = int(input())

array = []

for _ in range(N):
    row = list(map(int, input()))
    array.append(row)


def bfs(x, y):
    dx = (0, 0, -1, 1)
    dy = (1, -1, 0, 0)


    queue = deque([(x, y)])

    array[x][y] = 0


    house_count = 0

    while queue:
        current_x, current_y = queue.popleft()
        house_count += 1
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if array[nx][ny] == 1:
                    array[nx][ny] = 0
                    queue.append((nx, ny))
    return house_count

total = 0

nums_list = []

for x in range(N):
    for y in range(N):
        if array[x][y] == 1:
            nums_list.append(bfs(x, y))
            total += 1


print(total)
for x in sorted(nums_list):
    print(x)

