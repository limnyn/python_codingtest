# https://school.programmers.co.kr/learn/courses/30/lessons/60057
s ="abcabcabcabcdededededede"
# s = "a"


def solution(s):
    length = len(s)
    answers = []
    if length == 1:
        return 1
    
    for step in range(1,length):
        mols = []
        for i in range(0, length, step):
            mols.append(s[i:step+i])

        result = []
        count = 1
        for k in range(len(mols)):
            
            if k != len(mols)-1 and mols[k] == mols[k+1]:
                    count += 1
            else:
                if count == 1:
                    result.append(mols[k])
                else:
                    result.append(str(count)+mols[k])
                count = 1

        # print("step : ", step, (''.join(result)), mols)
        answers.append(len(''.join(result)))

    return min(answers)

print(solution(s))

# line = input()
# length = len(line)
# mols = []
# step = 2
# for i in range(0, length, step):
#     print(i, step+i, line[i:(step+i)])
#     mols.append(line[i:(step+i)])
# print(mols)

# ab cd ab cd ab c

# 오답노트
# step의 길이가 len(s)의 절반만 해도 모든 케이스를 통과할 수 있다고 생각해서 step의 for문을
# len(s)//2로 풀이했는데 len(s)//2+1로 고쳐서 해결했다.