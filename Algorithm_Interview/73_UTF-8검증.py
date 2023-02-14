# 입력값이 UTF-8 문자열이 맞는지 검증하라.

# 첫 바이트를 기준으로 한 판별
# 1바이트
#     0xxxxxxx
# 2바이트
#     110xxxxx 10xxxxxx
# 3바이트
#     1110xxxx 10xxxxxx 10xxxxxx
# 4바이트
#     11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

# 정상
data = [197,130, 1] 

# 비정상
# data = [235, 149, 4]

def validUtf8(data:list)->bool:
    # 문자 바이트 만큼 10으로 시작 판별
    def check(size):
        for i in range(start + 1, start + size + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
            return True
    start = 0
    while start < len(data):
        # 첫 바이트 기준 총 문자 바이트 판별
        first = data[start]
        if (first >> 3) == 0b11110 and check(3):
            start +=4
        elif (first >> 4) == 0b1110 and check(2):
            start += 3
        elif (first >> 5) == 0b110 and check(1):
            start += 2
        elif (first >> 7) == 0:
            start +=1
        else:
            return False
    return True

print(validUtf8(data))



