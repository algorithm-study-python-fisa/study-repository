# 덱
import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()
for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        d.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        d.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if not d:
            print(-1)
        else:
            print(d.popleft())
    elif cmd[0] == 'pop_back':
        if not d:
            print(-1)
        else:
            print(d.pop())
    elif cmd[0] == 'front':
        if not d:
            print(-1)
        else:
            print(d[0])
    elif cmd[0] == 'back':
        if not d:
            print(-1)
        else:
            print(d[-1])
    elif cmd[0] == 'size':
        print(len(d))
    elif cmd[0] == 'empty':
        if not d:
            print(1)
        else:
            print(0)