# 팩토리얼
# 예제 5번 / 2가지 방식으로 구현한 팩토리얼 예제

# 반복적으로 구현
def factorial_iterative(n):
    sum = 1
    for i in range (n):
        sum *= i+1
    return sum

print(factorial_iterative(5))

# 재귀적으로 구현

def factorial_recursive(n):
    if n > 1:
        return n * factorial_recursive(n-1)
    elif n <= 1:
        return 1

print(factorial_recursive(5))
