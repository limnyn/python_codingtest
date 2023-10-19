# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1


# 6! 720개

T = int(input())
for t_c in range(1, T + 1):
    num = [int(x) for x in input()]
    numlen = len(num)
    decode = [0] * numlen
    count = 1

    idx = num.index(1)
    is1 = True
    for i in range(idx, numlen):
        if is1 == True and num[i] == 0:
            count += 1
            is1 = False
        elif is1 == False and num[i] == 1:
            count += 1
            is1 = True
    if sum(num) == 0:
        count = 0

    print(f"#{t_c} {count}")

# 123456
# # 654321에 대해 몇번 바꿔서 만들 수 있는가에 대해 생각
# 123을 예로 들어, 최소로 바꾸는 수 n에 대해
# 123 0
# 213 1
# 321 1
# 132 1
# 312 2
# 231 2

# 같은수가 없을 때
# n % 2 == 0: 0~ n까지 짝수 중 max
# n % 2 == 1: 1~ n까지 홀수중 max
# 같은수가 있으면 n이하 모든 수
