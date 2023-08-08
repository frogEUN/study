# 11654번
print(ord(input()))

# 11720번
# 첫째 줄에 숫자의 개수, 둘째 줄에 숫자 n개 공백없이.
# 숫자들의 합을 출력
n = int(input())
result = 0
numbers = input()
for i in range(0, n):
    result = result + int(numbers[i])
print(result)
