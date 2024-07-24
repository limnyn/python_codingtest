# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math
def hour_to_min(record):
    hour = int(record[:2])
    minute = int(record[3:5])
    minute += hour * 60
    return minute
    

def solution(fees, records):
    base_time = fees[0] # 기본 시간(분)
    base_fee = fees[1] # 기본 요금(원)
    unit_time = fees[2] # 단위 시간(분)
    unit_fee = fees[3] # 단위 요금(원)
    
    acc_time = [-1] * 10000 # 누적 시간
    car_fee = [0] * 10000 # 요금 계산
    park_start_time = [-1] * 10000 # 입차 시간
    
    for record in records:
        parking_minute = hour_to_min(record) # 현재 시간 to 분
        car_number = int(record[6:10])
        
        if record[11] == 'I': # 입차인 경우
            park_start_time[car_number] = parking_minute
            if acc_time[car_number] == -1:
                acc_time[car_number] = 0
        else:
            minute = parking_minute - park_start_time[car_number]
            acc_time[car_number] += minute
            
            park_start_time[car_number] = -1
            
    answer = []
            
    for car_number in range(10000):
        if park_start_time[car_number] != -1:
            minute = park_start_time[car_number]
            gap_minute = (23*60 + 59) - minute
            acc_time[car_number] += gap_minute
            
        if acc_time[car_number] != -1:
            if acc_time[car_number] <= base_time:
                fee = base_fee
            else:
                fee = base_fee + (math.ceil((acc_time[car_number] - base_time) / unit_time)) * unit_fee
            car_fee[car_number] += fee
            answer.append(car_fee[car_number])

    

    return answer