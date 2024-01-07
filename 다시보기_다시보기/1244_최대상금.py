# https://velog.io/@seungjae/SWEA-1244.-SW-%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0-%EC%9D%91%EC%9A%A9-2%EC%9D%BC%EC%B0%A8-%EC%B5%9C%EB%8C%80-%EC%83%81%EA%B8%88-Python-%EC%99%84%EC%A0%84%ED%83%90%EC%83%89

# 6! 720개


from collections import deque

for t_c in range(int(input())):
    num, n = input().split()
    n = int(n)

    same = False  # 만약 같은 게 존재한다면 홀수 짝수 상관없이 n이하인 모든 경우 가능
    # 같은 게 존재하지 않는다면 홀수, 짝수 상관있는 n이하 경우만 가능

    dct = {num: 0}
    dq = deque()
    dq.append(num)

    while dq:
        num = dq.popleft()
        for i, c in enumerate(num):
            for j in range(i + 1, len(num)):
                tmp = list(num)
                tmp[i], tmp[j] = num[j], num[i]
                if num[i] == num[j]:
                    same = True
                tmp = "".join(tmp)
                if dct.get(tmp) == None:
                    dct[tmp] = dct[num] + 1
                    dq.append(tmp)

    max_num = -1

    for k, v in dct.items():
        if v <= n:
            if same:
                max_num = max(max_num, int(k))
            elif v % 2 == n % 2:
                max_num = max(max_num, int(k))

    print("#" + str(t_c + 1) + " " + str(max_num))


# 123456
# # 654321에 대해 몇번 바꿔서 만들 수 있는가에 대해 생각
# 123을 예로 들어, 최소로 바꾸는 수 n에 대해
# 123 0
# 213 1
# 321 1
# 132 1
# 312 2
# 231 2

# 같은수가 없을 때
# n % 2 == 0: 0~ n까지 짝수 중 max
# n % 2 == 1: 1~ n까지 홀수중 max
# 같은수가 있으면 n이하 모든 수
