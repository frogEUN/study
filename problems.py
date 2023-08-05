# 27866번
s = input()
i = int(input())
print(s[i-1])

# 2743번
word = input()
print(len(word))
# len()  : 문자열을 인자로 받아, 문자열의 길이를 숫자로 반환

# 9086번
t = int(input())
answers = list()
for i in range(1, t+1):
    word = input()
    answers.append(word[0]+word[-1])
for i in range(0, t):
    print(answers[i])
# append : 원소 마지막에 추가
# insert : 리스트.index(입력할 index, 값)
# extend : 리스트.extend(추가할 리스트)
