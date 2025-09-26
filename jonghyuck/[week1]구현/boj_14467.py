# 소가 길을 건너간 이유 1
# 2중 반복문..? => N<=100이라 될거같긴한데.. 좋은 방법은 아닌듯
# 그러면 메모이제이션으로 풀어야하지 않을까.. 위치 저장하면서
# 크기만큼 배열 만든 후, 해당 배열 인덱스로 비교

N = int(input())

cow_arr = []
count = 0
memo_arr = [-1] * (N+1)

for i in range(N):
    cow, location = map(int,input().split())

    if memo_arr[cow] == -1:
        memo_arr[cow] = location
        
    else :
        if memo_arr[cow] != location :
            count += 1
            memo_arr[cow] = location

print(count)

# for i in range(N):
#     if memo_arr[cow] == -1
    
# for i in range(N):
#     for j in range(N):
#         if cow_arr[i][0] == cow_arr[j][0] :
#             if cow_arr[i][1] != cow_arr[j][1] :
#                 count += 1
#                 break
            
            
    
    