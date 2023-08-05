# 4장 - 선택하기: if

furry = True
large = True
if furry:
    if large:
        print("yeti")
    else:
        print("cat")
else:
    if large:
        print("whale")
    else:
        print("human")

# 4.1
secret = 8
guess = 2
if secret == guess:
    print("just right")
elif guess > secret:
    print("too high")
else:
    print("too low")
