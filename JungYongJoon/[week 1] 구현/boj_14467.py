import sys
sys.stdin = open('input.txt')
n = int(input())
cow_positions = {}
cross_count = 0
# 2중인가?..
for _ in range(n):
  cow, pos = map(int, sys.stdin.readline().split())
  # 소를 처음 보거나 없으면
  if cow not in cow_positions:
    cow_positions[cow] = pos
    # {3 :1 ..}
    # 자리가 바뀌어 있으면 ? { 1 != 0}
  elif cow_positions[cow] != pos:
    cross_count += 1
    # cross_count : 1
    cow_positions[cow] = pos
    #{3:0 (새로운 값으로 덮음)}
print(cross_count)