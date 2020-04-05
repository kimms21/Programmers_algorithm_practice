from itertools import combinations
from functools import reduce

def solution(clothes):
    
    # 1. dictionary 만들기
    cloth_dict = {}   # cloth_dict[category] := 해당 카테고리에 해당되는 옷들의 리스트 반환 
    for item, category in clothes:
        if category not in cloth_dict.keys():
            cloth_dict[category] = [item]
        else:
            cloth_dict[category].append(item)
    cloth_dict_keys = list(cloth_dict.keys())        
    
    size_list = [len(cloth_dict[key]) for key in cloth_dict.keys()]
    
    # 2. 계산하기
    total_num = 0
    multiple_list = []
    for size in range(1, len(size_list)+1):
        if size == 1:
            total_num += sum(size_list)
        else:
            for combi_i in combinations(size_list, size):
                temp_multiple = reduce(lambda x,y:x*y, combi_i)
                multiple_list.append(temp_multiple)
    total_num += sum(multiple_list)
    
    return total_num