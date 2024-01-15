# https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number, k):
    stack = list(number[0])
    for num in number[1:]:
        while len(stack) > 0 and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    

    
    # number = 97865,  k=2인 경우 for문 순회시 
    # 9865, k=1인 상태로 남는데,
    # k가 남았을 때는 뒤에서부터 남은 수만큼 빼주면 된다.
    # 그러면 정상적으로 정답인 986이 출력된다
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)