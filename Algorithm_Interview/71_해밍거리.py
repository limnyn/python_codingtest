# 두 정수를 입력받아 몇 비트가 다른지 계산하라.
x = 1
y = 4

# 1 (0 0 0 1)
# 4 (0 1 0 0)
# 해밍거리 2

def hammingDistance(x, y) -> int:
    return bin(x ^ y)
print(hammingDistance(x,y).count('1'))

