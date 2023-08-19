# 코딩 기초 트레이닝

# 배열의 길이를 2의 거듭제곱으로 만들기
def solution(arr):
    while True:
        n = len(arr)
        if n & (n-1) == 0:
            return arr
        arr.append(0)
    # n이 2의 거듭제곱이라면 n과 n-1을 & 연산 했을 때 0이 나온다


# 배열 비교하기
def solution(arr1, arr2):
    a1, a2 = 0, 0
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    else:
        for a in arr1:
            a1 += a
        for a in arr2:
            a2 += a
        if a1 > a2:
            return 1
        elif a1 < a2:
            return -1
        else:
            return 0


# 문자열 묶기
def solution(strArr):
    answer = {1: 0, 2: 0}
    for str in strArr:
        if len(str) in answer:
            answer[len(str)] += 1
        else:
            answer[len(str)] = 1
    max_ = 1
    max_value = 0
    for key, value in answer.items():
        if value > max_value:
            max_value = value
            max_ = key
    return max_value


# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    k = 0
    if len(arr) % 2 == 0:
        k = 1
    else:
        k = 0
    for i in range(len(arr)):
        if i % 2 == k:
            arr[i] = arr[i] + n
    return arr


# 뒤에서 5등까지
def solution(num_list):
    num_list.sort();
    return num_list[:5]
