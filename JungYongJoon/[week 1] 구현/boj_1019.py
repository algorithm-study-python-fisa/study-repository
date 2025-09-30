import sys

sys.stdin = open('input.txt', 'r')

stack = []
cnt = 0
answer = 0
cnt1 = 0
cnt2 = 0
n, m = map(int, input().split())  # 26, 5 입력 받음
arr = [input().strip() for _ in range(n)]

for i in range(n):

        # Wkr tn ldaus
    # if (m % 2 == 0):
    if(len(set(arr[i])) == 1):
        cnt2 = m // 2
    elif (arr[i].count("W") != arr[i].count("B")):
        cnt1 = max(arr[i].count("W"), arr[i].count("B")) - m // 2
  

answer += (cnt1 + cnt2)




# 한 줄 한 줄 검사를 해야 할 거 같은데




print(answer)

# import sys

# sys.stdin = open('input.txt', 'r')

# n, m = map(int, input().split())  # 26, 5 입력 받음
# arr = [input().strip() for _ in range(n)]

# chess = dict()

# # chess[arr]
# for i in range(n):
#     chess["W"] = arr[i].count("W")
#     chess["B"] = arr[i].count("B")
#     if(m % 2 == 0 ):
#         if(chess[])

#     print(chess)



