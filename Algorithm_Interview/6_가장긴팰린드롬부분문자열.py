# 가장 긴 팰린드롬 부분 문자열

line = input()

def expand(left, right):
    while left >= 0 and right < len(line) and line[left] == line[right]:
        left-=1
        right+=1
    return line[left+1:right]

if len(line) < 2 or line == line[::-1]:
    print(line)
else:
    result = ''
    for i in range(len(line)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    print(result)

# line = input()



# def expand(left, right):
#     while left >= 0 and right < len(line) and line[left] == line[right]:
#             left -= 1
#             right += 1
#     return line[left+1:right]


# if len(line) < 2 or line == line[::-1]:
#     print(line)
# else:
#     result = ''
#     for i in range(len(line) - 1):
#         result = max(result, expand(i, i+1), expand(i, i+2), key=len)
#     print(result)