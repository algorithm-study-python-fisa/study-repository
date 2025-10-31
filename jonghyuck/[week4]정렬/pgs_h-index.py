def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    h_index = 0
    # if len(citations) % 2 == 0:
    #     answer = citations[len(citations)//2+1]
    # else :
    #     answer = citations[len(citations) // 2]
    
    # 내림차순으로 정렬하고, 피인용 수가 인덱스보다 작아질때 i를 구하면 된다.
    for i in range(len(citations)):
        
        if citations[i] < i + 1:
            answer = i
            break
        else :
            answer = len(citations)
        
        
        
    return answer