# n차원 리스트 초기화
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트 컴프리헨션
# 리스트를 조건/반복문을 통해 초기화가 가능하다.
    # 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
arr = [i for i in range(20) if i % 2 == 1]
print(arr)

    # 1부터 9까지의 수의 제곱 값을 포함하는 리스트
arr = [i * i for i in range(1,10)]
print(arr)

# N x M 크기의 2차원 리스트 초기화
n = 3
m = 3
arr = [[0]*m for _ in range(n)]
print(arr)

score = 85

if score >= 90:
    print('A')
elif score >=80:
    print('B')
elif score >=80:
    print('C')
else:
    print('D')        

# 한줄에 표현하기
result = 'Success' if score >= 80 else 'fail'
print(result)

# 한줄에 표현하기2 - 리스트에서 특정값 제거
a = [1, 2, 3, 4, 5, 5, 5]
removeSet = {3, 5}
result = [i for i in a if i not in removeSet]
print(result)


# 파이썬 조건문 내 부등식
x = 15
if 0 < x < 20:  #라고 부등식을 쓸 수 있다.
    print('x 는 0~20 사이의 수입니다.')
    


