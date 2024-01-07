

for t_c in range(1, int(input())+1):
    n, m = map(int, input().split())
    n_l = list(map(int, input().split()))
    m_l = list(map(int, input().split())) 
       
    if n < m:
        short_l = n_l
        long_l = m_l
    else:
        short_l = m_l
        long_l = n_l
    
    max_num = -1e9
    
    for i in range(len(long_l)-len(short_l)+1):
        loop_sum = 0
        for j in range(len(short_l)):
            loop_sum += short_l[j]*long_l[j+i]    
        
        max_num = max(max_num, loop_sum)
        
        
        
    print(f'#{t_c} {max_num}')
        
    
        
        