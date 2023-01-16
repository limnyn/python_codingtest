

t =int(input())


# for i in range(10, n+1):
    
#     j = i
#     cnt = 0
#     while(j >= 10):
#         j %= 10
#         cnt+=1
#         print(j, cnt)
    
if (t < 100):
    print(t)
else:
    cnt = 99
    for i in range(100, t+1):
        j = i
        seq = []
        while(j > 9):
            seq.append(j%10)
            j = j//10
        seq.append(j)
        if(len(seq)<=3 and(seq[2]-seq[1])==(seq[1]-seq[0])):
            cnt+=1

    print(cnt)
# j = t
# seq = []
# while(j > 10):
#         seq.append(j%10)
#         j = j // 10
# seq.append(j)
# if(seq[0] - seq[1] == seq[1] - seq[2]):
#     print("true")
# # print(seq)