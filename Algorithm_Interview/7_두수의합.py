# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
nums = [2, 7, 11, 15]
target = 9

subs = {}
for i, num in enumerate(nums):
    subs[num] = i


for i, num in enumerate(nums):
    if target - num in subs and i != subs[target-num]:
        print(nums[i],"+",nums[subs[target-num]])
        break


