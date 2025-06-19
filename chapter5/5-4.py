# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)


# try:
#     age=int(input('나이를 입력하세요: '))
# except:
#     print('입력이 정확하지 않습니다.')
# else:
#     if age <= 18:
#         print('미성년자는 출입금지입니다.')
#     else:
#         print('환영합니다.')


class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)