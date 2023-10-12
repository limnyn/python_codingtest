# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

for t in range(1, 11):
    n = int(input())
    cities = list(map(int, input().split()))

    count = 0

    for i, city in enumerate(cities[:-2]):
        if i < 2 or city == 0:
            continue
        for j in range(city, 0, -1):
            if (
                cities[i - 2] < j
                and cities[i - 1] < j
                and cities[i + 1] < j
                and cities[i + 2] < j
            ):
                count += 1
            else:
                break
    print("#" + str(t) + " " + str(count))
