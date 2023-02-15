# 여러 명의 사람들이 줄을 서 있다. 각각의 사람은 (h, k)의 두 정수 쌍을 갖는데,
# h는 그 사람의 키, k는 앞에 줄 서 있는 사람들 중 자신의 키 이상인 사람들의 수를 뜻한다.
# 이 값이 올바르도록 줄을 재정렬하는 알고리즘을 작성하라.

line = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

print(line)

def reconstructQueue(line):
    import heapq
    heap = []
    for person in line:
        heapq.heappush(heap, (-person[0],person[1]))

    result = []
    while heap:
        person = heapq.heappop(heap)
        
        # insert(a,b)는 a인덱스에 b를 삽입한다.
        result.insert(person[1],[-person[0],person[1]])
        
    return result
print(reconstructQueue(line))