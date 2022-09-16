#https://programmers.co.kr/learn/courses/30/lessons/49993
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA","RTSKFV"]
def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in range(len(skill_trees)) :
        skills = list(skill)
        for j in skill_trees[i]:
            if(j in skill) :
                if(j != skills.pop(0)) :
                    answer -= 1
                    break

    print(answer)
    return answer
solution(skill,skill_trees)