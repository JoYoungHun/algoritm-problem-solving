#https://school.programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines) :
    n = len(lines)
    log = [[0 for _ in range(2)] for _2 in range(n)]

    traffic = []
    for i in range(n):
        time = int(float(lines[i].split()[2].replace('s','')) * 1000)
        hours = int(lines[i].split()[1][0:2]) * 60**2 * 1000
        mins = int(lines[i].split()[1][3:5]) * 60 * 1000
        secs = int(float(lines[i].split()[1][6:12]) * 1000 )
        log[i][0] = hours + mins + secs - time + 1
        log[i][1] = hours + mins + secs
    for j in log :
        cnt = 0
        cnt2 = 0
        start = j[0] - 999
        end = j[0]
        start2 = j[1]
        end2 = j[1] + 999
        for k in log :
            if(start <= k[1] and end >= k[0]) :
                cnt += 1
            if(start2 <= k[1] and end2 >= k[0]) :
                cnt2 += 1
        traffic.append(cnt)
        traffic.append(cnt2)
    return max(traffic)