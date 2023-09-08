# https://school.programmers.co.kr/learn/courses/30/lessons/155651

# book_time = [
#     ["15:00", "17:00"],
#     ["16:40", "18:20"],
#     ["14:20", "15:20"],
#     ["14:10", "19:20"],
#     ["18:20", "21:20"],
# ]


book_time = [["16:00", "16:10"], ["16:20", "16:30"], ["16:40", "16:50"]]


from collections import defaultdict


def solution(book_time):
    time_line = []
    time_table = defaultdict(int)
    for time in book_time:
        times = []
        for i in range(2):
            minute = int(time[i][:2]) * 60 + int(time[i][3:])
            times.append(minute)
        time_table[times[0]] += 1
        time_table[times[1] + 10] -= 1
        time_line.append(times)
    time_table = sorted(time_table.items(), key=lambda x: x[0])

    count = 0
    max_count = 0
    for time, i in time_table:
        count += i
        max_count = max(count, max_count)

    return max_count


print(solution(book_time))
