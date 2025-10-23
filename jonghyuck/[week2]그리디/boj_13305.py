# 주유소
# 메모이제이션
N = int(input())
length_list = []
cost_list = []

sum = 0

length_list = list(map(int, input().split()))

cost_list = list(map(int, input().split()))

min_cost = cost_list[0]

remain_length = 0

for i in range(len(length_list)):
    if cost_list[i] < min_cost:
        sum = sum + cost_list[i] * length_list[i]
        min_cost = cost_list[i]
    else :
        sum = sum + min_cost * length_list[i]
print(sum)
