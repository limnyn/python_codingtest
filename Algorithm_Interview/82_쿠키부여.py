# 아이들에게 1개씩 쿠키를 나눠줘야 한다.
# 각 아이 child__i마다 그리드 팩터gi를 갖고 있으며, 이는 아이가 만족하는 최소 쿠키의 크기를 말한다.
# 각 쿠기 cookie_k는 크기 sj를 가지고 있으며 sj>=ji이어야 아이가 만족하며 쿠키를 받는다.
# 최대 몇 명의 아이들에게 쿠키를 줄 수 있는지 출력하라.

children = [1,2,3]
cookies = [1,1]

def findContentChildren(children, cookies):
    children.sort()
    cookies.sort()
    child_i = cookie_j = 0
    # 만족하지 못할 때 까지 그리디 진행
    while child_i < len(children) and cookie_j < len(cookies):
        if cookies[cookie_j] >= children[child_i]:
                child_i+= 1
        cookie_j += 1




    return child_i
            


        


print(findContentChildren(children,cookies))
