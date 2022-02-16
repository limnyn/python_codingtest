# n차원 리스트 초기화
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화



n = 10
a = [0] * n
print(a)

# 리스트 컴프리헨션
# 리스트를 조건/반복문을 통해 초기화가 가능하다.
    # 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
arr = [i for i in range(20) if i % 2 == 1]
print(arr)

    # 1부터 9까지의 수의 제곱 값을 포함하는 리스트
arr = [i * i for i in range(1,10)]
print(arr)

# N x M 크기의 2차원 리스트 초기화
n = 3
m = 3
arr = [[0]*m for _ in range(n)]
print(arr)

score = 85

if score >= 90:
    print('A')
elif score >=80:
    print('B')
elif score >=80:
    print('C')
else:
    print('D')        

# 한줄에 표현하기
result = 'Success' if score >= 80 else 'fail'
print(result)

# 한줄에 표현하기2 - 리스트에서 특정값 제거
a = [1, 2, 3, 4, 5, 5, 5]
removeSet = {3, 5}
result = [i for i in a if i not in removeSet]
print(result)


# 파이썬 조건문 내 부등식
x = 15
if 0 < x < 20:  #라고 부등식을 쓸 수 있다.
    print('x 는 0~20 사이의 수입니다.')
    


# # input 사용시의 시간 초과를 막기 위한 sys.stdin.readliine().rstrip() 
# # readline()은 enter를 \n문자로 인식하기 때문에 rstrip()함수를 호출해서 공백 문자를 제거한다.
# import sys
# data = sys.stdin.readline().rstrip()
# print(data)


# print함수 내부에 , 사용시 공백으로 처리된다
# print함수에 여러 종류의 변수 사용시 문자열로 변환하지 않으면 에러를 반환한다.
answer = 7
# 1.str형변환
print('정답은', str(answer), '입니다.')
# 2.f-string
print(f'정답은 {answer} 입니다')





# 주요 라이브러리 문법과 유의점
#     내장함수 : input, sum 등 import없이 사용가능한 함수
#     itertools : 반복되는 형태의 데이터 처리, 순열과 조합 라이브러리를 제공한다.
#     heapq : 힙 기능을 제공하는 라이브러리.
#     bisect : 이진 탐색 기능을 제공하는 라이브러리이다.
#     collections : 덱, 카운터 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.
#     math : 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 메서드부터 파이와 같은 상수를 포함하고 있다.

# 내장함수 
    # sum() == iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환
    # min(), max() == 파라미터가 두개 이상일때 가장 작은, 큰 값 반환
    # eval() == 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
result = eval("(3+5)*7")
print(result)
    # sorted() == iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다.
result = sorted([9,1,8,5,4])
print(result)
result = sorted(result, reverse = True)
print(result)
        # 특정 기준에 따라 정렬하는것도 가능 ex)리스트 내부 튜플의 2번째원소를 기준할때
            # ex)리스트 내부 튜플의 2번째 원소를 기준으로 내림차순 할 때

result = sorted([('홍길동', 35), ('이순신', 72), ('아무개', 50)], key = lambda x : x[1], reverse= True)
    # 리스트 같은 iterable 객체는 기본적으로 sort()메소드 포함, 따라서 sorted함수 호출이 불필요하다.
data = [9,1,8,5,4]
data.sort()
print(data)



# itertools
    # permutations, combinations 등의 순열과 조합 클래스들
        # permutations는 리스트같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산
            # 클래스이기 때문에 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import permutations
from operator import le
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
        # combinations는 순서를 고려하지 않은 r개의 데이터를 나열한다. 마찬가지로 리스트 자료형으로 변환하여 사용한다.
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result) 
        # product는 iterable객체에서 r개의 데이터를뽑아 나열하는데 순서를 두고 중복하여 뽑는다.
            # product 객체 초기화시에는 뽑고자하는 데이터의 수를 repeat 속성 값으로 넣어준다.
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)
        # combinations는 순서를 고려하지 않은 r개의 데이터를 나열한다. 같은 원소를 순서 상관없이 중복해서 포함이 가능하다
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result) 



# heapq
    # heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.
    # 파이썬의 힙은 최소힙으로 구성되어 있다.
    # heapq에 원소 삽입 시 heapq.heappush(), 힙에서 원소를 꺼낼때는 heapq.ㅗheappop()메서드 사용.

    # 힙 정렬읠 heapq로 구현
import heapq
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)

    # 힙의 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
    # 파이썬에서는 최대 힙을 제공하지 않는다. 최대 힙 구현시 원소삽입전 -부호를 붙이고 원소를 꺼낼때 -부호를 다시 붙인다.


# bisect
    # bisect 라이브러리는 정렬된 배열에서 특정한 원소를 찾아야 할 때 효과적으로 사용 가능하다.
    # bisect_left()와 bisect_right()가 주로 사용되며 시간복잡도는 O에 동작한다.
        
    # bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
    # bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

    # 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구하기에 사용가능
        # 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
            # 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
            # 값이 [-1, 3]범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))



# collections
    # deque, counter등의 자료구조를 제공하느 ㄴ라이브러리
    # deque를 사용해 큐를 구현한다.
    # list는 뒤쪽의 원소의 추가/제거 시간복잡도는 O(1)이지만 가장 앞쪽에 있는 원소 추가/제거 시간복잡도는O(N)이다
    # list의 앞쪽 데이터 처리에 많은 시간이 걸리기 때문에 deque를 사용하기도한다.
    # deque는 인덱싱, 슬라이싱 등의 기능을 사용할 수 없지만, 데이터의 시작/끝부분에 데이터 추가/삭제시 빠르게 할 수 있다.

    # popleft() == deque의 첫 번째 원소 제거
    # pop() == 마지막 원소 제거
    # appendleft(x) == deque의 첫 번째 인덱스에 x 삽입
    # append(x) == deque의 마지막 인덱스에 x 삽입 
from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))
    # collections 라이브러리의 Counter는 등장 횟수를 센다
    # iterable 객제차 주어졌을 때, 해당 객체 내부의 원소가 몇번씩 등장했는지 알려준다.
from collections import Counter
counter = Counter(['red', 'blue', 'red','green','blue','blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 변환



# math
    # 수학적인 기능을 포함하는 라이브러리
    # 팩토리얼, 제곱근, 최대공약수(GCD) 등을 계산해주는 기능을 포함하고 있다.
        # factorial(x) == x!값을 반환한다.
import math
print(math.factorial(5))
        # sqrt(x) == 제곱근을 반환한다
print(math.sqrt(6))
        # gcd(a, b) == a와 b의 최대공약수를 반환한다.
print(math.gcd(21,14))
        # math 라이브러리는 pi 와 e도 제공한다
print(math.e)
print(math.pi)
        

# 자신만의 알고리즘 노트 만들기
    # 메서드를 만들어 라이브러리화 시키기




