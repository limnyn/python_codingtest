# 못생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수를 의미합니다.
# 다시말해 오직 2, 3, 5를 약수로 가지는 합성수를 의미합니다.
# 1은 못생긴 수라고 가정합니다.
# 따라서 못생긴 수들은 [1,2,3,4,5,6,7,8,9,10,12,15,...] 순으로 이어지게 됩니다.
# 이때, n번째 못생긴 수를 찾는 프로그램을 작성하세요.

n = int(input())

ugly = [0] * n
ugly[0] = 1 
i2 = i3 = i5 = 0

next2, next3, next5 = 2, 3, 5

for l in range(1, n):
    ugly[l] = min(next2, next3, next5)
    
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])


##코드2
# n = int(input())

# nums = [2, 3, 5]
# dp = [0]*1001
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[5] = 5
# for i in range(1,10):
#     for num1 in nums:
#         for num2 in nums:
#             a = pow(num1, i)*num2
#             if a < 1001:
#                 dp[a] = a

# remove_set = {0}

# dp = [i for i in dp if i not in remove_set]
        
# # 2 3 5
# # 22 23 25
# # 32 33 35
# # 55
# # 235235
# # 222 223 225
# # 333 335
# # 555
# # 235235235

# print(dp[n-1])