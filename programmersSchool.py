# 코딩 기초 트레이닝

# 부분 문자열
def solution(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0


# 꼬리 문자열
def solution(str_list, ex):
    answer = ''
    for str in str_list:
        if ex in str:
            continue
        else:
            answer = answer + str
    return answer


# 정수 찾기
def solution(num_list, n):
    if num_list.count(n) == 0:
        return 0
    return 1


# 주사위 게임 1
def solution(a, b):
    answer = 0
    if a % 2 == 1 and b % 2 == 1:
        answer += a*a + b*b
    elif a % 2 == 1 or b % 2 == 1:
        answer += 2 * (a + b)
    else:
        answer += abs(a-b)
    return answer


# 날짜 비교하기
def solution(date1, date2):
    if date1[0] < date2[0]:
        return 1
    elif date1[0] > date2[0]:
        return 0
    else:
        if date1[1] < date2[1]:
            return 1
        elif date1[1] > date2[1]:
            return 0
        else:
            if date1[2] < date2[2]:
                return 1
            elif date1[2] > date2[2]:
                return 0
            else:
                return 0
