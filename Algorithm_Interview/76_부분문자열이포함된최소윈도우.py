# 문자열 S와 T를 입력받아 O(n)에 T의 
# 모든 문자가 포함된 S의 최소 윈도우를 찾아라.

# 입력
S = "ADOBECODEBANC"
# S = "ABBSESC"
T = "ABC"

# 브루트 포스
def minWindow(S, T):
    def contains(s_substr_lst, t_lst):
        for t_elem in t_lst:
            if t_elem in s_substr_lst:
                s_substr_lst.remove(t_elem)
            else:
                return False
        return True
    if not S or not T:
        return ''
    
    window_size = len(T)

    for size in range(window_size, len(S) + 1):
        for left in range(len(S) - size + 1):
            s_substr = S[left:left+size]
            if contains(list(s_substr), list(T)):
                return s_substr
    return ''
print(minWindow(S,T))

# 투 포인터, 슬라이딩 윈도우로 최적화
def minWindow(s, t):
    import collections
    need = collections.Counter(T)
    missing = len(t)
    left = start = end = 0

    # 오른쪽으로 포인터 이동
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1

        # 필요 문자가 0이면 왼쪽 포인터 이동 판단
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            
            if not end or right - left <= end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
    return s[start:end]

        
print(minWindow(S, T))
