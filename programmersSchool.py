# 코딩 기초 트레이닝

# 세 개의 구분자
def solution(myStr):
    word = ''
    answer = []
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            answer.append(word)
            word = ""
            continue
        word = word + i
    answer.append(word)
    answer = [a for a in answer if a != ""]
    if len(answer) == 0:
        return ["EMPTY"]
    return answer


# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for a in arr:
        for i in range(a):
            answer.append(a)
    return answer


# 빈 배열에 추가, 삭제하기
def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i] == True:
            for k in range(arr[i]*2):
                X.append(arr[i])
        else:
            X = X[:len(X)-arr[i]]
    return X


# 배열 만들기 6
def solution(arr):
    stk = list()
    i = 0
    while True:
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            del stk[-1]
            i += 1
        else:
            stk.append(arr[i])
            i += 1
        if i >= len(arr):
            break
    if len(stk) == 0:
        return [-1]
    return stk


# 무작위로 K개의 수 뽑기
def solution(arr, k):
    answer = []
    for a in arr:
        if answer.count(a) == 0:
            answer.append(a)
        if len(answer) >= k:
            break
    while True:
        if len(answer) >= k:
            break
        answer.append(-1)
    return answer
