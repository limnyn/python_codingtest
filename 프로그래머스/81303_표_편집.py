# https://school.programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):
    # 연결 리스트
    ll = {i : [i - 1, i + 1] for i in range(n)}
    
    # 시작의 이전 노드, 끝의 다음 노드를 None으로 초기화
    ll[0][0], ll[n-1][1] = None, None
    
    
    current = k
    
    undo_stack = []
    
    for command in cmd:
        
        operation = command[0]
        
        if operation == "U" or operation == "D":
            
            offset = int(command[2:])
            
            for _ in range(offset):
            
                if operation == "U":
                    current = ll[current][0]
                else:
                    current = ll[current][1]
            
        elif operation == "C":
            past, future = ll[current]
            undo_stack.append((current, past, future))
            
            if past != None:
                ll[past][1] = future
            if future != None:
                ll[future][0] = past
            
            current = future if future is not None else past
            
            
        elif operation == "Z":
            node, past, future = undo_stack.pop()
            
            if past != None:
                ll[past][1] = node
            if future != None:
                ll[future][0] = node
            
    result = ["O"] * n
    for node, _, _ in undo_stack:
        result[node] = "X"
        
        
    return "".join(result)
        
        
            
                
            
        
    
    
    
