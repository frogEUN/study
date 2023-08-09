# 25083번
print('         ,r\'\"7')
print('r`-_   ,\'  ,/')
print(' \\.\". L_r\'')
print('   `~\\/')
print('      |')
print('      |')

# 3003번
# 킹 1, 퀸 1, 룩 2, 비숍 2, 나이트 2, 폰 8
dong = input().split()
answers = [1, 1, 2, 2, 2, 8]
for i in range(0, len(dong)):
    print(answers[i] - int(dong[i]), end=' ')
