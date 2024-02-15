# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1


for t_c in range(10):
    t_c_num = int(input())

    n, m = map(int, input().split())
    result = n**m
    print("#" + str(t_c + 1) + " " + str(result))
