# 코딩 기초 트레이닝

# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
def solution(myString, pat):
    if myString.count(pat) == 1:
        return myString[:myString.find(pat)]+pat
    temp = myString[::-1]
    tempPat = pat[::-1]
    return myString[:len(myString)-temp.find(tempPat)-1]+pat


# 문자열이 몇 번 등장하는지 세기
def solution(myString, pat):
    answer = 0
    temp = 0
    while True:
        idx = myString.find(pat, temp)
        if idx == -1:
            break
        answer += 1
        temp = idx + 1
    return answer


# ad 제거하기
def solution(strArr):
    delList = list()
    for i in range(len(strArr)):
        if strArr[i].find("ad") >= 0:
            delList.append(i)
    delList.sort(reverse=True)
    for k in delList:
        del strArr[k]
    return strArr


# 공백으로 구분하기 1
def solution(my_string):
    return my_string.split()


# 공백으로 구분하기 2
def solution(my_string):
    return my_string.split()
