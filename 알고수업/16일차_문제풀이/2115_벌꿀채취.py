# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu

'''
각 좌표별로 돌면서
그 좌표의 꿀통 최대 값을들 갱신하고,
겹치지 않는 선에서 꿀통을 두개뽑는 결과를 출력하면 된다

각 꿀통에 대해 최대값을 구하는 것은
    m이 5이하이기 때문에, 멱집합을 뽑아서
    각 부분집합별로 C를 초과하지 않는 값을 비교해가며
    최대값을 찾을 수 있다.
'''

from itertools import combinations
def max_honey(r,c):
    result = 0
    if c + m - 1 >= n:
        return result
    line = grid[r][c:c+m]

    
    for i in range(m):
        comb = combinations(line, i+1)
        for subset in comb:
            tmp = 0
            tmp_pow = 0
            for num in subset:
                tmp += num
                tmp_pow += num**2
            if tmp <= honey_max:
                result = max(result, tmp_pow)
    # print(r, c, result)
    return result
        
for t_c in range(1, int(input())+1):
    n, m, honey_max = map(int, input().split())
    grid = []

    for _ in range(n):
        grid.append(list(map(int,input().split())))

    results = [[0] * (n-m+1) for _ in range(n)]
    for r in range(n):
        for c in range(0,n-m+1):
            results[r][c] = max_honey(r, c)


    answer = 0
    for r1 in range(n):
        for c1 in range(n-m+1):
            for r2 in range(r1,n):
                for c2 in range(n-m+1):
                    if r1==r2 and c2<c1+m:
                        #겹치는 부분은 계산을 안해줘야 한다
                        continue
                    answer = max(answer, results[r1][c1] + results[r2][c2])
    print(f"#{t_c} {answer}")



                        
                        
                        
    # line의 값들에 대한 powerset을 만들고
    # if sum(부분집합) <= 10:
    #     max_result = (max_resultm sum([x*x for x in 부분집합]))
    # return max_result 를 수행한다.
    

    
    # for i in range(m):
    #     comb = combinations(line, i)
    #     for subset in comb:
    #         tmp = 0
    #         tmp_pow2
    #         for n in subset:
    #             tmp += n
    #             tmp_pow += n**2
    #         if tmp <= honey_max:
    #             result = max(result, tmp_pow)
    # return result
        