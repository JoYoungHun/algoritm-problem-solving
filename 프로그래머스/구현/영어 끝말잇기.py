#https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    length = len(words)
    passed = []
    passed.append(words[0])
    cnt = 1
    for roop1 in range(1,length) :
        cnt += 1
        if(words[roop1] in passed or words[roop1][:1] != passed[len(passed)-1].strip()[-1]) :
            break
        passed.append(words[roop1])
    #print(cnt)
    if(cnt % n == 0) :
        if(len(passed) == length) :
            return [0,0]
        else :
            return [n,cnt//n]
    else :
        return [cnt % n , cnt//n+1]