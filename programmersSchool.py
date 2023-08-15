# 코딩 기초 트레이닝

# n 번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]


# 순서 바꾸기
def solution(num_list, n):
    return num_list[n:] + num_list[:n]


# 왼쪽 오른쪽
def solution(str_list):
    if str_list.count('l') == str_list.count('r') == 0:
        return []
    elif str_list.count('l') == 0:
        return str_list[str_list.index('r') + 1:]
    elif str_list.count('r') == 0:
        return str_list[:str_list.index('l')]
    l = str_list.index('l')
    r = str_list.index('r')
    if l < r:
        return str_list[:l]
    else:
        return str_list[r + 1:]


# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]


# n개 간격의 원소들
def solution(num_list, n):
    return num_list[::n]

