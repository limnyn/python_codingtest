for t_c in range(1, int(input()) + 1):
    n, m, k, a, b = map(int, input().split())
    a -= 1
    b -= 1
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    tk = list(map(int, input().split()))
    """
    접수창구
        1. 여러 고객 대기중에는 고객번호 낮은순 우선
        2. 빈 창구가 여려 곳인 경우 접수 창구 번호가 작은곳으로
        
    정비창구
        1. 여러 고객 대기 중에는 먼저 기다리는 고객 우선
        2. 동시간대에 대기를 시작한 경우 접수창구 번호가 작은 고객이 우선
        빈 창구가 여러 곳인 경우 창구번호 작은 곳으로 간다.
        
    """

    visited_A = [[0, 0] for _ in range(len(ai))]
    visited_B = [[0, 0] for _ in range(len(bi))]
    wait_A = list()
    wait_B = list()
    ans1 = list()
    ans2 = list()
    check = [0] * k

    while 1:
        if sum(check) == k:
            break

        for i in range(0, len(tk)):
            if tk[i] == 0:  # 접수처에 i가 도착
                wait_A.append(i)
                tk[i] = -1
            elif tk[i] > 0:
                tk[i] -= 1

        # A -> B
        # wait_B -> B로도 체크해줘야함
        for i in range(0, len(visited_A)):
            if visited_A[i][1] > 0:
                visited_A[i][1] -= 1
                if visited_A[i][1] == 0:  # 시간 다 되면 접수처 비었다는 의미
                    wait_B.append(visited_A[i][0])
                    visited_A[i] = [0, 0]

        # B -> End
        for i in range(0, len(visited_B)):  # 정비소 시간 줄여주기
            if visited_B[i][1] > 0:
                visited_B[i][1] -= 1
                if visited_B[i][1] == 0:  # 시간 다 되면
                    check[visited_B[i][0]] = 1
                    visited_B[i] = [0, 0]

        #############################################시간 -1 하기

        # T -> A
        wait_A.sort()  # 고객번호가 낮은 순서대로 접수
        for j in range(0, len(ai)):
            if visited_A[j][1] == 0 and wait_A:  # 접수처에 빈자리 있으면
                tmp = wait_A.pop(0)
                visited_A[j] = [tmp, ai[j]]  # 사람idx, 남은 시간
                if j == a:
                    ans1.append(tmp)

        for j in range(0, len(bi)):
            if visited_B[j][i] == 0 and wait_B:  # 정비소에 빈자리 있으면
                tmp = wait_B.pop(0)
                visited_B[j] = [tmp, bi[j]]  # 사람idx, 남은시간
                if b == j:
                    ans2.append(tmp)

    answer = set(ans1).intersection(ans2)
    final = sum(answer) + len(answer)
    if final == 0:
        final - 1
    print(final)

# https://qrlagusdn.tistory.com/93
