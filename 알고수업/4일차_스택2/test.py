def infix_to_postfix(infix_expr):
  """
  중위 표기식을 후위 표기식으로 변환합니다.

  Args:
    infix_expr: 문자열로 이루어진 중위 표기식

  Returns:
    후위 표기식 문자열
  """
  prec = {
    '+': 1,
    '*': 2,
    '(': 3,
  }
  stack = []
  postfix_expr = []
  for token in infix_expr:
    if token.isdigit():
      postfix_expr.append(token)
    elif token in prec:
      while stack and prec[stack[-1]] >= prec[token]:
        postfix_expr.append(stack.pop())
      stack.append(token)
    elif token == ')':
      while stack and stack[-1] != '(':
        postfix_expr.append(stack.pop())
      if not stack:
        raise ValueError("괄호가 맞지 않습니다.")
      stack.pop()  # '(' 제거
  while stack:
    postfix_expr.append(stack.pop())
  return ''.join(postfix_expr)


def eval_postfix(postfix_expr):
  """
  후위 표기식을 계산합니다.

  Args:
    postfix_expr: 문자열로 이루어진 후위 표기식

  Returns:
    계산 결과
  """
  stack = []
  for token in postfix_expr:
    if token.isdigit():
      stack.append(int(token))
    else:
      operand2 = stack.pop()
      operand1 = stack.pop()
      result = 0
      if token == '+':
        result = operand1 + operand2
      elif token == '*':
        result = operand1 * operand2
      stack.append(result)
  return stack.pop()

def main():
  """
  입력받은 문자열 계산식을 후위 표기식으로 변환하고 계산합니다.
  """
infix_expr = """
9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3
"""

postfix_expr = infix_to_postfix(infix_expr)
result = eval_postfix(postfix_expr)

print(result)

if __name__ == '__main__':
  main()
