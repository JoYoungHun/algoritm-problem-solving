#https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 1
    while(n != 1) :
        ans += n%2
        n = n//2
    print(ans)
    return ans