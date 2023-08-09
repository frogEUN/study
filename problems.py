# 2753번
# 윤년이면 1, 아니면 0 출력
# 연도가 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일때
year = int(input())
if year % 4 == 0:
    if year % 100 != 0:
        print(1)
    elif year % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)
#  // 몫을 리턴, % 나머지값을 리턴


# 10950번
# 첫째 줄에 테스트 케이스의 개수 T
# A, B -> A+B 출력
t = int(input())
for i in range(0, t):
    nums = input().split()
    print(int(nums[0]) + int(nums[1]))

