from collections import deque
            
    
def solution(begin, target, words):
    
    transitable = lambda a, b: (sum([1 if x != y else 0 for x,y in zip(a, b)]) == 1)
    
    q, d = deque(), dict()
    
    d[begin] = [w for w in words if transitable(begin, w)]
    for w in words:
        d[w] = [x for x in words if transitable(x, w)]
    
    q.append((begin, 0))  # node, level
    
    while q:
        current_node, level = q.popleft()
        if level > len(words):
            return 0
        for child_i in d[current_node]:
            if child_i == target:
                return level+1
            else:
                q.append((child_i, level+1))
                
    return 0