#n명이 모여있을 때 생일이 같은 사람이 존재할 확률 출력하기 ->10만번 실험해서 확률 추출
import random

same_birthdays = 0 
n = int(input())
trials = int(input())


for i in range(trials):
    birthdays = []

    for i in range(n):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays+=1
            break
        birthdays.append(birthday)
    
result = (same_birthdays / trials) * 100
print(f'{result}%')

