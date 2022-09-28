#https://programmers.co.kr/learn/courses/30/lessons/49994
dirs = "ULURRDLLU"
def solution(dirs):
    answer = 0
    log = []
    cur = [5,5]
    for i in dirs:
        pre = cur.copy()

        if(i == 'L') : #LEFT
            cur[0] = cur[0] - 1
        elif (i == 'R'): #RIGHT
            cur[0] = cur[0] + 1
        elif (i == 'U'): #UP
            cur[1] = cur[1] + 1
        else: #DOWN
            cur[1] = cur[1] - 1


        if (0 <= cur[0] <= 10 and 0 <= cur[1] <= 10):
            if not([pre,cur] in log) :
                log.append([pre.copy(),cur.copy()])
                log.append([cur.copy(),pre.copy()])
                answer += 1
                # print("log = " , log)

        else :
            cur = pre.copy()
    print(answer)
    return answer
solution(dirs)