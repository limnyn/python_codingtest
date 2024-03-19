
'''
n-1개의 사이구간에 대해 좌|우를 나누고, 해당 구간에 대해 인력을 계산해서 0이 가능하다면 처리해서 계산

n-1 사이 구간을 구하는 방법
n개에 대해서 
1부터 n-2까지 반복하면 사이구간에 대해 접근이 가능하다

해당 사이 구간에 대해
left 인력 계산, right 인력 계산



'''


def binary_search(sector_num):
    start = spot[sector_num-1]
    end = spot[sector_num]

    for i in range(50):
        formula = []
        x = (start + end) / 2
        for j in range(n):
            formula.append(weight[j]/((x-spot[j])**2))

        gravitation = sum(formula[:sector_num])-sum(formula[sector_num:])
        if gravitation > 0:
            start = x
        elif gravitation < 0:
            end = x
    return x

for t_c in range(1, int(input())+1):

    n = int(input())

    line = list(map(int, input().split()))
    spot = line[:n]
    weight = line[n:]
    
    gravitation_by_sector = []
        
    result = []
    
    for i in range(1, n):
        result.append("{0:.10f}".format(binary_search(i)))

    print(f"#{t_c}", end=" ")
    for r in result:
        print(f"{r}", end=" ")
    print()


