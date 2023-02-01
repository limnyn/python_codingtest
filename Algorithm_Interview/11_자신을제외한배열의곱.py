# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
# 나눗셈 연산 금지


array = [1,2,3,4]

result = 1
output = []
# 아래 과정을 통해 자신(i)을 제외한 왼쪽 값들의 곱을 output에 넣는다 
p = 1
for i in range(len(array)):
    output.append(p)
    p *= array[i]
# 자신(i)을 제외한 오른쪽 값들의 곱을 p로 구한뒤 자신을 제외한 왼쪽 값들에 넣는다.
p = 1
for i in range(len(array)-1, -1, -1):
    output[i]*=p
    p*=array[i]

print(output)


    