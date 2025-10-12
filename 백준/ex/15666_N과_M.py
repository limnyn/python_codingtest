# https://www.acmicpc.net/problem/15666

"""
여러개 선택 가능, 중복 입력은 다 제외해도 된다.

1. 입력에서 중복 제거(set)
2. dfs를 통해 선택 후 level 이동
3. 출력
"""

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    count =[0] * 10001 
    arr = sorted(set(list(map(int, input().split()))))
    
    
    path = []
    out = []
    def dfs(start, depth):
        if depth == m:
            out.append(' '.join(map(str, path)))
            return
        
        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i, depth + 1)
            path.pop()
            
    dfs(0, 0)
    print('\n'.join(out))
    
    