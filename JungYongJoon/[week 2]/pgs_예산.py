def solution(d, budget):
    d.sort()
    answer = 0
    total = 0 
    for i in range(len(d)):
        if(total + d[i] <= budget):
            total += d[i]
            answer += 1
        else :
            break
    return answer
        