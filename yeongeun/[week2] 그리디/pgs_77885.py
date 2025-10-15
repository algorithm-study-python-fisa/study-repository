# 2개 이하로 다른 비트

def solution(numbers):
    answer = []
    for x in numbers:
        if x % 2 == 0:
            answer.append(x + 1)
        else:
            bits = list('0' + bin(x)[2:])
            idx = ''.join(bits).rfind('0')
            bits[idx] = '1'
            bits[idx + 1] = '0'
            min_num = int(''.join(bits), 2)
            answer.append(min_num)
    return answer