# 0과 1로만 이루어진 문자열 S
# S에 있는 모든 숫자를 전부 같게 만들려고 합니다. 
# S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집습니다.
# 뒤집는것은  1을 0으로, 0을 1로 바꾸는 것입니다.
# S = 0001100 일 때
    # 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 한번에 모두 같은 숫자로 만들 수 있습니다.

# 문자열 S가 주어졌을 때, 행동의 최소 횟수

# 입력 조건
#     첫째 줄에 0과 1로만 이루어진 문자열 S가 주어집니다. S의 길이는 100만 보다 작습니다.

# 출력 조건
#     첫째줄에 다솜이가 해야하는 행동의 최소 횟수를 출력합니다.

# 입력 예시
#     00011000

# 출력 예시
#     1

S = input()

def act(S):
    # blob => list which have strings made of same nums
    blob = []
    start = 0
    prev = S[0]
    for i, s in enumerate(S):
        if s != prev:
            blob.append(S[start:i])
            start =  i
        prev = s
        
    blob.append(S[start:len(S)])
    
    return len(blob)//2

    
            

print(act(S))