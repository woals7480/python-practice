# def add(a, b):
#     return a+b

# a = 3
# b = 4
# c = add(a, b)
# print(c)

# def add_many(*args): 
#     result = 0 
#     for i in args: 
#         result = result + i
#     return result

# result = add_many(1,2,3)
# print(result)

# result = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)


# def add_mul(choice, *args): 
#     if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
#         result = 0 
#         for i in args: 
#             result = result + i 
#     elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
#         result = 1 
#         for i in args: 
#             result = result * i 
#     return result

# result = add_mul('add', 1,2,3,4,5)
# print(result)

# result = add_mul('mul', 1,2,3,4,5)
# print(result)


# def print_kwargs(**kwargs):
#     print(kwargs)
#     print(kwargs['name'])

# print_kwargs(name='foo', age=3)



# def say_myself(name, age, man=True): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % age) 
#     if man: 
#         print("남자입니다.")
#     else: 
#         print("여자입니다.")

# say_myself("박응용", 27)


# a = 1 
# def vartest(): 
#     global a 
#     a = a+1

# vartest() 
# print(a)


add = lambda a, b: a+b
result = add(3, 4)
print(result)