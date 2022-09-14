#https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
def solution(nums):
    answer = 0
    list1 = (list(combinations(nums,3)))
    for i in list1 :
        sumi = sum(i)
        # print("sumi = " , sumi)
        for j in range(2,sumi//2+1) :
            # print(j)
            if(sumi%j == 0) :
                break
            if(j*j > sumi) :
                answer +=1
                break
    # print("answer = " , answer)
    return answer