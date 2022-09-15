#https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    graph = [[] for _1 in range(n+1)]
    visited = [0] * (n+1)
    for op1,op2 in edge :
        graph[op1].append(op2)
        graph[op2].append(op1)
    queue = deque([1])
    visited[1] = 1
    while queue:
        v = queue.popleft()

        for i in graph[v] :
            if(visited[i] == 0) :
                visited[i] = visited[v] + 1
                queue.append(i)
    maxlen = max(visited)
    answer = 0
    for j in visited:
        if(j == maxlen) :
            answer += 1
    return answer