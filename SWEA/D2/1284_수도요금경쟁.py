T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    a = p * w
    if w <= r:
        b = q
    else:
        b = q + (w - r) * s
    print(f"#{test_case} {min(a,b)}")
