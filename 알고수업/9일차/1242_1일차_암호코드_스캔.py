"""
1. 각 라인에 대해 암호 덩어리를 찾고 - 함수 하나
2. 암호가 검증했던 암호인지 확인,

암호 검증 모듈

암호코드
    하나의 최소 가로길이 = 56
    선이 굵어질 수록(배수) 56의 배수의 길이를 갖게 된다

    if 숫자코드 하나가 7칸 -> 56
    elif 14칸 -> 112
    else 7*i -> 56*i

    암호의 시작(뒤)에서 부터 2진화 진행, 
각 암호는 7자리, 16진수에 대해 7*x배수일 때 몇 칸씩 끊어야 하는가

16진수에 대해 2진화를 한 후, 뒤에서 가장 먼저 나오는 1부터 시작하여 56*n에 대해 배수를 찾는다.


    
    탐색 모듈 A. 뒤에서부터 16진수를 탐색해서 암호검증 모듈에 전달
        - 각 암호는 띄어져 있기 때문에 뒤에서부터 0일때 까지 탐색
    
    검증 모듈 B. 암호 검증(16진수 입력)

        1. 찾았던 암호인지 dict에서 확인
            찾았던 암호면 pass

        2. 16진수에 대해 뒤에서부터 0이아닐 때 까지 탐색
            만약 탐색한 16진수가 x자릿수 일 때
            16진수를 2진수로 만든다. 그리고 뒤에서부터 0이 아닐 때 까지 pop하고, 
            앞에 숫자가 현재보다 큰 가장 가까운 56의 배수가 되도록 추가해준다.
            56의 배수를 찾아서 해당 배수만큼 암호를 판별하고 
            암호 dict에 해당 찾은 암호를 검증값을 더한 것과 쌍으로 추가.

    C.배열 각 행에 대해 처리 후 dict에서 값을 출력해서 계산

풀이
    -7개를 읽어서 판별하겠다
    -끝이 전부 1로 되어있다. -> 어디서 끝나는 지 추정할 수 있다.
    -또한 암호는 0으로 감싸져 있다 -> 1 0 으로 암호가 끝난다고 볼 수 있다
    
    따라서 뒤에서 부터 볼때 최초의 1이 오른쪽 벽인것이 확실하다

    두깨에 대한 계산
        - 0010111같은게 있을 때, 0과 1의 묶음 네개를 찾아서 비율을 매칭해서 찾아 볼 수 있다.
        - 4묶음이 나오도록 count 한다
            - 4묶음에 대한 비율이 나온다면 (00 1111 00 111111) -> 14개
            - 이것으로 배율을 구할 수 있다 -> 묶음 길이 14 = 7 * 2 = > 2배
            - 따라서 2로 나누면 1:2:1:3, 

            -최적화를 위해 뒤에서 세 묶음만 사용해도 된다. (101 패턴 세묶음으로 배율을 구할 수 있다)
                - 해당 배율만큼 띄면서 8번 처리하면 금방 구할 수 있다.

    
        for r in range(n):
            while c > 0
            x, y, z = 0
            # start = 0
            code_cnt = 0
            codes = []
            while grid[r][c] == 1: 
                start = c
                z += 1 
                c -= 1
            while grid[r][c] == 0: 
                y += 1 
                c -= 1
            while grid[r][c] == 1: 
                x += 1 
                c -= 1
            
            x:y:z로 비율을 찾아서 
            g = math.gcd(x,y,z)
            x /= g
            y /= g
            z /= g
            # start * g*7만큼 넘어가면서 c -= g만큼 넘어가면서 z, y, x 에 넣고 7번 더 반복 -> 암호하나 get
            codes.append(코드숫자)
            code_cnt += 1

            if code_cnt == 8:
                코드 판별, 검증 -> true
                result += 정상 코드 숫자
            다시 x, y, z 반복 
            # 끝나면 


    중복계산 방지
        - 우상단 확인으로 인해 같은데이터인지 확인해 볼 수 있다.
        if map[i][j] = 1 && map[i-1][j] == 0일때 탐색하기 
            x = y = z = 0;
            while (map[i][j] == 1) {z++; j--;}
            while (map[i][j] == 0) {y++; j--;}
            while (map[i][j] == 1) {x++; j--;}
            int min = min(x,y,z)
            x /= min
            y /= min
            z /= min
            xyz비율로 코드 확인 

            code[codei--] = scode[x-1][y-1][z-1];
        



"""

