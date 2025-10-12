# https://www.acmicpc.net/problem/15702

import sys
def input(): return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    n, m = map(int, input().split())
    
    rewards = list(map(int, input().split())) # 점수 표
    scores = {} # 학생 점수를 저장할 딕셔너리
    
    for _ in range(m):
        
        arr = list(input().split())
        student, result = int(arr[0]), arr[1:]
        
        # 학생이 처음 등장하는 경우에만 0점으로 초기화
        if student not in scores:
            scores[student] = 0
        
        for i, r in enumerate(result):     # 학생 점수 계산
            if r == "O":
                scores[student] += rewards[i]
    
    # 최고 점수 학생 찾기
    # best_student = sorted(scores.items(), key=lambda x: (-x[1], x[0]))[0]
    # 위 기존 코드는 전체 정렬을 수행 후 0번 값 사용 -> 1~n-1까지 값들도 불필요하게 정렬 처리함
    # -> n log n
    
    # top-N이 전체 정렬보다 효율적이기에 max를 통해 n으로 처리
    # 점수(x[1])는 높을수록, 학생 번호(x[0])는 작을수록 우선순위가 높다.
    best_student = max(scores.items(), key=lambda x: (x[1], -x[0]))
    
    print(best_student[0], best_student[1])