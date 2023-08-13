# 코딩 기초 트레이닝

# 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]


# 접두사인지 확인하기
def solution(my_string, is_prefix):
    jub = list()
    for i in range(len(my_string)):
        jub.append(my_string[:i])
    if is_prefix in jub:
        return 1
    return 0


# 문자열 뒤집기
def solution(my_string, s, e):
    my_string = list(my_string)
    temp = my_string[s:e+1]
    for idx, w in enumerate(temp[::-1]):
        my_string[s+idx] = w
    return ''.join(my_string)


# 세로 읽기
def solution(my_string, m, c):
    return my_string[c-1::m]


# qr code
def solution(q, r, code):
    code = list(code)
    answer = []
    for i in range(len(code)):
        if i % q == r:
            answer.append(code[i])
    return ''.join(answer)

