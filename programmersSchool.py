# 코딩 기초 트레이닝
# 문자열 섞기
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer


# 문자 리스트를 문자열로 변환하기
def solution(arr):
    answer = ''
    for i in range(len(arr)):
        answer = answer + arr[i]
    return answer


# 문자열 곱하기
def solution(my_string, k):
    answer = my_string * k
    return answer


# 더 크게 합치기
def solution(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    ab = int(ab)
    ba = int(ba)
    if ab >= ba:
        answer = ab
    else:
        answer = ba
    return answer


# 두 수의 연산값 비교하기
def solution(a, b):
    ab = int(str(a) + str(b))
    if ab >= 2*a*b:
        answer = ab
    else:
        answer = 2*a*b
    return answer
