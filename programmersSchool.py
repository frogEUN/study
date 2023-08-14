# 코딩 기초 트레이닝

# 문자 개수 세기
def solution(my_string):
    answer = []
    for i in range(ord('A'), ord('Z')+1):
        answer.append(my_string.count(chr(i)))
    for i in range(ord('a'), ord('z')+1):
        answer.append(my_string.count(chr(i)))
    return answer


# 배열 만들기 1
def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)
    return answer


# 글자 지우기
def solution(my_string, indices):
    my = list(my_string)
    indices.sort(reverse=True)
    for i in indices:
        del my[i]
    return ''.join(my)


# 카운트 다운
def solution(start, end):
    answer = []
    for i in range(start, end-1, -1):
        answer.append(i)
    return answer


# 가까운 1 찾기
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1


