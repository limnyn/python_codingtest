# https://school.programmers.co.kr/learn/courses/30/lessons/181187

import math
def solution(r1, r2):

    count = 0
    for i in range(1, r2):
        max_y = math.floor(math.sqrt(r2*r2 - i*i))
        min_y = 0
        if i >= r1:
            min_y = 0
        else:
            min_y = math.ceil(math.sqrt(abs(i*i - r1*r1)))
        count += max_y - min_y+1  
    return 4*(count + 1)

    
            
    
    
    # return count + point_count + 8

# 1 ≤ r1 < r2 ≤ 1,000,000


