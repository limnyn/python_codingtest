# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXGKdbqczEDFAUo
# https://diane21.tistory.com/44
# 페르마의 소정리
# mod pow, mod 곱, mod factorial에 대해서 복습하기

def facto_mod(n, p):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % p
    return result

p = 1234567891
for t_c in range(1,int(input())+1):
    n, r = map(int, input().split())
    
    top = facto_mod(n, p) # A
    rfact = facto_mod(r, p) 
    n_min_rfact = facto_mod(n-r,p)
    rnrfact = rfact * n_min_rfact % p
    bottom = pow(rnrfact, p-2, p)
    result = top * bottom % p

    
    # print(result)
    print(f'#{t_c} {result%1234567891}')

