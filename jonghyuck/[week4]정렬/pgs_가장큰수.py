# permutations로 순열 다 만드면 시간초과남.. 정렬로 풀기!
# from itertools import permutations
# def solution(numbers):
#     answer = ''
#     list_numbers = []
#     str_list = []
    
#     list_numbers = list(permutations(numbers, len(numbers)))  
    
#     for i in list_numbers:
#         str_numbers = ''.join(map(str,i))
#         str_list.append(str_numbers)
#     # print(list_numbers)
#     return max(str_list)

class CompareNum(str):
    def __lt__(self, other):
        return self + other > other + self
        
from itertools import permutations
def solution(numbers):
    answer = ''
    str_numbers = list(map(str,numbers))
    str_numbers.sort(key = CompareNum)   
    answer = ''.join(str_numbers)
    
    return str(int(answer))