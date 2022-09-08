#https://programmers.co.kr/learn/courses/30/lessons/12978

from collections import deque

def solution(N, road, K):

    visited = [0] * (N + 1)
    costgraph = {}
    alreadysum = [0] * (N+1)
    graph = [[] for opt in range(N+1)]
    for roop1 in road :
        if(roop1[1] not in graph[roop1[0]]) :
            costgraph[roop1[0],roop1[1]] = roop1[2]
            costgraph[roop1[1],roop1[0]] = roop1[2]
            graph[roop1[0]].append(roop1[1])
            graph[roop1[1]].append(roop1[0])
        else:
            costgraph[roop1[0], roop1[1]] = min(costgraph[roop1[0], roop1[1]], roop1[2])
            costgraph[roop1[1], roop1[0]] = min(costgraph[roop1[1], roop1[0]], roop1[2])

    print(graph)
    print(costgraph)
    q = deque([1])
    visited[1] = 1
    alreadysum[1] = 1
    answer = 1
    while q :
        v = q.popleft()
        # print("v",v)
        for i in graph[v] :
            # print("i = ",i)
            if(visited[i] == 0) :
                # print("cost = ",costgraph[v,i])
                visited[i] = visited[v] + costgraph[v,i]

                q.append(i)

            else :
                if(visited[i] >  visited[v] + costgraph[v,i]) :
                    visited[i] = visited[v] + costgraph[v,i]
                    q.append(i)
            if (visited[i] - 1 <= K and alreadysum[i] == 0):
                answer += 1
                alreadysum[i] = 1

    return answer