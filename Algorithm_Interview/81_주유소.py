# 원형으로 경로가 연결된 주유소 목록이 있다.
# 각 주유소는 gas[i]만큼의 기름을 갖고 있으며,
# 다음 주유소로 이동하는데 cost[i]가 필요하다.
# 기름이 부족하면 이동할 수 없다고 할 때 모든 주유소를 방문할 수 있는 출발점의 인덱스를 출력하라.
# 출발저이 존재하지 않을 경우 -1을 리턴하며, 출발점은 유일하다.

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]


def canCompleteCircuit(gas:list, cost:list):
    if sum(gas) < sum(cost):
        return -1
    start, fuel = 0, 0
    
    for i in range(len(gas)):
        # 출발점이 안 되는 지점 판별
        if gas[i] + fuel < cost[i]:
            start = i +1
            fuel = 0
        else:
            fuel += gas[i]-cost[i]
    return start 
    
        
print(canCompleteCircuit(gas, cost))