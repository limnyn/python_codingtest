T = int(input())
m_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    month_a, day_a, month_b, day_b = map(int, input().split())
    day_sum_a = 0
    for i in range(month_a - 1):
        day_sum_a += m_days[i]
    day_sum_a += day_a

    day_sum_b = 0
    for i in range(month_b - 1):
        day_sum_b += m_days[i]
    day_sum_b += day_b

    print(f"#{test_case} {day_sum_b - day_sum_a + 1}")
