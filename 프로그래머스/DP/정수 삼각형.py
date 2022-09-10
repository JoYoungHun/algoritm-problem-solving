#https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    n = len(triangle)
    d = [[0 for op1 in range(n+1)] for op2 in range(n+1)]
    d[1][0] = triangle[0][0]

    d[2][0] = d[1][0] + triangle[1][0]
    d[2][1] = d[1][0] + triangle[1][1]

    for i in range(3,n+1) :
        for j in range(i) :
            if(j == 0) :
                d[i][j] = (d[i-1][0]+triangle[i-1][0])
            elif(j == (i-1)) :

                d[i][j] = (d[i-1][j-1]+triangle[i-1][j])
            else :
                d[i][j] = (max(d[i-1][j-1]+triangle[i-1][j],d[i-1][j]+triangle[i-1][j]))
    return max(d[n])