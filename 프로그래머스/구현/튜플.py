#https://school.programmers.co.kr/learn/courses/30/lessons/64065

s = "{{20,111},{111}}"


def solution(s):
    s = s[1:-1]

    tuple = []
    temps = ''
    templ = []
    switch = 0
    notin = ['{',',','}']
    leng = []
    cnt = 0
    for i in s:
        if (i == '{'):
            switch = 1
        if (switch == 1 and (i not in notin)):
            cnt += 1
            temps += i

        if(switch == 1 and i == ',') :
            templ.append(temps)

            temps = ''
        if (i == '}'):
            templ.append(temps)
            templ = list(map(int,templ))
            tuple.append(templ)
            temps = ''
            templ = []
            leng.append(cnt)
            cnt = 0
            switch = 0

    full = tuple[leng.index(max(leng))]
    answer = []
    while(len(tuple) != 0) :

        for j in tuple[leng.index(min(leng))] :
            if(j in full) :
                answer.append(j)
                full.remove(j)
        del tuple[leng.index(min(leng))]
        leng.remove(min(leng))
    return answer
solution(s)