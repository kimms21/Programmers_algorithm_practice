global answer

def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if (idx == N and target==value):
        answer += 1
        return
    if idx == N:
        return
    
    DFS(idx+1, numbers, target, value-numbers[idx])
    DFS(idx+1, numbers, target, value+numbers[idx])

def solution(numbers, target):
    global answer
    answer = 0
    
    DFS(0, numbers, target, 0)
    
    return answer