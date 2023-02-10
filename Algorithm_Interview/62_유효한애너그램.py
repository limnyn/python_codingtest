# t가 s의 애너그램인지 판별하라
s = "anagram"
t = "nagaram"

#정렬을 이용한 비교
def isAnagram(s, t):
    return sorted(s) == sorted(t)

print(isAnagram(s, t))
