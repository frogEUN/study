# 코딩 기초 트레이닝

# 마지막 두 원소
def solution(num_list):
    answer = []
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1]*2)
    return num_list + answer


# 수 조작하기 1
def solution(n, control):
    for i in control:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        elif i == 'a':
            n -= 10
    return n


# 수 조작하기 2
def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        temp = numLog[i] - numLog[i-1]
        if temp == 1:
            answer = answer + 'w'
        elif temp == -1:
            answer = answer + 's'
        elif temp == 10:
            answer = answer + 'd'
        elif temp == -10:
            answer = answer + 'a'
    return answer


# 수열과 구간 쿼리 3
def solution(arr, queries):
    for q in queries:
        arr[q[0]], arr[q[1]] = arr[q[1]], arr[q[0]]
    return arr


# 수열과 구간 쿼리 2
def solution(arr, queries):
    answer = []
    small = -1
    for q in queries:
        for i in range(len(arr)):
            if q[0] <= i <= q[1]:
                if arr[i] > q[2]:
                    if small == -1:
                        small = arr[i]
                    else:
                        if small > arr[i]:
                            small = arr[i]
        answer.append(small)
        small = -1
    return answer

