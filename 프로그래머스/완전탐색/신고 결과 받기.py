def solution(id_list, report, k):
    numofid = len(id_list)
    reportid = [[] for roop1 in range(numofid)]
    numofreport = [0] * numofid
    answer = [0] * numofid
    for roop2 in range(len(report)) :
        temp = report[roop2].split()
        if(temp[1] not in reportid[id_list.index(temp[0])]) :
            reportid[id_list.index(temp[0])].append(temp[1])
            numofreport[id_list.index(temp[1])] += 1
    #print(reportid)
    #print(numofreport)
    for roop3 in range(numofid) :
        if(numofreport[roop3] >= k) :
            target = id_list[roop3]
            for roop4 in range(numofid) :
                if(target in reportid[roop4]) :
                    answer[roop4] += 1
    #print(answer)
    return answer

# solution(id_list,report,k)