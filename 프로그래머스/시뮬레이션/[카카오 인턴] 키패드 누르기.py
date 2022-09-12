#https://programmers.co.kr/learn/courses/30/lessons/67256

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

def solution(numbers , hand) :
    loc = {1:(1,1),2:(2,1),3:(3,1),4:(1,2),5:(2,2),6:(3,2),7:(1,3),8:(2,3),9:(3,3),0:(2,4)}
    l = [1,4,7]
    r = [3,6,9]
    rh = (3,4)
    lh = (1,4)
    answer = ''
    for i in numbers :
        if(i in l) :
            answer += 'L'
            lh = loc[i]
        elif(i in r) :
            answer += 'R'
            rh = loc[i]
        else :

            if(hand == 'right') :
                if( abs(rh[0] - loc[i][0]) + abs(rh[1] - loc[i][1]) <= abs(lh[0] - loc[i][0]) + abs(lh[1] - loc[i][1]) ) :
                    answer += 'R'
                    rh = loc[i]
                else :
                    answer += 'L'
                    lh = loc[i]
            else :
                if( abs(rh[0] - loc[i][0]) + abs(rh[1] - loc[i][1]) >= abs(lh[0] - loc[i][0]) + abs(lh[1] - loc[i][1]) ) :
                    answer += 'L'
                    lh = loc[i]
                else :
                    rh = loc[i]
                    answer += 'R'

    return answer

solution(numbers , hand)