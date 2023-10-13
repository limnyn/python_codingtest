# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1


# 가장 긴 팰린드롬 반환
def longest_palindrome(grid):
    result = 0
    for n in range(100, 0, -1):
        for line in grid:
            for c in range(100 - n + 1):
                txt = line[c : c + n]
                txt_r = txt[::-1]
                if txt == txt_r:
                    if result < n:
                        result = n
                        return result


for t_c in range(10):
    t_c_num = int(input())
    result = 0
    grid_r = []
    grid_c = [[] for _ in range(100)]

    for row in range(100):
        line = input()
        grid_r.append([c for c in line])
        # for i, c in enumerate(line):
        # grid_c[i].append(c)
        grid_c = list(map(list, zip(*grid_r)))

    # 가로 세로 그리드 중 가장 긴 펠린드롬을 찾는다
    result = max(longest_palindrome(grid) for grid in [grid_r, grid_c])

    print("#" + str(t_c + 1) + " " + str(result))
