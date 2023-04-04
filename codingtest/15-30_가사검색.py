# # https://programmers.co.kr/learn/courses/30/lessons/60060
# trie써서 다시 풀기

# def solution(words, queries):
#     answer = []
#     q_dict = {}  
#     for q in queries:
#         if q[0] == '?':
#             for i in range(len(q)):
#                 if q[i] == '?':
#                     q_dict[q] = [1,i+1, len(q), 0]
#                 else:
#                     break
#         elif q[-1] == '?':
#             for i in range(len(q)-1,-1, -1):
#                 if q[i] == '?':
#                     q_dict[q] = [0,i,len(q), 0]
#                 else:
#                     break
#     for q in queries:
#         start_front, end, lenq = q_dict[q][0], q_dict[q][1], q_dict[q][2]
        
#         for w in words:
#             if len(w) != lenq:
#                 continue
            
#             if start_front:
#                 w_split = w[end:]
#                 q_split = q[end:]
#             else:
#                 w_split = w[:end]
#                 q_split = q[:end]
#             if w_split == q_split:                
#                 q_dict[q][3] += 1

#         answer.append(q_dict[q][3])
    
#     return answer

# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# # result = [3, 2, 4, 1, 0]

# # 
# print(solution(words,queries))
