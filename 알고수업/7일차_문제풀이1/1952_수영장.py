"""


"""
day_by_month = []
cost = []
mincost = 1e9
def dfs(idx, answer):
    global mincost
    if idx >=12:
        if answer < mincost:
            mincost = answer
        
    
    else:
        # 1일권
        dfs(idx + 1, answer + day_by_month[idx]*cost[0])
        # 1달권
        dfs(idx + 1, answer + cost[1])
        # 3달권
        if idx <= 9:
            dfs(idx + 3, answer + cost[2])
        if idx == 0:
            dfs(idx + 12 ,answer + cost[3])

for t_c in range(1, int(input())+1):
    mincost = 1e9
    cost = list(map(int,input().split()))
    day_by_month = list(map(int, input().split()))
    dfs(0, 0)
    print(f"#{t_c} {mincost}")