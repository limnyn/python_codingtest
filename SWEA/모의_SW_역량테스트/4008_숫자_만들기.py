
calc_oper = ['+','-','*', '/']


def calc(a, b, oper):
    if oper == 0:
        return a + b
    elif oper == 1:
        return a - b
    elif oper == 2:
        return a * b
    elif oper == 3:
        return int(a / b)

def dfs(idx, answer):
    global minnum, maxnum
    if idx == n-1:
        if minnum > answer:
            minnum = answer
        if maxnum < answer:
            maxnum = answer
        
    
    else:
        for i in range(4):
            if cards[i]:
                cards[i] -= 1
                dfs(idx+1, calc(answer, nums[idx+1], i))
                cards[i] += 1

maxnum = -1e9
minnum = 1e9

for t_c in range(1, int(input())+1):
    minnum = 1e9
    maxnum = -1e9
    n = int(input())
    cards = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    dfs(0,nums[0])
    print(f'#{t_c} {maxnum-minnum}')
    
"""
3 -> testcase
5
2 1 0 1
3 5 3 7 9
6
4 1 0 0
1 2 3 4 5 6 
5
1 1 1 1
9 9 9 9 9 
"""