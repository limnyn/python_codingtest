# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
nums = [-1, 0, 1, 2, -1, -4]

nums.sort()
# print(nums)

result = []

# Two pointer
for i in range(len(nums)-2):
    left = i+1
    right = len(nums)-1
    while left < right:
        sum = nums[i]+nums[left]+nums[right] 
        if sum == 0:
            result.append([nums[i],nums[left],nums[right]])
            break
        elif sum < 0:
            left+=1
        elif sum > 0:
            right-=1
    
print(result)







# # Brute force
# for i in range(len(nums) -2):
#     if i> 0 and nums[i] == nums[i - 1]:
#         continue
#     for j in range(i+1,len(nums)-1):
#         if j> 0 and nums[j] == nums[j - 1]:
#             continue
#         for k in range(i+2, len(nums)):
#             if k> 0 and nums[k] == nums[k - 1]:
#                 continue
#             if nums[i]+ nums[j] + nums[k] == 0:
#                 result.append([nums[i],nums[j],nums[k]])
            
            

# print(result)