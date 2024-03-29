'''

제약 사항

    3 <= D <= 13
    1 <= W <= 20
    1 <= K <= D

    백트래킹으로 풀 수 있을 정도의 입력이 주어진다.

문제 접근
    0부터 n-1번째 줄 r에 대해 
    r을 안바꿀때, A로 바꿀때, B로 바꿀때에 대한 재귀적인 접근으로 탐색을 한다.
    만약 현재까지의 최대 약품 투입횟수보다 많으면 가지치기를 통해 더이상 깊게 탐색하지 않는다.
    이러한 방식으로 백트래킹을 구현하면 해결할 수 있을거 같다.

결과
    copy를 사용해서 2차원 그리드를 복사해서 변경 후 처리를 했었는데 0.7초 나왔었다.
    시간초과가 나서 copy 대신 직접 슬라이싱을 통해 값을 할당해주었더니 0.2초로 줄었고 통과했다.
    2차원그리드 복사에 대해서 앞으로 슬라이싱을 통해 해결해봐야 겠다.
    
    
'''

UNVISITED = -2
NON_CHEM = -1
CHEM_A = 0
CHEM_B = 1
CASES = [NON_CHEM, CHEM_A, CHEM_B]

max_count = 1e9


def check(comb):
    grid_c = []
    
    for i in range(D):
        if comb[i] != NON_CHEM:
            grid_c.append([comb[i]]*W)
        else:
            grid_c.append(grid[i][:])

    for c in range(W):
        start = grid_c[0][c]
        cnt = 1
        for r in range(1,D):
            if grid_c[r][c] == start:
                cnt += 1
                if cnt == K:
                    break
            else:
                start = grid_c[r][c]
                cnt = 1
        if cnt != K:
            return False
    return True


def backtracking(comb, count):
    global max_count
    if len(comb) == D:
        if check(comb):
            max_count = min(max_count, count)
        return True
    
    for case in CASES:
        if case != NON_CHEM:
            if count + 1 < max_count:
                backtracking(comb + [case], count + 1)
        else:
            backtracking(comb + [case], count)





if __name__ == "__main__":
    
    for t_c in range(1, int(input()) + 1):
        max_count = 1e9
        D, W, K = map(int, input().split())
        grid = [list(map(int,input().split())) for _ in range(D)]
        backtracking([], 0)
        print(f"#{t_c} {max_count}")

