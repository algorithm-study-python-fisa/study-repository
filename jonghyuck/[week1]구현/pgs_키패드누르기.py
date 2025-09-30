def solution(numbers, hand):
    keypad = {
        1 : [0,0], 2 : [0,1], 3 : [0,2],
        4 : [1,0], 5 : [1,1], 6 : [1,2],
        7 : [2,0], 8 : [2,1], 9 : [2,2],
        '*': [3,0], 0 : [3,1], '#': [3,2]
    }
    answer = ''
    lefthand = keypad['*']
    righthand = keypad['#']
    
    for i in numbers:
        if(i in [1,4,7]):
            answer += 'L'
            lefthand = keypad[i]
        elif(i in [3,6,9]):
            answer += 'R'
            righthand = keypad[i]
        else :
            # 왼엄지에서 2,5,8,0 까지의 거리
            left_distance = abs(keypad[i][0] - lefthand[0]) + abs(keypad[i][1] - lefthand[1])
            # 오른엄지에서 2,5,8,0 까지의 거리
            right_distance = abs(keypad[i][0] - righthand[0]) + abs(keypad[i][1] - righthand[1])
            if (left_distance - right_distance)>0:
                answer += 'R'
                righthand = keypad[i]
            elif left_distance - right_distance<0:
                answer += 'L'
                lefthand = keypad[i]
            else :
                if hand == 'right':
                    answer += 'R'
                    righthand = keypad[i]
                else :
                    answer += 'L'
                    lefthand = keypad[i]
                
    return answer