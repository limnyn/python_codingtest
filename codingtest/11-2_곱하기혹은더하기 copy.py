# 숫자로만 이루어진 문자열 S가 주어졌을 때,
# 각 숫자 사이에 x와 + 연산자를 넣어 결과적으로 만들 어 질 수 있는 가장 큰 수를 구하는 프로그램
# 단 모든 연산은  x가 +보다 먼저 연산되는 것이 아닌 
# 왼쪽에서 오른쪽으로 한단계씩 연산하는 순서입니다.

# 입력 조건
#     첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 20)

# 출력 조건
#     첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

# 입력 예시
#     02984

# 출력 예시
#     576

S = input()

def solution(S):
    result = int(S[0])
    for i in range(1, len(S)):
        if int(S[i-1]) <= 1:
            result += int(S[i])
        else:
            result *=  int(S[i])

    return result

    
            

print(solution(S))