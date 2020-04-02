# [풀이-1] 정렬 활용
# 파이썬 내장 sort : timsort
# 최악의 경우 O(n logn), 평균 O(n)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = None
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer is None:
        answer = participant[-1]
    
    return answer


# [풀이-2] - Counter 활용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
