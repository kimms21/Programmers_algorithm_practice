# UTF-8
# [풀이 #1] for문 활용
def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        target_num = sorted(array[(i-1):j])[k-1]
        answer.append(target_num)

    return answer

# [풀이 #2] map 활용
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))