# 상위 k번 이상 등장하는 요소를 추출하라.

# 입력
#     nums = [1,1,1,2,2,3], k = 2
# 출력
#     [1,2]

# nums = [1,1,1,2,2,3]
nums = [3,3,2,2,1]
k = 2

import collections
result = list(zip(*collections.Counter(nums).most_common(k)))[0]
print(result)
