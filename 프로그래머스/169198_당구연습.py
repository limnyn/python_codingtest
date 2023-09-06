def solution(m, n, startX, startY, balls):
    # 일단 출발점에서 벽에 제일 가까운 위치를 구하고(이때 해당 방향에 목표가 존재하면 생략) 좌표를 오버해서 삼각형 대각선 길이를 구한다.
    # 4방향 좌표를 구해서 계산하자
    answer = []

    for ball in balls:
        endx, endy = ball[0], ball[1]
        xy1 = (-1 * startX, startY)
        xy2 = (2 * m - startX, startY)
        xy3 = (startX, -1 * startY)
        xy4 = (startX, 2 * n - startY)
        lst = [xy1, xy2, xy3, xy4]

        # 아래에서 진행 방향에 공이 있을 경우 검사
        if startX == endx:
            if (startY - endy) < 0:
                lst.remove(xy4)
            else:
                lst.remove(xy3)
        if startY == endy:
            if (startX - endx) < 0:
                lst.remove(xy2)
            else:
                lst.remove(xy1)

        # 각 방향에 대해 최단거리 계산
        min_dist = 1e9
        for x, y in lst:
            min_dist = min(min_dist, (x - endx) ** 2 + (y - endy) ** 2)

        answer.append(min_dist)

    return answer


m = 10
n = 10
startX = 3
startY = 7
balls = [[7, 7], [2, 7], [7, 3]]
# result = [52, 37, 116]


print(solution(m, n, startX, startY, balls))
