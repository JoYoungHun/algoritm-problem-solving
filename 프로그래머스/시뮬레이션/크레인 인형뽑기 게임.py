def solution(board, moves):

    n = len(board)
    box = []
    answer = 0
    for j in moves:

        j = j-1

        for i in range(n) :

            if(board[i][j] != 0):
                box.append(board[i][j])
                board[i][j] = 0
                break

        if(len(box) >= 2 and box[-1] == box[-2]) :
            del box[-1]
            del box[-1]
            answer += 2
    return answer