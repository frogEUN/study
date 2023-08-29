# 코딩 기초 트레이닝

# 정수를 나선형으로 배치하기
def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for k in range(n):
            temp.append(0)
        answer.append(temp)
    right = True
    left = False
    up = False
    down = False
    r = 0
    c = 0
    for i in range(1, n * n + 1):
        answer[r][c] = i
        if right:
            if c + 1 >= n or answer[r][c + 1] != 0:
                right = False
                down = True
                r = r + 1
            else:
                c = c + 1
        elif left:
            if c - 1 < 0 or answer[r][c - 1] != 0:
                left = False
                up = True
                r = r - 1
            else:
                c = c - 1
        elif up:
            if answer[r - 1][c] != 0:
                up = False
                right = True
                c = c + 1
            else:
                r = r - 1
        elif down:
            if r + 1 >= n or answer[r + 1][c] != 0:
                down = False
                left = True
                c = c - 1
            else:
                r = r + 1
    return answer
