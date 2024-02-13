T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import Counter

for test_case in range(1, T + 1):
    t_c = int(input())
    cnt = Counter(list(map(int, input().split()))).most_common()
    cnt.sort(key=lambda x: -x[1])
    result = cnt[0][0]
    print(f"#{t_c} {result}")
