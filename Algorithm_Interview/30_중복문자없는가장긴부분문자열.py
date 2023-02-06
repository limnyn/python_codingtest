# 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.
# 입력
#     abcabcbb
# 출력
#     3


s = input()
used = {}
max_length = start = 0
for index, char in enumerate(s):
    if char in used and start <= used[char]:
        start = used[char] + 1
    else:
        max_length = max(max_length, index - start + 1)

    # 현재 문자의 위치 삽입
    used[char] = index
print(max_length)
        
