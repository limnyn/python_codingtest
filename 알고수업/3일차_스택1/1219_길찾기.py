

def solution():
    left = [-1]*100
    right= [-1]*100
    # print(left)
    t_c, n = map(int,input().split())
    input_list = list(map(int,input().split()))
    for i in range(0,n*2,2):
        idx, num = input_list[i], input_list[i+1]
        if left[idx] == -1:
            left[idx] = num
        else:
            right[idx] = num
    

    # 1차원 리스트 2쌍 완료
    
    # stack으로 dfs 구현하기
    visited = [False] * 100

    stack = [0]
    
    while stack:
        src = stack.pop()
        if visited[src] == True:
            continue
        else:
            visited[src] = True
        
        if left[src] != -1:
            dst = left[src]
            if dst == 99:
                return 1
            if visited[dst] == False:
                
                stack.append(dst)
            
        if right[src] != -1:
            dst = right[src]
            if dst == 99:
                return 1
            if visited[dst] == False:
        
                stack.append(dst)
        
    return 0


            
for t_c in range(1,11):
    print(f'#{t_c} {solution()}') 
    
