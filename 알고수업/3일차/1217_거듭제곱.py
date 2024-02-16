# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

def power(n, m):
    if m == 0:
        return 1
    else:
        return n * power(n, m-1)
for _ in range(10):
    t_c_num = int(input())

    n, m = map(int, input().split())
     
    print(f'#{t_c_num} {power(n,m)}')
