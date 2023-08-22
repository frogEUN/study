# 코딩 기초 트레이닝

# 커피 심부름
def solution(order):
    answer = 0
    for o in order:
        if 'americano' in o or o == 'anything':
            answer += 4500
        else:
            answer += 5000
    return answer


# 그림 확대
def solution(picture, k):
    answer = []
    temp = ''
    for p in picture:
        for s in p:
            temp += s * k
        for i in range(k):
            answer.append(temp)
        temp = ''
    return answer


# 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    if k % 2 == 0:
        for i in range(len(arr)):
            arr[i] = arr[i] + k
    else:
        for i in range(len(arr)):
            arr[i] = arr[i] * k
    return arr


# l로 만들기
def solution(myString):
    my = list(myString)
    for i in range(len(my)):
        if ord(my[i]) < ord('l'):
            my[i] = 'l'
    return ''.join(my)


# 특별한 이차원 배열 1
def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for k in range(n):
            if i == k:
                temp.append(1)
            else:
                temp.append(0)
        answer.append(temp)
    return answer
