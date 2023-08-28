# 문제
# 연속해서 같은 숫자가 3번 연속 나오지 않는 n자리 이진수를 순서대로 출력하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에 정수 n이 공백을 사이에 두고 주어집니다.
#
# 1 ≤ n ≤ 20
# 출력 형식
# 한 줄에 하나의 이진수를 이진법으로 나타내어 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 4
# 출력:
#
# 0010
# 0011
# 0100
# 0101
# 0110
# 1001
# 1010
# 1011
# 1100
# 1101


def generate_binary_strings(n, current=""):
    if len(current) == n:
        print(current)
        return

    if len(current) < 2 or (current[-2:] != "00"):
        generate_binary_strings(n, current + "0")
    if len(current) < 2 or (current[-2:] != "11"):
        generate_binary_strings(n, current + "1")


n = int(input())
generate_binary_strings(n)

