# 코딩 기초 트레이닝
# 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a+b}')


# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str1+str2)


# 문자열 돌리기
str = input()
for i in range(len(str)):
    print(str[i])


# 홀짝 구분하기
n = int(input())
if n % 2 == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')


# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer
