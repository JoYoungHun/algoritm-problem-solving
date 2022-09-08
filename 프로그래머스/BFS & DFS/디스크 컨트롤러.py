#https://programmers.co.kr/learn/courses/30/lessons/42627

from collections import deque
def solution(jobs):
    n = len(jobs)
    jobs.sort(key= lambda x:(x[0],x[1]))
    queue = deque([jobs[0]])
    curr = jobs[0][0]
    jobs.pop(0)
    answer = 0
    while queue:
        start , take = queue.popleft()
        end = curr + take
        answer += end - start
        curr = end
        minj = 1001
        for i,j in jobs:
            if(i>curr) :
                break
            else :
                if(minj > j) :
                    minj = j
                    temp = [i,j]
        if(len(jobs) != 0) :
            if(minj == 1001) :
                st , ta = jobs.pop(0)

                queue.append([st,ta])
                curr = st
            else:
                queue.append(temp)
                jobs.remove(temp)
        else:
            continue
    return (int(answer/n))