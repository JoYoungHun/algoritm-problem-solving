#https://school.programmers.co.kr/learn/courses/30/lessons/77886

s = ["100111100"]

def solution(s):
    answer = []

    for i in s:
        templist = []
        cnt = 0
        for k in i:
            if(len(templist) >= 2 and k == '0' and templist[-1] == '1' and templist[-2] == '1') :
                templist.pop()
                templist.pop()
                cnt += 1
            else :
                templist.append(k)

        cnt1 = 0
        for j in templist[::-1] :
            if(j == '0') :
                break
            else :

                cnt1 += 1

        answer.append(''.join(templist[:len(templist)-cnt1])+'110'*cnt+'1'*cnt1)
    return (answer)



solution(s)