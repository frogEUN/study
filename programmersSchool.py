# 코딩 기초 트레이닝
# n의 배수
def solution(num, n):
    if num % n == 0:
        answer = 1
    else:
        answer = 0
    return answer


# 공배수
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        answer = 1
    else:
        answer = 0
    return answer


# 홀짝에 따라 다른 값 반환하기
def solution(n):
    answer = 0
    if n % 2 == 0:  # 짝수
        for i in range(2, n+2, 2):
            answer += i * i
    else:  # 홀수
        for i in range(1, n+2, 2):
            answer += i
    return answer


# 조건 문자열
def solution(ineq, eq, n, m):
    if ineq == ">":
        if eq == "=":
            if n >= m:
                return 1
            else:
                return 0
        else:
            if n > m:
                return 1
            else:
                return 0
    else:
        if eq == "=":
            if n <= m:
                return 1
            else:
                return 0
        else:
            if n < m:
                return 1
            else:
                return 0


# flag에 따라 다른 값 반환하기
# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b
