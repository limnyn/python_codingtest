def possible_time(S):
    # 각 숫자마다 켜지는 segment를 나타내는 2차원 리스트
    segment = [[1, 1, 1, 1, 1, 1, 0], # 0
               [0, 1, 1, 0, 0, 0, 0], # 1
               [1, 1, 0, 1, 1, 0, 1], # 2
               [1, 1, 1, 1, 0, 0, 1], # 3
               [0, 1, 1, 0, 0, 1, 1], # 4
               [1, 0, 1, 1, 0, 1, 1], # 5
               [1, 0, 1, 1, 1, 1, 1], # 6
               [1, 1, 1, 0, 0, 0, 0], # 7
               [1, 1, 1, 1, 1, 1, 1], # 8
               [1, 1, 1, 1, 0, 1, 1]] # 9
    
    result = []
    for h1 in range(2):
        for h2 in range(10):
            for m1 in range(6):
                for m2 in range(10):
                    time = [0, 0, 0, 0] # 시간을 나타내는 리스트
                    # 시간을 설정
                    time[0] = h1 * 2 # 0 또는 2
                    time[1] = h2
                    time[2] = m1
                    time[3] = m2
                    # 가능한 시간인지 체크
                    valid_time = True
                    for i in range(4):
                        if not all([s == 1 for s in [S[i][j] for j in range(7) if segment[time[i]][j] == 1]]):
                            valid_time = False
                            break
                    # 가능한 시간이면 결과에 추가
                    if valid_time:
                        result.append(time)
    # 24시간을 고려하여 결과 반환
    return [r if r[0] < 24 else [r[0]-24, r[1], r[2], r[3]] for r in result]


S =[[1,1,0,0,0,0,0],[1,1,1,0,0,0,0],[0,0,0,0,0,1,1],[0,1,1,0,1,0,0]]
print(possible_time(S))