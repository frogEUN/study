# 25206번
# 20줄 - 전공과목명, 학점 등급
# 전공평점 출력하기
scores = {'A+' : 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum1 = 0
sum2 = 0
for i in range(20):
    temp = input().split()
    if temp[2] == 'P':
        continue
    sum1 += float(temp[1])
    sum2 += scores[temp[2]] * float(temp[1])
print(sum2/sum1)


# 1157번
# 알파벳으로 이루어진 단어가 주어짐.
# 가장 많이 사용된 글자 출력. 여러개면 ? 출력.
word = input()
max_num = 0
max_letter = ''
for letter in word:  # input()의 글자를 돌면서
    count = word.count(letter)
    if count == max_num and max_letter != letter:
        max_num = -1
        break        # 그 글자의 개수가 최대개수와 같고 최대 글자와 다르다면 max_num을 -1로 하고 break
    elif count > max_num:
        max_num = count
        max_letter = letter  # 그 글자의 개수가 최대 개수보다 크면 최대개수의 글자의 개수를, 최대 문자의 글자를 넣는다
if max_num == -1:
    print('?')
else:
    print(max_letter)
# 시간 초과....


word = input().upper()
letters = list(set(word))  # input()을 set으로 만들고 다시 list로 만든다
counts = list()
for letter in letters:
    counts.append(word.count(letter))  # letters를 순회하면서 input()에서 개수를 세서 리스트에 넣는다

if counts.count(max(counts)) > 1:  # counts에서 최댓값이 여러 개면 ? 출력
    print('?')
else:
    print(letters[counts.index(max(counts))])  # 최댓값으로 인덱스를 구해 문자를 찾아 출력
