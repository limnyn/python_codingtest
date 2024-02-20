


# [3,6,5,7,2,1,4,9,8]

"""
stack = [] # stack에 역순으로 정답이 들어간다

del_list = []
for v in graph:
    if v == []:
        del_list.append(v)

while del_list:
    for node in del_list:
        graph[node] = []
        stack.append(node)


    for v in graph:
        for node in del_list:
            if node in v:
                v.remove(node)
        if v == []:
            del_list.append(v)

"""

for t_c in range(1, 11):
    vertex, e = map(int, input().split())

    graph = [[] for _ in range(vertex+1)]
    
    line = list(map(int,input().split()))
    for i in range(e):
        src, dst = line[2*i], line[2*i+1]
        
        graph[src].append(dst)
    
    
    stack = [] # stack에 역순으로 정답이 들어간다

    del_list = []
    for i,v in enumerate(graph):
        if v == []:
            del_list.append(i)

    while len(stack) <= vertex:
        for node in del_list:
            # graph[node] = []
            if node not in stack:
                stack.append(node)

        next_del  = []

        for i, v in enumerate(graph):
            if i in del_list:
                continue
            for n in graph[i]: 
                if n in del_list:
                    graph[i].remove(n)
            if v == [] and v not in stack:
                next_del.append(i)
        del_list = next_del[:]
    
    result = stack[1:]
    print(f'#{t_c}',end=' ')
    while result:
        c = result.pop()
        print(c, end=' ')
    print()

    