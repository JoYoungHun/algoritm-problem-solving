#https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    eng = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for i in eng:
        if i in s:
            s = s.replace(i,str(eng.index(i)))
    return int(s)

solution("one4seveneight")