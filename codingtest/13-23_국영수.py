# https://www.acmicpc.net/problem/10825


n = int(input())

scores = []
for _ in range(n):
    line = input().split()
    score = []
    score.append(line[0])
    score.extend(list(map(int, line[1:])))
    score = tuple(score)
    scores.append(score)
#     print(score)
# print(scores)
# scores = sorted(scores, key= lambda x : x[0], reverse=False)
# scores = sorted(scores, key= lambda x : x[3], reverse=True)
# scores = sorted(scores, key= lambda x : x[2], reverse=False)
# scores = sorted(scores, key= lambda x : x[1], reverse=True)
scores = sorted(scores, key= lambda x : (-x[1],x[2],-x[3],x[0]))


for score in scores:
    print(score[0])
    