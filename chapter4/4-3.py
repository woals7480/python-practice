# 파일 생성
# f = open("C:/Users/woals/Desktop/python/chapter4/새파일.txt", 'w', encoding='utf-8')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# 파일 읽기
# f = open("C:/Users/woals/Desktop/python/chapter4/새파일.txt", 'r', encoding='utf-8')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open("C:/Users/woals/Desktop/python/chapter4/새파일.txt", 'r', encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#     line = line.strip() # 줄 끝의 줄 바꿈 문자 제거
#     print(line)
# f.close()

# f = open("C:/Users/woals/Desktop/python/chapter4/새파일.txt", 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# f = open("C:/Users/woals/Desktop/python/chapter4/새파일.txt", 'r', encoding='utf-8')
# for line in f:
#     print(line)
# f.close()

# 파일 내용 추가
# f = open("C:/Users/woals/Desktop/python/chapter4/새파일.txt", 'a', encoding='utf-8')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# with 문을 사용하면 with 블록(with 문에 속해 있는 문장)을 벗어나는 순간, 열린 파일 객체 f가 자동으로 닫힌다.
with open("C:/Users/woals/Desktop/python/chapter4/foo.txt", 'w', encoding='utf-8') as f:
    f.write("Life is too short, you need python")