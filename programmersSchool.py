# 코딩 기초 트레이닝

# 배열 만들기 5
def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        temp = int(num[s:s+l])
        if temp > k:
            answer.append(temp)
    return answer


# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        answer = answer + my_strings[i][parts[i][0]:parts[i][1]+1]
    return answer


# 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[len(my_string)-n:]


# 접미사 배열
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    return sorted(answer)


# 접미사인지 확인하기
def solution(my_string, is_suffix):
    jub = list()
    for i in range(len(my_string)):
        jub.append(my_string[i:])
    if is_suffix in jub:
        return 1
    return 0
