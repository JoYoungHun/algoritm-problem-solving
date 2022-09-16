#https://programmers.co.kr/learn/courses/30/lessons/72410
new_id = "...!@BaT#*..y.abcdefghijklm"
def solution(new_id):
    answer = new_id.lower()
    canuse = '_.-abcdefghijklmnopqrstuvwxyz1234567890'
    for i in answer:
        if(i not in canuse) :
            answer = answer.replace(i,"")
    while('..' in answer):
        answer = answer.replace('..','.')

    if(len(answer) != 0 and answer[0] == '.'):
        answer = answer[1:]
    #
    if(len(answer) != 0 and answer[-1] == '.'):
        answer = answer[:-1]

    if(len(answer) == 0) :
        return 'aaa'
    else :
        if(len(answer) >= 16) :
            answer = answer[0:15]

        if(len(answer) != 0 and answer[0] == '.'):
            answer = answer[1:]
        #
        if(len(answer) != 0 and answer[-1] == '.'):
            answer = answer[:-1]
        if(len(answer) == 1) :
            return answer+answer+answer
        if(len(answer) == 2) :
            return answer + answer[-1]
        print(answer)
    return answer
solution(new_id)