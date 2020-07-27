

def solution(board, moves):
    result = 0
    res_list = []
    ### start point 찾기
    visited = [0] * len(board)
    is_end = True
    while is_end:
        # moves 배열이 0이 될 때까지

        if len(moves) == 0:
            is_end = False
            break
        else:
            ### moves의 앞에서부터 순서대로 채우는건데 인덱스-1로 포착해야함

            col_index = moves.pop(0) - 1
            max_depth = len(board)


            is_end2 = True
            ## 마지막에 어디지점까지 갔는지 넣어야함
            row_index = visited[col_index]

            while is_end2 :
                ##끝나는 시점은 집게 집거나 끝까지 같으면 끝내기
                if row_index == max_depth:
                    is_end2 = False
                    break

                elif board[row_index][col_index] == 0 :
                    row_index += 1
                    if row_index == max_depth:
                        is_end2 = False
                        break

                else :
                    res_list.append(board[row_index][col_index])
                    board[row_index][col_index] = 0
                    #start지점을 미리 정해줌
                    visited[col_index] = row_index + 1
                    if len(res_list) > 1:
                        if res_list[len(res_list)-1] == res_list[len(res_list)-2]:
                            del res_list[len(res_list)-2:len(res_list)]
                            result += 1
                            is_end2 = False
                            break
                        else :
                            is_end2 = False
                            break


                    else :
                        is_end2 = False
                        break

    return result


arr = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
res_ = [1,5,3,5,1,2,1,4]

print(solution(arr,res_))