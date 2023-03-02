# 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

line = input()
sum = 0
result = []
for c in line:
    if c.isnumeric():
        sum += int(c)
    else:
        result.append(c)

result.sort()
result.append(str(sum))
print(''.join(result))



