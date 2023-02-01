# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
import sys
array = [7,1,5,3,6,4]

min_num = sys.maxsize
max_num = -sys.maxsize
profit = 0
for i in range(len(array)):
    min_num = min(array[i], min_num)
    profit = max(profit, array[i]-min_num)



print(profit)   