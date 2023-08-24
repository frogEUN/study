# 코딩 기초 트레이닝

# 특별한 이차원 배열 2
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


# 정사각형으로 만들기
def solution(arr):
    a = len(arr)
    b = len(arr[0])
    if a > b:
        for i in range(len(arr)):
            for k in range(a - b):
                arr[i].append(0)
    elif a < b:
        for i in range(b - a):
            temp = []
            for k in range(b):
                temp.append(0)
            arr.append(temp)
            temp = []
    return arr


# 이차원 배열 대각선 순회하기
def solution(board, k):
    answer = 0
    temp = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                temp.append(board[i][j])
    for t in temp:
        answer += t
    return answer
