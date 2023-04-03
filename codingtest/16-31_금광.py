# 금광


# n x m 크기의 금광이 있습니다.
# 금광은 1x1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
# 채굴자는 첫번째 열부터 출발하여 금을 캐기 시작합니다.
# 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.
# 이후에 m번에 걸쳐서 매버 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

# 입력 조건
#     첫째 줄에 테스트 케이스 T가 입력됩니다.
#     매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다.
#     둘째 줄에 n x m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다.

# 출력 조건
#     테스트 ㅔ이스마다 채굴자가 어을 수 있는 금의 초디ㅐ 크기를 출력합니다.
#     각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.
    
# 입력 예시
#     2
#     3 4
#     1 3 3 2 2 1 4 1 0 6 4 7
#     4 4
#     1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
    
result = []
    
def dp(grid,n,m):
    dpgrid = [[0] * (m) for _ in range(n)]
    for i in range(n):
        dpgrid[i][0] = grid[i][0]
    
    for c in range(1, m):
        for r in range(n):
            x, z = 0, 0
            
            # 범위 벗어나면 0처리
            if r > 0:
                x = dpgrid[r-1][c-1]
            if r != n-1:
                z = dpgrid[r+1][c-1]                
                

            y = dpgrid[r][c-1]
            dpgrid[r][c] = grid[r][c] + max(x,y,z)
    #2차원 리스트의 마지막 col 값주 최댓값 반환
    return max([i[m-1] for i in dpgrid])
    
    
    
for _ in range(int(input())):
    n, m = map(int, input().split())
    
    line = list(map(int, input().split()))
    tmp = []
    for i in range(n):
        tmp.append(line[m*i:m*(i+1)])
    
    result.append(dp(tmp, n, m))
    
for r in result:
    print(r)
        
