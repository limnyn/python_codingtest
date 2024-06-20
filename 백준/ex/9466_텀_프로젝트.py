# https://www.acmicpc.net/problem/9466
'''
[문제]
    s1, s2, ... sr, s1 또는
    s1, s1 형식의 싸이클을 찾아서 제외하고
    남은 학생의 수 출력하기

[입력]
    2 <= n <= 100,000

[접근]
    1. 각 시작점 별로 visited를 번호로 매겨 같은 싸이클에 대해 중복순회를 돌지 않게 한다
    2. 방문한 노드가 나올 때 까지 스택을 통해 깊이 탐색을 한다
    3. 마지막 노드가 이전 노드와 일치할 때 까지 스택에서 pop 한다
        3-1. 이때까지 반복되는 동안은 Group이기 때문에 Group 내부에 포함되었다고 체크해준다 - grouped
    4. group에 포함되지 않은 노드들을 count 해서 더한다.

'''
import sys
def input(): return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr = [a - 1 for a in arr]
        visited = [-1] * n
        grouped = [False] * n
        idx = 0

        while idx < n:
            node = idx # 1.
            if visited[node] != -1:
                idx += 1
                continue

            stack = []
            while visited[node] == -1: # 2.
                stack.append(node)
                visited[node] = idx
                node = arr[node]
            
            if visited[node] == idx:
                grouped[node] = True
                
                while stack: # 3.
                    before = stack.pop()
                    if before == node:
                        break
                    grouped[before] = True
            
            idx += 1
        
        result = 0 # 4.
        for g in grouped:
            if not g:
                result += 1
        print(result)

'''
입력 간선을 counting 해 cycle 외부의 노드들을 찾아서 반환하는 제일 빠른 코드
if __name__ == "__main__":
    result = []
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr = [a - 1 for a in arr]

        counts = [0] * n
        for a in arr:
            counts[a] += 1

        ends = [i for i, c in enumerate(counts) if c == 0]
        i = 0

        while i < len(ends):
            x = arr[ends[i]]
            i += 1
            counts[x] -= 1
            if counts[x] == 0:
                ends.append(x)

        ans = counts.count(0)
        print(ans)
'''