# 부호없는 정수형을 입력받아 1비트의 개수를 출력하라.

# 1의 개수 구하기
nums = 0b00000000000000000000000000001011
print(bin(nums).count('1'))

# 비트 연산으로 계산하기
# 이진수의 특징
#     이진수 A와 A-1을 and 연산하면 A의 비트에서 1이 하나 사라진다
#     ex) 1000 & 0111 =>0000
#         1010 & 1001 =>1000
#     따라서 0이 될 때까지 이 연산을 반복하면 1의개수를 구할 수 있다.

def hammingWeight(n:int):
    count = 0
    while n:
        # 1을 뺀값과 AND 연산 횟수 측정
        n &= n-1
        count += 1
    return count
print(hammingWeight(nums))