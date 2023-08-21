# 코딩 기초 트레이닝

# 0 떼기
def solution(n_str):
    return n_str.lstrip('0')


# 두 수의 합
def solution(a, b):
    return str(int(a)+int(b))


# 문자열로 변환
def solution(n):
    return str(n)


# 배열의 원소 삭제하기
def solution(arr, delete_list):
    for d in delete_list:
        if d in arr:
            del arr[arr.index(d)]
    return arr


# 부분 문자열인지 확인하기
def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0
