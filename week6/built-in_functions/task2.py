cnt1 = 0
cnt2 = 0

s = input()
for i in range(len(s)):
    if s[i].islower():
        cnt1 += 1
    elif s[i].isupper():
        cnt2 += 1

print(cnt1, cnt2)