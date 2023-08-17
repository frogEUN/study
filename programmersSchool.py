# 코딩 기초 트레이닝

# x 사이의 개수
def solution(myString):
    answer = myString.split('x')
    result = list()
    for a in answer:
        result.append(len(a))
    return result


# 문자열 잘라서 정렬하기
def solution(myString):
    myString = myString.strip('x')
    answer = myString.split('x')
    answer = [a.strip('x') for a in answer if a.strip('x') != '']
    answer.sort()
    return answer


# 간단한 식 계산하기
def solution(binomial):
    temp = binomial.split()
    a = int(temp[0])
    op = temp[1]
    b = int(temp[2])
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b


# 문자열 바꿔서 찾기
def solution(myString, pat):
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == "A":
            myString[i] = "B"
        else:
            myString[i] = "A"
    myString = ''.join(myString)
    temp = myString.find(pat)
    if temp == -1:
        return 0
    return 1


# rny_string
def solution(rny_string):
    my = list(rny_string)
    for i in range(len(my)):
        if my[i] == "m":
            my[i] = "rn"
    return ''.join(my)
