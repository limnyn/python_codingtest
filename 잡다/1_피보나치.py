def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def solution(n, m):
    return fibonacci(n) * fibonacci(m)

print(solution(7, 5))