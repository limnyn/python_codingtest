# https://www.acmicpc.net/problem/1082
"""
[문제]
N - 숫자 갯수
M - 준비된 금액
Pi - 각 숫자별 가격

[조건]
방 번호가 0이 아니라면 0으로 시작할 수 없다
1 <= N <= 10
1 <= Pi <= 50
1 <= M <= 50
각 숫자는 정수


[목표]
가진 비용으로 만들 수 있는 가장 큰 방 번호 구하기

[접근]

가장 큰 방번호는?
1. 가장 큰 자릿수
2. 가장 큰 자릿수 중에서 앞 번호가 가장 큰 경우

[시도]
1. 가장 긴 자릿수를 구한다. (맨 처음에는 0이 되면 안된다.)
2. 맨 첫자리 부터 가능한 큰 수로 바꾸는 연산을 진행한다.
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def max_room_number(N, costs, M):
    # 비용과 숫자를 묶어서 정렬 (비용 오름차순, 비용 같으면 숫자 내림차순)
    sorted_numbers = sorted(range(N), key=lambda x:(costs[x], -x))

    # 0만 있는 경우는 방을 만들 수 없다
    if N == 1:
        return "0"

    # 1. base 케이스 생성
    base = ""
    
    if sorted_numbers[0] == 0: # 가장 싼 숫자가 0일 경우
        temp_cost = M - costs[sorted_numbers[1]] # 두번째로 싼 숫자 선택
        if temp_cost < 0: # 0이 아닌 가장 싼 숫자 사용 불가인 경우
            return "0"
        base += str(sorted_numbers[1])
        length = temp_cost // costs[sorted_numbers[0]]
        base += str(sorted_numbers[0]) * length
        M = temp_cost - costs[sorted_numbers[0]] * length

    else: # 가장 싼 숫자가 0이 아닐 경우
        length = M // costs[sorted_numbers[0]]
        base += str(sorted_numbers[0]) * length
        M -= length * costs[sorted_numbers[0]]

    # 2. 큰 숫자로 교체
    base = list(base)
    for i in range(len(base)):
        current_cost = costs[int(base[i])] # 현재 자릿수
        for j in range(N-1, int(base[i])-1, -1):
            if M >= costs[j] - current_cost:
                M -= (costs[j] - current_cost)
                base[i] = str(j)
                break

    return ''.join(base)


if __name__ == "__main__":
    N = int(input())
    costs = list(map(int, input().split()))
    M = int(input())
    print(max_room_number(N, costs, M))


    
