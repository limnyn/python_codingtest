# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1


# 각 열의 첫 빨강에 대해 그 아래에 파랑이 몇개 있는지 반환하면 되는 간단한 문제
for t_c in range(10):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    grid = list(map(list, zip(*grid)))

    count = 0

    for line in grid:
        mag = False
        for i in range(n):
            if line[i] == 1:
                mag = True
            elif line[i] == 2:
                if mag == True:
                    mag = False
                    count += 1

    print("#" + str(t_c + 1) + " " + str(count))

# 1 0 2 0 1 0 1
# 0 2 0 0 0 0 0
# 0 0 1 0 0 1 0
# 0 0 0 0 1 2 2
# 0 0 0 0 0 1 0
# 0 0 2 1 0 2 1
# 0 0 1 2 2 0 2
