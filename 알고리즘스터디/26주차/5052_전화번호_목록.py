# https://www.acmicpc.net/problem/5052
'''
[문제]
전화번호 목록에서 한 전화번호가 다른 전화번호의 접두어인 경우 NO 출력
해당 경우가 존재하지 않는 경우 YES 출력

[접근]
트라이
트라이 구조에 전화번호를 짧은 길이 순으로 삽입
중복이 발생하면 break 하고 NO 출력
전체 삽입이 문제없이 진행되면 YES 출력

[구조]

입력값에 대해 짧은 순으로 정렬
트라이 -> 노드 생성
트라이에 삽입 도중 이미 존재했던 값 삽입하면 중단하고 NO 출력
'''

import sys
def input(): return sys.stdin.readline().rstrip()


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        
class Trie:
    
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        global result
        
        current_node = self.head
        
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            if current_node.data != None:
                result = "NO" 
        current_node.data = string
        
    
if __name__ == "__main__":
    
    
    for t_c in range(int(input())):
        trie = Trie()
        result = "YES"
        numbers = []
        
        for _ in range(int(input())):
            numbers.append(input()) 
        numbers.sort(key = lambda x : (len(x), x))
        
        for number in numbers:
            trie.insert(number)
            
            if result == 'NO':
                break
            
        print(result)