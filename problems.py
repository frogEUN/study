# 1152번
print(len(input().split()))

# 2908번
# 두 수 A와 B가 주어짐(세 자리 수)
# 두 수를 거꾸로 읽어서 큰 수를 출력
words = input().split()
A = int(words[0][2]) * 100 + int(words[0][1]) * 10 + int(words[0][0])
B = int(words[1][2]) * 100 + int(words[1][1]) * 10 + int(words[1][0])
if A > B:
    print(A)
else:
    print(B)
