#https://www.acmicpc.net/problem/1110

N = str(input())
a = []
b = []
c = 0
if(int(N) >= 10 ) :
    a = list(N)
else :
    a.append(0)
    a.append(int(N))
b.append(a[0])
b.append(a[1])
count = 0
while(1) :
    x = int(b[1]) + int(b[0])
    c = int(b[1])
    if ( x >= 10 ) :
        b =[]
        b = list(str(x))
    else :
        b = []
        b.append(0)
        b.append(x)
    b[0] = c
    b[1] = str(b[1])
    count += 1
    if ( int(a[0]) == int(b[0]) and int(a[1]) == int(b[1]) ) :
        break

print(count)