def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget > 0:
            budget = budget - i
            if budget >= 0:
                answer += 1
            else :
                break
        
    return answer