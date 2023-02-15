# A에서 Z로 표현된 태스크가 있다.
# 각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고, n번의 간격 내에는 동일한 태스크를 실행할 수 없다.
# 더 이상 태스크를 실행할 수 없는 경우 아이들 상태가 된다.
# 모든 태스크를 실행하기 위한 최소 간격을 출력하라.

tasks = ["A","A","A","B","B","B"]
n = 2

def leastInterval(tasks, n):
    import collections
    counter = collections.Counter(tasks)
    result = 0
    while True:
        subCount = 0

        # 개수 순 추출
        for task, _ in counter.most_common(n+1):
            subCount += 1
            result += 1
            counter.subtract(task)

            # Counter는 0과 음수도 처리하므로 0이하는 제거해야 한다.
            # 0 이하인 아이템을 목록에서 완전히 제거하는 기능
            counter += collections.Counter()
        if not counter:
            break
        result += n - subCount + 1
    return result

print(leastInterval(tasks,n))