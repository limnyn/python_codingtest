# https://school.programmers.co.kr/learn/courses/30/lessons/60058


# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.



# if p.count("(") == p.count(")"):
#     print("균형잡힌 괄호 문자열입니다.")
# else:
#     print("균형잡힌 괄호 문자열이 아닙니다.")
# "()  ))(( () "	 () 

                   
def solution(p):
    answer = ""
    # 1.입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == "":
        return answer
    # 2. 문자열 w를 두 균형잡힌 괄호 문자열 u,v로 분리합니다. u는 "균형잡힌 괄호 문자열로 더이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다."
    op, cp = 0, 0
    end_index = 0
    for i in range(len(p)):
        if p[i] == "(":
            op += 1
        elif p[i] == ")":
            cp += 1
        if cp == op:
            end_index = i+1
            break
    
    u = p[:end_index]
    v = p[end_index:]
    # 3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    op_u, cp_u = 0, 0
    isright = True
    for i in range(len(u)):
        if u[i] == "(":
            op_u += 1
            
        else:
            cp_u += 1
            if op_u < cp_u:
                isright = False
                break


    if isright == True:
        # 3-1. 수행한 결과 문자열을 u에 이어붙인 후 반환한다.
            answer = u + solution(v)
        # return u
        

            
    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('을 붙입니다.
        answer = '('    
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자를 이어 붙입니다.
        answer += solution(v)
        # 4-3. ')' 를 다시 붙입니다.
        answer += ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
        # 4-5. 생성된 문자열을 반환합니다.

    

    return answer

p = "()))((()"
# result = "()(())()"

print(solution(p))                
