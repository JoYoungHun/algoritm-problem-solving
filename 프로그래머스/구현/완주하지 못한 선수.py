#https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1) :
        if(participant[i] != completion[i]) :
            return participant[i]
    else :
        return participant[len(participant)-1]