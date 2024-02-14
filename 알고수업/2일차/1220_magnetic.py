# https://swexpertacademy.com/main/talk/solvingClub/problemPassedUser.do?contestProbId=AV14hwZqABsCFAYD&solveclubId=AV6kld8aisgDFASb&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14&probBoxId=AV-4MojKLNADFATz


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

# 7
# 1 0 2 0 1 0 1
# 0 2 0 0 0 0 0
# 0 0 1 0 0 1 0
# 0 0 0 0 1 2 2
# 0 0 0 0 0 1 0
# 0 0 2 1 0 2 1
# 0 0 1 2 2 0 2
