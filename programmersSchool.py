# 코딩 기초 트레이닝

# 홀수 vs 짝수
def solution(num_list):
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if (i+1) % 2 == 0:
            even += num_list[i]
        else:
            odd += num_list[i]
    if even >= odd:
        return even
    else:
        return odd


# 5명씩
def solution(names):
    return names[::5]


# 할 일 목록
def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if finished[i] == False:  # not finished[i]
            answer.append(todo_list[i])
    return answer


# n보다 커질 때까지 더하기
def solution(numbers, n):
    result = 0
    for num in numbers:
        result += num
        if result > n:
            return result


# 수열과 구간 쿼리 1
def solution(arr, queries):
    for q in queries:
        for i in range(len(arr)):
            if q[0] <= i <= q[1]:
                arr[i] = arr[i] + 1
    return arr
