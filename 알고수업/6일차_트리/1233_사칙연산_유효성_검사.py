



for t_c in range(1, 11):
    result = 1
    n = int(input())
    # print(f"{n}번 반복 예정")
    for i in range(n):
        line = list(input().split())

        # 숫자일 때 자식이 없어야 하고 
            # 숫자일 때 len(line) < 2
        # 기호일 때 자식이 있어야 한다
            # 기호일 때 len(line) == 4
        
        if line[1].isdigit():
            if len(line) > 2:
                result = 0
                
        else:
            if len(line) < 4:
                result = 0
                
    print(f'#{t_c} {result}')

