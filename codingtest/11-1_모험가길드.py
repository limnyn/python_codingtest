# 입력 조건
#     첫째 줄에 모험가의 수 N이 주어집니다.
#     둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

# 출력 조건
#     여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

# 입력 예시
#     5
#     2 3 1 2 2

# 출력 예시
#     2


N = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

party_count = 0
party = 0
for a in adventurers:
    party+=1
    if party >= a:
        party = 0
        party_count += 1

print(party_count)
    
