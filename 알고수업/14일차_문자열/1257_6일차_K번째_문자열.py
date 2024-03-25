

def get_substrings(s):
    substrings = set()
    n = len(s)
    for length in range(1, n+1):
        for start in range(n-length+1):
            substrings.add(s[start:start+length])
    return substrings
    
for t_c in range(1, int(input())+1):
    k = int(input())
    string = input()
    result = "none"
    all_substrings = sorted(get_substrings(string))
    if len(all_substrings) >= k:
        result = all_substrings[k-1]
    print(f"#{t_c} {result}")
    
    
