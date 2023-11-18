for t_c in range(1, int(input())+1):
    lines = []
    lens = []
    result = []
    for _ in range(5):
        line = list(input())
        lens.append(len(line))
        lines.append(line)
    for i in range(max(lens)):
        for j in range(5):
            if i < lens[j]:
                result.append(lines[j][i])
    print(f'#{t_c} {"".join(result)}')

