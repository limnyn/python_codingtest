
import heapq #파이썬은 최소힙
for t_c in range(1,11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    max_boxes = [[-x, i] for i, x in enumerate(boxes)]
    min_boxes = [[x, i] for i, x in enumerate(boxes)]
    heapq.heapify(max_boxes)
    heapq.heapify(min_boxes)
    for _ in range(dump):
        highest = heapq.heappop(max_boxes)
        heapq.heappush(max_boxes,[highest[0]+1, highest[1]])
        lowest = heapq.heappop(min_boxes)
        heapq.heappush(min_boxes, [lowest[0]+1, lowest[1]])
    result = -(heapq.heappop(max_boxes)[0] + heapq.heappop(min_boxes)[0])
    print(f'#{t_c} {result}')

"""
이전 코드 대비 변수명은 직관적이지만 이해하기 더 복잡해짐

"""