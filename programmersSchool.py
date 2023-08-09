# Lv0. 문자열이 몇 번 등장하는지 세기
# 문자열 myString과 pat이 주어짐.
# myString에서 pat이 등장하는 횟수를 return하는 solution함수 완성하기
''' 풀이1
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
'''


''' 풀이2
def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer
'''