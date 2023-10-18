T = int(input())
for t_c in range(1, T + 1):
    n, a, b = map(int, input().split())
    result = 1e9
    for r in range(1, n):
        for c in range(1, n):
            if r * c > n:
                break
            else:
                result = min((a * abs(r - c) + b * (n - r * c)), result)

    print(f"#{t_c} {result}")
