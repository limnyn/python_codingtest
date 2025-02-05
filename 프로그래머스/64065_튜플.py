# https://school.programmers.co.kr/learn/courses/30/lessons/64065
import json

def solution(s):
    input_string = s.replace('{', '[').replace('}', ']')

    result_list = json.loads(input_string)
    
    # result_list를 길이를 기준으로 정렬합니다.
    result_list.sort(key=len)

    answer = []
    for lst in result_list:
        for num in lst:
            if num not in answer:
                answer.append(num)
    return answer