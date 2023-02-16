# 숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라.

input = "2*3-4*5"

def diffWaysToCompute(input):
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))
        return results
    
    if input.isdigit():
        return [int(input)]
    
    results = []
    for index, value in enumerate(input):
        if value in "-+*":
            left = diffWaysToCompute(input[:index])
            right = diffWaysToCompute(input[index+1:])

            results.extend(compute(left,right,value))
    return results

print(diffWaysToCompute(input))
            
