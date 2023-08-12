# 코딩 기초 트레이닝

# 간단한 논리 연산
def solution(x1, x2, x3, x4):
    return bool((x1 + x2) * (x3 + x4))


# 주사위 게임 3
def solution(a, b, c, d):
    score = 0
    if a == b == c == d:
        score += 1111 * a
    elif a == b == c:
        score += (10 * a + d)**2
    elif a == b == d:
        score += (10 * a + c)**2
    elif a == c == d:
        score += (10 * a + b) ** 2
    elif b == c == d:
        score += (10 * b + a) ** 2
    elif a == b and c == d:
        score += (a + c) * abs(a - c)
    elif a == c and b == d:
        score += (a + b) * abs(a - b)
    elif a == d and b == c:
        score += (a + c) * abs(a - c)
    elif a == b:
        score += c * d
    elif a == c:
        score += b * d
    elif a == d:
        score += b * c
    elif b == c:
        score += a * d
    elif b == d:
        score += a * c
    elif c == d:
        score += a * b
    else:
        small = a
        for n in (b, c, d):
            if n < small:
                small = n
        score += small
    return score


# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = []
    my_string = list(my_string)
    for index in index_list:
        answer.append(my_string[index])
    return ''.join(answer)


# 9로 나눈 나머지
def solution(number):
    num_sum = 0
    for n in number:
        num_sum += int(n)
    return num_sum % 9


# 문자열 여러 번 뒤집기
def solution(my_string, queries):
    my = list(my_string)
    for q in queries:
        temp = my[q[0]:q[1]+1]
        temp = temp[::-1]
        for idx, s in enumerate(range(q[0], q[1]+1)):
            my[s] = temp[idx]
    return ''.join(my)
# enumerate
# 반복 가능한 객체를 받아 해당 객체의 각 요소와 해당 요소의 인덱스를 함께 반환
# (인덱스, 요소) 형태로 반환
# 반복문에서 현재 아이템의 값을 사용하면서 동시에 그 아이템의 인덱스도 사용할 수 있어서 유용함.
