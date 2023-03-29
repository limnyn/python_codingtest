# https://www.acmicpc.net/problem/1715

import sys, heapq
input = sys.stdin.readline
n = int(input())
deck = []

for _ in range(n):
    deck.append(int(input()))

def solution(deck):
    
    mte = 0
    heapq.heapify(deck)
    while len(deck) > 1:
        a = heapq.heappop(deck) 
        b = heapq.heappop(deck)   
        heapq.heappush(deck, a+b)
        mte += (a + b)

    return mte


print(solution(deck))

