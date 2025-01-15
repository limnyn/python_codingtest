# https://www.acmicpc.net/problem/12904
"""
문자열 초기값 S가 주어졌을때, 두 가지 연산만을 통해서 결과값 T 상태를 만들 수 있는지 판별

1. 문자열의 뒤에 A를 추가한다.
2. 문자열을 뒤집고 뒤에 B를 추가한다.

A 제거
    ABBA - ABB
B 제거
    ABB - AB - BA
A 제거
    BA - A


[그리디]
    T의 마지막 글자가 A라면
        - 문자열의 뒤에 A를 추가한다.
    T의 마지막 글자가 B라면
        - 문자열을 뒤집고 뒤에 B를 추가한다.
"""

import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    S = list(input())
    T = list(input())

    while len(T):
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            T.reverse()
        
        if T == S:
            print(1)
            exit()
    print(0)