# import math

# # print(len("0111011 0110001 0111011 0110001 0110001 0001101 0010011 0111011"))
# print(len("01110110110001011101101100010110001000110100100110111011"))
# 56
# print(56/4)
# print(len("1DB176C588D26EC"))
# print(len("1DB176C588D26EC")*4)

# h = int('1DB176C588D26EC', 16)
# num = 10010011
# # num = 0x00000000000F3F033CC0F03CC0F30F0C30F3CFC00000000000000000D32C49B7268D18000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000019E7819FE67E7981E79F861E187800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# print(bin(num))
# # print(len(bin(0x1DB176C588D26EC)))
# # print(len('111011011000101110110110001011000100011010010011011101100'))


# # B 검증 모듈
# # def decode(code):




'''
수정본
    1. line 2진화
    2. 뒤에서부터 첫 1을 start로 지정
        end = start-7*i 진행하며 
        if end == 0 and end~start가 패턴에 존재하면 탐색

패턴이 존재하면 검증

start = end -1 로 하고 다음 루프 진행
'''
def hex_to_binary(hex_string):
    binary_string = ""
    for char in hex_string:
        # 각 16진수 문자에 대응하는 4비트의 이진수 문자열 생성
        binary_char = bin(int(char, 16))[2:].zfill(4)
        # 0이 아닌 경우에만 해당 이진수 문자열 추가
        binary_string += binary_char if char != '0' else '0000'
    return binary_string

import math
n, m = map(int, input().split())
grid = []
for _ in range(n):
    line = input()
    grid.append(list(map(int, list(hex_to_binary(line)))))
    # print(bin(int(line,16)))
    # exit()
    # grid.append(list(bin(int(line,16))))
    # grid.append(list(map(int,list(str(bin(int(line,16))))[2:])))

# grid = [list(map(int, list(input)) for _ in range(n)]
# for g in grid:
#     print(g)

code_verification = dict()
code_verification["211"]=0
code_verification["221"]=1
code_verification["122"]=2
code_verification["411"]=3
code_verification["132"]=4
code_verification["231"]=5
code_verification["114"]=6
code_verification["312"]=7
code_verification["213"]=8
code_verification["112"]=9

# print(code_verification[str(2)+str(3)+str(1)])
    
'''
if map[i][j] = 1 && map[i-1][j] == 0일때 탐색하기 
    x = y = z = 0;
    while (map[i][j] == 1) {z++; j--;}
    while (map[i][j] == 0) {y++; j--;}
    while (map[i][j] == 1) {x++; j--;}
    int min = min(x,y,z)
    x /= min
    y /= min
    z /= min
    xyz비율로 코드 확인 

    code[codei--] = scode[x-1][y-1][z-1];

'''

result = 0

for r in range(1, n):
    c = len(grid[r])-1
    codes = []
    while c > 0:
        x, y, z = 0, 0, 0
        # start = 0
        code_cnt = 0
        if grid[r][c] == 1 and grid[r-1][c] == 0: 
            while grid[r][c] == 1:
                start = c
                z += 1 
                c -= 1
            while grid[r][c] == 0: 
                y += 1 
                c -= 1
            while grid[r][c] == 1: 
                x += 1 
                c -= 1
            
            # x:y:z로 비율을 찾아서 
            g = math.gcd(x,y,z)
            x //= g
            y //= g
            z //= g

            # start * g*7만큼 넘어가면서 c -= g만큼 넘어가면서 z, y, x 에 넣고 7번 더 반복 -> 암호하나 get
            
            codes.append(code_verification[str(x)+str(y)+str(z)])
            code_cnt += 1
            
            if code_cnt == 8:
                print(codes)
                codes.reverse()
                odd, even = 0, 0
                
                for i, v in enumerate(codes):
                    if i & 2 == 0:
                        odd += v
                    else:
                        even += v
                if (odd * 3 + even) % 10 == 0:
                    result += (odd * 3 + even)
                    codes = []
        else:
            c -= 1

print(result)
