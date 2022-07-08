# 입력 조건
#     첫째 줄에 N, M이 주어진다. M은 입력으로 주어지는 연산의 개수이다.
#     다음 M개의 줄에는 각각의 연산이 주어진다.
#     '팀 합치기'연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
#     '같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다.
#     a와 b는 N 이하의 양의 정수이다.

# 출력 조건
#     '같은 팀 여부 확인' 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.


# 입력 예시
#     7 8
#     0 1 3
#     1 1 7
#     0 7 6
#     1 7 1
#     0 3 7
#     0 4 2
#     0 1 1
#     1 1 1

# 출력 예시
#     NO
#     NO
#     YES



n, m = map(int, input().split())

p = [-1] * (n+1) 

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

for i in range(1, n+1):
    p[i] = i
def union(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def isUnion(p, a, b):
    if p[a] == p[b]:
        return "YES"
    else:
        return "NO"

result = []
for _ in range(m):
    calc, a, b = map(int, input().split())
    if calc == 0:
        union(p,a,b)
    elif calc == 1:
        result.append(isUnion(p,a,b))

for r in result:
    print(r)    