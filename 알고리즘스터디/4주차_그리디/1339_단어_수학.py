# https://www.acmicpc.net/problem/1783



"""
1. 단어의 길이가 긴 숫자에 큰 수를 준다
2. 가장 큰 자리 수 부터 9, 8, 7, .. 내려온다
    2-1. 만약 같은 자리 수가 여러개면 
        2-1-1. 해당 자리 숫자의 중복갯수가 많은 수부터 높은 수 부여

10자리 단어에 대해
제일 처음 나오는 숫자부터 9로
"""
n = int(input())
word_mod = {}
words = [{} for _ in range(10)]
words_origin = []
for _ in range(n):
    line = list(input())
    words_origin.append(line)
    line_len = len(line)
    # line_front = [-1]*(10-len(line))
    for i, c in enumerate(line):
        if c not in words[10-line_len-1+i]:
            words[10-line_len-1+i][c] = 1
        else:
            words[10-line_len-1+i][c] += 1
        if c not in word_mod:
            word_mod[c] = 1
            
        
    # words.append(line_front + line)

conv_dict = {}
num = 9
print(words)
for word in words:
    for key, value in word.items():
        if key not in conv_dict:
            conv_dict[key] = num
            num -= 1
print(conv_dict)

result = 0

for word in words_origin:
    for i, v in enumerate(word[::-1]):
        result += conv_dict[v] * 10**i
print(result)