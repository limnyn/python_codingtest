# 입력 조건
#     첫쨰 줄에 떡의 개수 N과 요철한 떡의 길이 M이 주어진다. (1 <= N <= 1000000, 1<= M <= 2000000000)
#     둘째 줄에는 떡의 개별 높이가 주어진다. 
#     떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양 만큼 떡을 사갈 수 있다.
#     높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

# 적어도 M만큼의 떡을집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

# 입력 예시
#     4 6
#     19 15 10 17

# 출력 예시
#     15
    
    


stock, order = list(map(int, input().split()))
items = set(map(int, input().split()))

start = 1
end = max(items) 
result = 0
while(start<=end):
    cut = (end + start) //2
    leftRicecake = 0
    for i in items:
        if i - cut > 0:
            leftRicecake += i - cut 
    if leftRicecake < order:
        end = cut -1 
    else:
        result = cut
        start = cut + 1
        

print(result)    
                


