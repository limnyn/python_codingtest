# 큐 == 대기열, FIFO, 선입선출
# 예제 2번
# 삽입5-삽입2-삽입3-삽입7-삭제-삽입1-삽입4-삭제
# 넣고 빼는 속도가 리스트보다 빠르다. 
from collections import deque

queue = deque()


queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)


