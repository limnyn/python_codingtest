# https://school.programmers.co.kr/learn/courses/30/lessons/60061



# 조건
#     1. 기둥 : 바닥, 기둥 위 또는 보의 한쪽 끝 부분
#     2. 보   : 한쪽 끝 부분이 기둥 위 또는 양쪽 끝 부분이 다른 보와 동시에 연결


# [x,y,a,b]
#     x, y    = 교차점의 좌표, 보는 좌표기준 오른쪽, 기둥은 좌표 기준 위쪽
#     a       = 0은 기둥 1은 보
#     b       = 0은 삭제 1은 설치


# 출력
#     [x,y,a]
#     x좌표 기준으로 오름차순, 그 다음은 y좌표




n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

# 조건
#     1. 기둥 : 바닥, 기둥 위 또는 보의 한쪽 끝 부분
#     2. 보   : 한쪽 끝 부분이 기둥 위 또는 양쪽 끝 부분이 다른 보와 동시에 연결
def build_permission(results):
    for x, y, col in results:
        if col == 0:
            # x,y 좌표에서 만약 col이면 x,y-1이 기둥이나 땅인지, 
            if y == 0:
                continue
            elif [x, y-1, 0] in results:
                continue

            elif [x, y, 1] in results:
                continue
            # 아니면 y의 x-1의 col이 1일때 (보 일때)
                        # 이거는 제외[또는 x col이 1이면서 x-1의 col이 1이아닐때]
            elif [x-1, y, 1] in results:
                continue

            # else: false 반환
            else: 
                return False
        
        if col == 1:
            
            # 현재위치 or x+1의 아래가 기둥일때 true
            if [x, y-1, 0] in results or [x+1, y-1, 0] in results:
                continue
            # 또는 x-1의 col이 1이고 x+1의 col이 1일때 true
            elif [x-1, y, 1] in results and [x+1, y, 1] in results:
                continue

            # else: false 반환
            else:
                return False
    return True
             
    
    



def solution(n, build_frame):
    n+=1
    
    results = []
    # print(board)
    for build in build_frame:
        x, y, col, act = build[0], build[1], build[2], build[3]
        
        
        if act == 1: # 설치시
            results.append([x,y,col])
            if build_permission(results) == False:
                results.remove([x,y,col])
                
        elif act == 0: # 삭제시
            results.remove([x,y,col])
            if build_permission(results) == False:
                results.append([x,y,col])

    results.sort()
    
                   
    return results       
        
        
# print(build_frame[0])
  
print(solution(n, build_frame))