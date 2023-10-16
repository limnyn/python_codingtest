T = int(input())

for test_case in range(1, T + 1):
    visited = [0] * 10
    n = int(input())

    k = 1
    # print(number)
    while 1:
        number = [c for c in str(n * k)]
        for c in number:
            if visited[int(c)] == 0:
                visited[int(c)] = 1
        if sum(visited) == 10:
            break
        k += 1

    print(f"#{test_case} {n*k}")
