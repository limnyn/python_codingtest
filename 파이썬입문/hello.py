# # a = 12
# # b = 4

# # #몫은 //
# # print(a//b)
# # #나머지는 %
# # print(a%b)
# # #나누기값 /
# # print(a/b)
# # #제곱은 ** 
# # print(a**b)
# # #^는 비트이동?
# # print(a^2)
# # print(type(a+b))

# # a = 'python'
# # b = ' is fun'
# # c = a  + b
# # print(c* 100)

# # # #문자열 자료형
# # # #문자열[이상:미민:간격]
# # # #문자열[번호], 음수일 경우 뒤에서부터 시작
# # # #문자열 출력시 기준
# # z = "Life is too short, Need  Python"
# # # # #역출력
# # print(z[::]) 

# # a = "I eat %d apples." % 3
# # b = 'I eat ' + str(3) + " apples" 
# # print(a)
# # print(b)
# # number = 30
# # day = "Three"
# # c = "I eat %d apples. so I was sick for %s days." % (number, day)
# # print(c)


# # #포맷 사용법
# # name = "이문현"
# # age = 24

# # x = f"나의 이름음 {name}이고 {age}세 입니다. "
# # print(x)

# # 문자열 함수
# # .count(a) = 문자열에서 a 갯수 반환
# # .find(a) = 문자열에서 a의 인덱스 반환 없으면 -1 반환
# # .index(a) = 문자열에서 a인덱스 반환 없으면 에러'

# # # 리스트[] = 추가삭제 가능, 튜플()= 추가삭제 불가

# # t1 = (1,2,'a','b')
# # t2 = (3,4)
# # t2 *= 3
# # print(t2)

# # # 딕셔너리 자료형 = key : value
# # dic = {'name':'이문현', 'age' : 15}
# # print(dic['name'])
# # dic['추가하는법'] = '이렇게'
# # print(dic)
# # del dic['추가하는법']
# # print(dic)

# # print(dic.get('키가존재하는가? 있으면 값 출력', '없으면 출력할 문자열'))
# # print(dic.get('age'))   #age의 값 출력
# # print('name' in dic)    #true 출력

# # #키만  보기, 값만 보기
# # print(dic.keys())
# # print(dic.values())
# # #새로운 튜플 형태로 담기
# # print(dic.items())

# # for k, v in dic.items():
# #     print('키는 ' + str(k))
# #     print('값은 ' + str(v))

# # #비우기
# # dic.clear()
# # print(dic)



# # # #집합 -순서 X  중복 X
# # # from hashlib import new


# # # s1 = set([1,2,3])
# # # print(s1)
# # # print(type(s1))

# # # #중복삭제과정
# # # x = [1,2,2,3,3]
# # # newList = list(set(x)) #리스트->집합(중복제거)->리스트로 형변환
# # # print(newList)
# # # print(type(newList))  
# # # #또는
# # # a = set("Hello")
# # # print(a)    #순서가 없고 중복이 삭제된다

# # # #교집합 합집합 차집합
# # # s1 = set([1,2,3,4,5,6])
# # # s2 = set([4,5,6,7,8,9])
# # # print(s1 & s2)      #교집합 출력
# # # print(s1.intersection(s2)) #교집합 출력
# # # print(s1 | s2)      #합집합 출력
# # # print(s1.union(s2))
# # # print(s1 - s2)      #차집합 출력
# # # print(s1.difference(s2))
# # # print(s2.difference(s1))

# # # s1.add(10)
# # # print(s1)           #집합에 원소 추가
# # # s2.update([11,13,14,1]) #집합에 여러 원소 추가, 중복된것은 자동 처리
# # # print(s2) 


# # #  bool형식
# # from operator import truediv


# # a = True
# # b = False

# # print(a)
# # print(type(b))

# # a = [1,2,3,4]
# # while a:
# #     a.pop()
# #     print(a)    
    
# #변수할당
# a, b = ('python', 'life')
# print(a)
# print(b)


# (a, b) = ('n', 'le')
# print(a)
# print(b)

# [a, b] = ['python', 'life']
# print(a)
# print(b)

# a = b = "hello"
# print(a)
# print(b)

# #swap
# a = 3
# b = 5
# a,b = b,a
# print(a)
# print(b)


# #정규표현식

#     #문자 클래스 []
#     from re import T, X


#     [abc] => 한글자라도 포함하면 매치가능
#     또는 [a-c] = [abc], [0-5] ==[012345]

#     #dot .
#     a.b의 .은 모든 문자를 의미한다
#     => a0b, aab, acb 등 일치
#     abc는 일치하지 않는다

#     #반복 *
#     ca*t

#     ct는 a가 0번반복 ==> 매치
#     cat는 a가 0번 이상 반복 ==> 매치
#     caaaaaat도 매치

#     #반복 +
#     ca+t

#     ct  a가 0번반복 => 매치 X
#     cat는 a가 1번 이상 반복 ==> 매치
#     caaaaaat도 매치

#     #반복({m,n}, ?)
#     ca{2}t
#     cat는 a가 1번만 반복되어 매치되지 않음 
#     caat는 a가 2번 반복되어 매치    

#     ca{2,5}t
#     a가 2이상 5이하만 매치
#     caat 매치
#     caaaaat 매치

#     #반복 ({m,n}, ?)
#     ab?c
#     b가 0회 또는1회
#     ? == {0,1} 같은표현


#     #정규표현식모듈
#     정규표현식 지원 모듈 = re모듈
#     import re 
#     p = re.compile('ab**')


