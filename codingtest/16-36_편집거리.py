# 두 개의 문자열 A와 B가 주어졌을 때, 문자열 A를 편집하여 문자열 B로 만들고자 합니다.
# 문자열 A를 편집할 때는 다음의 세 연산자 중에서 한 번에 하나씩 선택하여 이용햘 수 있습니다.
#     1. 삽입 :   특정한 위치에 하나의 문자를 삽입합니다.
#     2. 삭제 :   특정한 위치에 있는 하나의 문자를 삭제합니다.
#     3. 교체 :   특정한 위치에 있는 하나의 문자를 다른 문자로 교체합니다.
# 이때 편집 거리란 문자열 A를 편집하여 문자열 B로 만들기 위해 사용한 연산의 수를 의미합니다.
# 문자열 A를 문자열 B로 만드는 최소 편집 거리를 계산하는 프로그램을 작성하세요.
# 예를 들어 "sunday"와 "saturday"의 최소 편집 거리는 3입니다.

# 입력 조건
#     두 문자열 A와 B가 한줄에 하나씩 주어집니다.
#     각 문자열은 영문 알파벳으로만 구성되어 있으며, 각 문자열의 길이느 1보다 크거나 같고, 5000보다 작거나 같습니다.

# 출력 조건
#     최소 편집 거리를 출력합니다.


# 입력 예시 1
#     cat
#     cut
    
# 입력 예시 2
#     sunday
#     saturday

a = input()
b = input()

len_a = len(a) + 1
len_b = len(b) + 1


# dp = [[0]*(len_a) for _ in range(len_b)]

# for i in range(1,len_a):
#     for j in range(1, len_b):
#         if a[i-1] == b[j-1]:  # 인덱스를 0부터 시작하도록 수정
#             dp[j][i] = dp[j-1][i-1] + 1  # 인덱스를 0부터 시작하도록 수정
#         else:
#             dp[j][i] = max(dp[j-1][i], dp[j][i-1])  # 인덱스를 0부터 시작하도록 수정
                    
# print(max(len_a, len_b)-1 - dp[len_b-1][len_a-1])


dp = [[0]*(len_b) for _ in range(len_a)]

for i in range(1, len_a):
    dp[i][0] = i
    
for i in range(1, len_b):
    dp[0][i] = i
    
for i in range(1,len_a):
    for j in range(1, len_b):
        if a[i-1] == b[j-1]:  # 인덱스를 0부터 시작하도록 수정
            dp[i][j] = dp[i-1][j-1]# 인덱스를 0부터 시작하도록 수정
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    
print(dp[len_a-1][len_b-1])
    
    