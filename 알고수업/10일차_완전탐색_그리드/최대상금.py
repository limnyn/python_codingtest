'''
(123, 3)
일 때 (12,13,23) 변경
12 -> (213, 2) , 12 ->(1,2,3,1) 13 ->, 23 -> 
13 -> (321, 2), 
이런식으로 완전탐색 할 수 있다.

2차원 배열 또는 dict를 만들어서
해당 값이 검색했던 값인지 확인해서 있으면 계산 생략

'''

num, s = map(int, input().split())

check_board = [[-1]*10 for _ in range(999999)]
# print(check_board)

#check ,값이 있다면 
#           break
#       값이 없다면 값을 넣고
#           해당 값을 전역변수와 비교하고 최대값 갱신
from itertools import combinations
result = -1e9
def check(num, s):
    global result
    if s == 0:
        return
    combs = combinations([x for x in range(len(str(num)))], 2)
    for comb in combs:
        num = list(map(int, str(num)))
        a, b = num[comb[0]], num[comb[1]]
        num[comb[1]] = a
        num[comb[0]] = b
        num = int(''.join(map(str, num)))
        
        if check_board[num][s] == -1:
            check_board[num][s] = num
            result = max(result, num)
            check(num, s-1)
        else:
            continue

    
# for i in range(s):
check(num, s)
print(result)