
# #정규표현식

#     #문자 클래스 []
#     from re import T, X


#     [abc] => 한글자라도 포함하면 매치가능
#     또는 [a-c] = [abc], [0-5] ==[012345]

#     #dot .
#     a.b의 .은 [\n\제외 모든 문자를 의미한다
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








# import re
# #p==패턴
# p = re.compile('[a-z]+')#a부터z까지 문자열이 한번이상 반복
# # m = p.match('python')# m ==match 객체
# # print(m)

# # m = p.search('3 python') #처음이 꼭 일치하지 않아도 일치구문 있으면 반환
# # print(m)

# # m = p.findall('life is too short')  #p와 일치하는 string을 list로 반환
# # print(m)


# # m = p.finditer("life is too short")#매치되는 문자열을 매치객체로 리턴
# # for r in m:
# #     print(r)

# #match 객체
# #group(), start(), end(), span()메서드 포함

#     #.group() == 매치된 문자열을 리턴한다
#     #.stat() == 매치된 문자열의 시작 위치를 리턴한다
#     #.end() == 매치된 문자열의 끝 위치를 리턴한다
#     #.span() == 매치된 문자열의 (시작, 끝)에  해당되는 튜플을 리턴한다.

# m = p.match('python')
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())



##########

#컴파일 옵션, DOTALL, S, IGNORECASE, MULTILINE, M, VERBOSE, X

# #DOTALL, S
# import re
#     # p = re.compile('a.b')
#     # m = p.match('a\nb') # == None 출력, dot은 \n제외
#     # print(m)
# p = re.compile('a.b', re.DOTALL)    #\n도 인식한다
# #또는 
# #p = re.compile('a.b', re.S)도 같은기능
# m = p.match('a\nb')
# print(m)




# #IGNORECASE
# import re
# p = re.compile('[a-z]', re.IGNORECASE)#대문자소문자 무시
# print(p.match('python'))
# print(p.match('Python'))
# print(p.match('PYTHON'))

# # MULTILINE, M
# import re
# p = re.compile("^python\s\w+", re.M)
# #^ = 맨처음으로 나오는, \s=공백, w+=단어가 여러번 반복
# #제일 처음나오는 python공백+단어를 찾는다
# #re.M 추가시 각 줄의 처음으로 인식하기 때문에
# # python one~three까지 출력한다
# #MULTILINE == ^등 조건을 각 라인마다 적용시킨다.
# data = """python one
# life is too short
# python two
# you need python
# python three"""

# print(p.findall(data))



# #VERBOSE, X     ==정규표현식은 줄바꿈으로 표현이 안되지만 공백을 제거해서 설명을쓰더라도 컴파일 가능 , 하나씩 설명가능
# import re
# charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# charref = re.compile(r"""
# &[#]                # Start of a numeric entity reference
# (
#       0[0-7]+       #Octal form
#     | [0=9]+        #Decimal form
#     | x[0-9a-fA-F]+ #Hexadecimal form
# )
# ;                   #Trailing semicolon
# """, re.VERBOSE)    




# #백슬래시 문제
# #\section을 표현하고 싶을때, \s (공백) 와 충돌한다
# p = re.compile('\\section') #\\가 문자열일때는 \로 치환된다, 따라서 
# p = re.compile('\\\\section') #으로 쓰거나
# p = re.compile(r'\\section')#r을 사용해서 \문제를 해결한다, 로우스트링




# #메타문자
# # |
# import re
# p = re.compile('Crow|Servo') # A|B == A or B
# m = p.match('CrowHello')    # Crow나 Servo와 매치하는지 검사한다
# print(m)


# #^      #맨 처음을 나타낸다
# print(re.search('^Life', 'Life is too short'))  #첫단어가 Life이기 때문에 매치
# print(re.search('^Life', 'My Life'))            #첫번째에 Life가 존재하지 않기때문에 none

# #$      #맨 끝을 나타낸다
# print(re.search('Life$', 'Life is too short'))  #Life로 문자열이 끝나지 않기 때문에 none
# print(re.search('Life$', 'My Life'))            #끝에 Life가 존재하기 때문에 match

# #\b = 공백을 나타낸다
# p = re.compile(r'\bclass\b')    #공백class공백을 찾는다
# print(p.search('no class at all'))
# print(p.search('the declassified algorithm'))#declassfied != \bclass\b
# print(p.search('one subcalss is'))          #subclass != \bclass\b




# #그루핑()
# import re
# p = re.compile('(ABC)+')  #ABC로 반복되는걸 찾고싶을때
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group())
# #그루핑2()
# p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
# m = p.search("park 010-1234-1234")
# print(m.group(1)) #그루핑 된 것중 첫번째 그룹(\w+) == park을 출력한다 

# #그루핑된 문자열에 이름붙이기 ?P<name>
# import re
# p =re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")   #그룹에 이름을 붙여 불러올 수 있다.
# m = p.search("park 010-1234-1234")
# print(m.group("name"))



# #전방탐색: 긍정형 (?=)
# import re
# p = re.compile(".+(?=:)") #문자열이 반복되다가 :만나면 멈추고 그 전까지 반환 ==> http, 검색조건에는 :포함, 결과에는 포함 X
# m = p.search("http://google.com")
# print(m.group())

# #전방탐색: 부정형 (?!)
# import re
# p = re.compile(".*[.](?!bat$).*$", re.M)    #.*[.]일때 bat가 끝인것은 포함되지 않게 출력
# l = p.findall("""
# autoexec.exe
# autoexec.bat
# autoexec.jpg
# """)
# print(l)


# #문자열 바꾸기 sub
# import re
# p = re.compile('(blue|white|red)')
# print(p.sub('colour', 'blue socks and red shoes')) #.sub(A, B)를 사용해서 정규표현식에 일치하는단어를 B에서 찾아 A의 문자열로 바꿀수 있다


#Greedy / Non-Greedy
import re 
s = '<html><head><title>Title</title>'
print(re.match('<.*?', s).group())#Greedy ->제일 바깥 꺾쇠들로 인식     =>'<html><head><title>Title</title>'
#print(re.match('<.*?>', s).group()) #Non-Greedy ->제일 처음 나오는 꺽쇠로 구분  =>'<html>