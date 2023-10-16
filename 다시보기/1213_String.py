for test_case in range(1, 11):
    t = int(input())
    a = input()
    b = input()
    count = 0
    result = b.split(a)
    count = len(result) - 1

    print(f"#{t} {count}")
