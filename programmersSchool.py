# 코딩 기초 트레이닝

# 대문자로 바꾸기
def solution(myString):
   return myString.upper()


# 소문자로 바꾸기
def solution(myString):
    return myString.lower()


# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    for i in range(len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    return strArr


# A 강조하기
def solution(myString):
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'a' or myString[i] == 'A':
            myString[i] = myString[i].upper()
        else:
            myString[i] = myString[i].lower()
    return ''.join(myString)


# 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    m = list(my_string)
    for i in range(len(m)):
        if m[i] == alp:
            m[i] = m[i].upper()
    return ''.join(m)
