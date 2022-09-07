# https://programmers.co.kr/learn/courses/30/lessons/12971
sticker = [14, 6, 5, 11, 3, 9, 2, 10]


def solution(sticker) :
    n = len(sticker)
    # stend = [n-1,0]
    sumside = []
    sumall = sum(sticker)
    for i in range(n):
        if(0 < i < n-1) :
            sumside.append(sticker[i-1]+sticker[i+1])
        elif(i==0) :
            sumside.append(sticker[n-1]+sticker[1])
        else :
            sumside.append(sticker[n-2] + sticker[0])
    while(sum(sumside) != 201*n) :
        # print(sumside)
        lowval = min(sumside)
        lowindex = sumside.index(lowval)

        sumall -= lowval
        # print(sumall)
        if(1< lowindex < n-2) :
            sumside[lowindex-1] = 201
            sumside[lowindex] = 201
            sumside[lowindex+1] = 201
            if(sumside[lowindex-2] != 201) :
                sumside[lowindex-2] = sumside[lowindex-2]-sticker[lowindex-1]
            if (sumside[lowindex + 2] != 201):
                sumside[lowindex +2] = sumside[lowindex + 2] - sticker[lowindex + 1]

        elif(lowindex <= 1) :
            if(lowindex == 1) :
                sumside[lowindex - 1] = 201
                sumside[lowindex] = 201
                sumside[lowindex + 1] = 201
                if (sumside[n-1] != 201):
                    sumside[n-1] = sumside[n-1] - sticker[0]
                # if (sumside[lowindex + 2] != 201):
                #     sumside[lowindex + 2] = sumside[lowindex + 2] - sticker[lowindex + 1]
            else :
                sumside[n-1] = 201
                sumside[lowindex] = 201
                sumside[lowindex + 1] = 201
                if (sumside[n-2] != 201):
                    sumside[n-2] = sumside[n-2] - sticker[n-1]
            if (sumside[lowindex + 2] != 201):
                sumside[lowindex + 2] = sumside[lowindex + 2] - sticker[lowindex + 1]
        else :
            if (lowindex == n-2):
                sumside[lowindex - 1] = 201
                sumside[lowindex] = 201
                sumside[lowindex + 1] = 201
                if (sumside[0] != 201):
                    sumside[0] = sumside[0] - sticker[n-1]
            else :
                sumside[lowindex - 1] = 201
                sumside[lowindex] = 201
                sumside[0] = 201
                if (sumside[1] != 201):
                    sumside[1] = sumside[1] - sticker[0]
            if (sumside[lowindex - 2] != 201):
                sumside[lowindex - 2] = sumside[lowindex - 2] - sticker[lowindex - 1]


    return sumall
solution(sticker)