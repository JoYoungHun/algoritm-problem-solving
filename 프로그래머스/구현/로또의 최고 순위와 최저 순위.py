#https://programmers.co.kr/learn/courses/30/lessons/77484
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
def solution(lottos, win_nums):
    answer = [0,0]
    collect = [0,0]
    for roop1 in range(6) :
        if(win_nums[roop1] in lottos) :
            collect[0] += 1
            collect[1] += 1
        if(lottos[roop1] == 0) :
            collect[0] += 1
    print(collect)
    for roop2 in range(2) :
        if(7 - collect[roop2] <= 5) :
            answer[roop2] = 7 - collect[roop2]
        else :
            answer[roop2] = 6
    print(answer)
    return answer




solution(lottos , win_nums)