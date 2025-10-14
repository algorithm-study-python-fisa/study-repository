# 2진수로 변환하는 코드까지는 작성했습니다... 그 다음은 잘 모르겠어요
def solution(numbers):
    answer = []
    for i in numbers:
        string = binary(i)
        print(string)
    return answer

def binary(num):
    binary_str = ''
    while num > 0 :
        remainder = num % 2
        binary_str = str(remainder) + binary_str
        num = num // 2
    
    return binary_str