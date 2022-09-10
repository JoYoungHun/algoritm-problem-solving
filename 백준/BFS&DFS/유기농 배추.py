#https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10000)

def dfs(x,y) :
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited[y][x] = 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<= nx <= m-1 and 0<= ny <= n-1 and visited[ny][nx] == 0 and array[ny][nx] == 1) :
            visited[ny][nx] = 1
            dfs(nx,ny)

t = int(sys.stdin.readline())
for testcase in range(t) :
    cnt = 0
    m,n,k =map(int,sys.stdin.readline().split())
    #print(m,n,k)
    array = [[0 for _ in range(m)] for _1 in range(n)]
    visited = [[0 for v1 in range(m)] for v2 in range(n)]

    for _2 in range(0,k) :
        x,y = map(int,sys.stdin.readline().split())
        array[y][x] = 1

    for a in range(n) :
        for b in range(m) :

            if(array[a][b] == 1 and visited[a][b] == 0) :
                dfs(b,a)

                cnt += 1
    print(cnt)
