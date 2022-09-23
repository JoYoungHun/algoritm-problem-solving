#https://www.acmicpc.net/problem/2839

weight = int(input())

roop = weight//5

anwser = -1
if(weight == 3) :
    anwser = 1
for i in range(roop,-1,-1) :
    # print("roop = " , i)
    # print("weight-5*i" , weight-5*i)
    if((weight-5*i) % 3 == 0) :
        anwser = i + ((weight-5*i)//3)
        break
    if(i == 0 and weight % 3 != 0) :
        break
print(int(anwser))