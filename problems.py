# 10809번
word = input()
for i in range(ord('a'), ord('z')+1):
    print(word.find(chr(i)), end=' ')

# 2675번
t = int(input())
words = list()

for i in range(0, t):
    rANDs = input().split()
    words.append(rANDs)

for i in range(0, t):
    for k in range(0, len(words[i][1])):
        print(words[i][1][k] * int(words[i][0]), end='')
    print()
