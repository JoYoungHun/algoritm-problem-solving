#https://programmers.co.kr/learn/courses/30/lessons/12979

N = 11
stations = [4,11]
w = 1

def solution(n, stations, w):

    answer = 0

    temp = stations[0]

    if(temp-1-w > 0) :
        if((temp-1-w) % (2*w+1) != 0) :
            answer += (temp-1-w) // (2*w+1) +1
        else :
            (temp-1-w) // (2*w+1)
        del stations[0]


    for i in stations:

        if((temp-1)+w < i-1-w ) :
            if (((i-1-w)-(temp-1+w)-1) % (2 * w + 1) != 0):
                answer += ((i-1-w)-(temp-1+w)-1) // (2 * w + 1) +1
            else :
                answer += ((i-1-w)-(temp-1+w)-1) // (2 * w + 1)
        temp = i

    if(temp-1+w < n-1) :
        if(((n-1)-(temp-1+w)) % (2*w+1) != 0) :

            answer += ((n-1)-(temp-1+w)) // (2*w+1) + 1
        else :
            answer += ((n - 1) - (temp - 1 + w)) // (2 * w + 1)
    print(answer)
    return answer








solution(N, stations, w)