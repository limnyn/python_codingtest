# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1


import heapq

for t_c in range(10):
    n = int(input())
    boxes = list(map(int, input().split()))
    max_boxes = [[-x, i] for i, x in enumerate(boxes)]
    min_boxes = [[x, i] for i, x in enumerate(boxes)]
    heapq.heapify(max_boxes)
    heapq.heapify(min_boxes)
    for _ in range(n):
        x, i = heapq.heappop(max_boxes)
        heapq.heappush(max_boxes, [x + 1, i])
        x, i = heapq.heappop(min_boxes)
        heapq.heappush(min_boxes, [x + 1, i])
    result = -(heapq.heappop(max_boxes)[0] + heapq.heappop(min_boxes)[0])
    print("#" + str(t_c + 1) + " " + str(result))
