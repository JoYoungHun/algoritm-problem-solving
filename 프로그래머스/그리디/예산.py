#https://programmers.co.kr/learn/courses/30/lessons/12982
d = [1,3,2,5,4]
budget = 9
def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:

        if(i <= budget) :
            budget = budget - i
            answer += 1
        else :

            return answer

    return answer
solution(d,budget)