#https://programmers.co.kr/learn/courses/30/lessons/12987

A = [5,1,3,7]
B = [2,2,6,8]

def solution(a, b):
    answer = 0
    a.sort()
    b.sort()
    for i in b :
        if(i > a[0]) :
            answer += 1
            del a[0]

    return answer