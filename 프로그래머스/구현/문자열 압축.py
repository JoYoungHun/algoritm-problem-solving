#https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer_list = []
    for step in range(1, len(s)//2+1):
        count = 1
        count_list = []
        for i in range(len(s)//step):
            if s[i*step : (i+1)*step] == s[(i+1)*step : (i+2)*step]:
                count += 1
            else:
                if count != 1: count_list.append(count)
                count = 1
        answer_list.append(len(s) - step*sum(map(lambda x: x-1, count_list)) + sum(map(lambda x: len(str(x)), count_list)))
    return min(answer_list) if answer_list else 1

