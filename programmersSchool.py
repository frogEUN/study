# 코딩 기초 트레이닝

# 리스트 자르기
def solution(n, slicer, num_list):
    a, b, c = slicer[0], slicer[1], slicer[2]
    if n == 1:
        return num_list[:b + 1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b + 1]
    elif n == 4:
        return num_list[a:b + 1:c]


# 첫 번째로 나오는 음수
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1


# 배열 만들기 3
def solution(arr, intervals):
    answer = []
    for k in range(len(intervals)):
        for i in range(intervals[k][0], intervals[k][1]+1):
            answer.append(arr[i])
    return answer


# 2의 영역
def solution(arr):
    last = -1
    for i in range(len(arr)):
        if arr[i] == 2:
            last = i
    if last == -1:
        return [-1]
    if arr.index(2) == last:
        return [2]
    return arr[arr.index(2):last+1]


# 배열 조각하기
def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        if i % 2 == 0:
            answer = answer[:query[i]+1]
        else:
            answer = answer[query[i]:]
    return answer
