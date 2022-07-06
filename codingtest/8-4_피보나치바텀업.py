d = [0] * 1000
d[0] = 1
d[1] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])