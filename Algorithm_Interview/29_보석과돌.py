# J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까?
# 대소문자는 구분한다.
# 입력
    # J = "aA" S = 'aAAbbbb'
# 출력
    # 3
import collections
J = input()
S = input()

freqs = collections.Counter(S)
count = 0

for char in J:
    count+= freqs[char]

print(count)