#https://school.programmers.co.kr/learn/courses/30/lessons/62048
def solution(w,h):
    def GCD(x,y) :
        mx = max(x , y)
        mn = min(x , y)
        if( mx % mn  == 0) :
            return mn
        else :
            return GCD(mn,mx%mn)
    G = GCD(w,h)
    answer = w*h - (((w//G) + (h//G) - GCD(w//G , h//G)) * G)


    return answer