# 25304번 (영수증)
# 첫째 줄 - 영수증에 적힌 총 금액
# 둘째 줄 - 구매한 물건의 종류의 수
# 각 물건의 가격과 개수
x = int(input())
n = int(input())
result = 0
for i in range(n):
    a, b = input().split()
    result += int(a) * int(b)
if x == result:
    print('Yes')
else:
    print('No')


# 25314번
n = int(input())
print('long ' * (n//4) + 'int')
