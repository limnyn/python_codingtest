

'''

N*M 직사각형 2차원 배열에 0 이상의 값이 주어진다.


로봇이 왕복이동한다 - 쓰레기까지의 거리 * 2 만큼 비용

5 <= N, M <= 20

쓰레기에 대해 비용과 거리를 두 개 모으고, 
해당 쓰레기와 비용에 대해 최대로 채울 수 있는 문제
    
-> dp로 해결

'''

def robot():
  n, m, battery = map(int, input().split())

  grid = [list(map(int, input().split())) for _ in range(m)]
  
  gas_list = []
  trash_list = []
  # 시작점 찾기
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1:
        start = [i, j]
  
  #쓰레기 찾기
  for i in range(n-1, -1, -1):
    for j in range(m-1,-1, -1):
      if grid[i][j] != 1 and grid[i][j] != 0:
        gas = (abs(i-start[0]) + abs(j-start[1]))*2
        trash = grid[i][j]
        gas_list.append(gas)
        trash_list.append(trash)


  # 배낭 문제처럼 배터리를 만족하는 최대 쓰레기 양 계산
  dp = [[0]*(battery+1) for _ in range(len(trash_list) + 1)]

  for r in range(1, len(trash_list)+1):
    for c in range(1, battery + 1):
      if c - gas_list[r-1] >= 0:
        dp[r][c] = max(dp[r-1][c-gas_list[r-1]] + trash_list[r-1], dp[r-1][c])
      else:
        dp[r][c] = dp[r-1][c]

  return dp[-1][-1] 




for test_case in range(1, int(input())+1):
  print(f"#{test_case} {robot()}")



'''
[입력 예시]
3
5 5 10
0 0 0 50 0
0 0 20 0 0
0 0 10 0 0
0 10 1 10 0
0 0 0 0 0
5 5 10
100 0 0 0 0
0 0 0 0 0
0 0 10 0 0
0 10 1 10 0
0 0 10 0 0
10 10 50
0 0 40 0 0 0 0 0 0 0
0 0 0 0 0 0 0 10 0 0
0 0 10 0 0 20 0 0 0 0
0 20 0 0 0 0 0 0 0 20
0 0 0 0 1 0 10 0 0 0
0 0 50 0 0 0 0 0 0 0
0 0 0 0 10 0 30 0 10 0
0 40 0 0 0 0 0 0 0 0
0 0 0 60 0 0 0 10 0 0
0 0 0 0 0 0 30 0 0 0



[출력 예시]
#1 1
#2 2
#3 3

'''