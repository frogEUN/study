# 코딩 기초 트레이닝

# 수열과 구간 쿼리 4
def solution(arr, queries):
    for q in queries:
        for i in range(len(arr)):
            if q[0] <= i <= q[1]:
                if i % q[2] == 0:
                    arr[i] = arr[i] + 1
    return arr


# 배열 만들기2
def solution(l, r):
    answer = []
    temp = True
    for i in range(l, r+1):
        i = str(i)
        for k in range(len(i)):
            if i[k] == '5' or i[k] == '0':
                continue
            else:
                temp = False
                break
        if temp:
            answer.append(int(i))
        temp = True
    if len(answer) == 0:
        return [-1]
    return answer


# 카운트 업
def solution(start, end):
    answer = []
    for i in range(start, end + 1):
        answer.append(i)
    return answer


# 콜라츠 수열
def solution(n):
    answer = [n]
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        answer.append(n)
        if n == 1:
            break
    return answer


# 배열 만들기 4
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            del stk[-1]
    return stk
