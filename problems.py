# 5622번
word = input()
result = 0
nums = [[], [], ['ABC'], ['DEF'], ['GHI'], ['JKL'], ['MNO'], ['PQRS'], ['TUV'], ['WXYZ']]
for i in range(0, len(word)):
    for n in range(2, 10):
        if word[i] in nums[n][0]:
            result = result + n + 1
print(result)

# 11718번
# 문제의 목적 : 문자열을 올바르게 입력받고 파일의 끝을 올바르게 판단하는 법 연습
# 더 이상 읽을 게 없을 때 프로그램을 종료하는 법을 알아야함.
while True:
    try:
        print(input())
    except EOFError:
        break
# EOF : 더 이상 읽을 데이터가 없음
