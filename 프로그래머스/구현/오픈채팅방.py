#https://programmers.co.kr/learn/courses/30/lessons/42888

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    length = len(record)
    # log = [['0' for ans in range(3)] for ans2 in range(length)]
    log = [[] for ans in range(length)]
    userid = {}
    for roop1 in range(length) :
        temp = record[roop1].split()
        log[roop1] = temp
        if(log[roop1][0] == 'Enter') :
            userid[log[roop1][1]] = log[roop1][2]
            log[roop1][0] = '들어왔습니다.'
        elif(log[roop1][0] == 'Change') :
            userid[log[roop1][1]] = log[roop1][2]
            # del log[roop1]
        else :
            log[roop1][0] = '나갔습니다.'

    answer = []
    # print(userid[log[0][1]])
    # print(log[0][0])
    for roop2 in range(len(log)) :
        if(log[roop2][0] != 'Change') :
            answer.append('%s님이 %s'%(userid[log[roop2][1]],log[roop2][0]))
    #print(answer)



    return answer

solution(record)