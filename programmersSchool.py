# 코딩 기초 트레이닝

# 조건에 맞게 수열 변환하기 1
def solution(arr):
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
        elif arr[i] < 50 and arr[i] % 2 == 1:
            arr[i] = arr[i] * 2
    return arr


# 조건에 맞게 수열 변환하기 2
def solution(arr):
    x = 0
    arr_x = arr
    while True:
        arr_x = arr[:]
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        x = x + 1
        if arr_x == arr:
            return x-1


# 1로 만들기
def solution(num_list):
    result = 0
    for n in num_list:
        while True:
            if n == 1:
                break
            elif n % 2 == 0:
                n = n // 2
                result += 1
            else:
                n = (n - 1) // 2
                result += 1
    return result


# 길이에 따른 연산
def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        for n in num_list:
            answer += n
        return answer
    else:
        answer = 1
        for n in num_list:
            answer *= n
        return answer


# 원하는 문자열 찾기
def solution(myString, pat):
    if myString.upper().find(pat.upper()) == -1:
        return 0
    return 1
