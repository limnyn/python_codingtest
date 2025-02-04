# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import defaultdict
def solution(topping):
    """
    스위핑
    1. 전체를 동생 것이라 가정하고 토핑 갯수, 종류를 센다.
    2. 0번 인덱스 끝까지 탐색하면서 좌 우의 토핑 갯수가 같아지는 경우를 센다.
    """
    cheulsoo = [0] * 10001
    cheulsoo_cnt = 0
    
    bro = [0] * 10001
    bro_cnt = 0
    
    for t in topping:
        if bro[t] == 0:
            bro_cnt += 1
        bro[t] += 1

    answer = 0
    
    for i in range(len(topping)):
        
        topp = topping[i]
        
        if cheulsoo[topp] == 0:
            cheulsoo_cnt += 1
        cheulsoo[topp] += 1
        
        bro[topp] -= 1
        
        if bro[topp] == 0:
            bro_cnt -= 1
            
        if cheulsoo_cnt == bro_cnt:
            answer += 1
        
            
    return answer