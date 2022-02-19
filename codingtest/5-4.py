# 재귀 함수의 종료 조건
# 예제 4번 재귀함수 종료 예제
#  재귀함수를 100번 호출하도록 작성


def recursion_endwhen100(i):
    if(i == 100):
        return 
    else:
        print(str(i+1)+' 번째 재귀함수')
        recursion_endwhen100(i + 1)

recursion_endwhen100(0)

# 재귀 함수는 내부적으로 스택 자료구조와 동일하다.
