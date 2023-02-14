# 대문자로 구성된 문자열 s가 주어졌을 때 k번만큼의 변경으로 만들 수 있는,
# 연속으로 반복된 문자열의 가자 긴 길이를 출력하라.
s = "AAABC"
k = 2

def characterReplacement(s, k) -> int:
    import collections
    counts = collections.Counter()
    left = right = 0
    for right in range(1, len(s)+1):
        
        counts[s[right - 1]] += 1
        # 가장 흔하게 등장하는 문자 탐새
        max_char_n = counts.most_common(1)[0][1]

        # k 초과시 왼쪽 포인터 이동
        
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    
    return right - left 
    

print(characterReplacement(s,k))