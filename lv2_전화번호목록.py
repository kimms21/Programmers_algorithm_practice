# [풀이 #1] 정렬 활용
def solution(phone_book):
    # 문자 길이 순으로 오름차순 정렬
    phone_book = sorted(phone_book, key=lambda x:len(x))
    
    answer = True
    for i in range(len(phone_book)):
        base_str = phone_book[i]
        check_list = phone_book[(i+1):]
        for check in check_list:
            if check[:len(base_str)] == base_str:
                answer = False
                break
        if answer == False:
            break

    return answer


# [풀이 #2] .startswith()
def solution(phone_book):
    
    phone_book = sorted(phone_book)
    
    for i in range(len(phone_book)):
        base_str = phone_book[i]
        check_list = phone_book[(i+1):]
        for check in check_list:
            if check.startswith(base_str):
                return False
    return True