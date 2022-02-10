#간단한 메모장 만들기
#기능 - 메모 추가하기, 메모 조회하기
#입력 - 메모내용, 실행옵션
#출력 - memo.txt
#예 - python memo.py -a "Life is too short"

import sys
#sys.argv[0] == memo.py
#sys.argv[1] == -a같은 옵션
option = sys.argv[1] 
#print(option)

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close
elif option == '-v':
    f = open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)
