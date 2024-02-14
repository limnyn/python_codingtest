

for t_c in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    max_view = 0
    for i in range(2, n-2):
        view = 0
        for h in range(buildings[i], -1, -1):
            
            if (buildings[i-2] < h and buildings[i-1] < h and 
                buildings[i+1] < h and buildings[i+2] < h):
                view+=1
            else:
                break
        max_view += view
        
    print(f'#{t_c} {max_view}')


"""
이전 코드와 다르게 제외조건을 덜 처리했지만
사실상 동일하게 작동하고
if 조건문이 한눈에 더 잘들어오게 바꾼 것 같다
"""