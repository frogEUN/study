# 코딩 기초 트레이닝

# 코드 처리하기
def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = 1
            else:
                if i % 2 == 0:
                    ret = ret + code[i]
        else:
            if code[i] == '1':
                mode = 0
            else:
                if i % 2 == 1:
                    ret = ret + code[i]
    if len(ret) == 0:
        return "EMPTY"
    return ret


# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a + i * d
    return answer


# 주사위 게임 2
def solution(a, b, c):
    answer = 0
    if a != b and b != c and a != c:
        answer += a + b + c
    elif a == b and b == c:
        answer += (a+b+c)*(a*a+b*b+c*c)*(a**3+b**3+c**3)
    elif a == b or b == c or a == c:
        answer += (a+b+c)*(a*a+b*b+c*c)
    return answer


# 원소들의 곱과 합
def solution(num_list):
    a = 1
    b = 0
    for num in num_list:
        a *= num
        b += num
    b = b*b
    if a < b:
        return 1
    else:
        return 0


# 이어 붙인 수
def solution(num_list):
    even = ''
    odd = ''
    for num in num_list:
        if num % 2 == 0:
            even = even + str(num)
        else:
            odd = odd + str(num)
    return int(even) + int(odd)
