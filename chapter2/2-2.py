a = "I eat %d apples." % 3
print(a)

b = "I eat %s apples." % "five"
print(b)

number = 10
day = "three"
c = "I ate %d apples. so I was sick for %s days." % (number, day)
print(c)

d = "%10s" % "hi"
print(d)

e = "%-10sjane." % 'hi'
print(e)

f = "%0.4f" % 3.42134234
print(f)

e = "I ate {0} apples. so I was sick for {1} days.".format(10, 'three')
print(e)

f = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(f)

# 왼쪽 정렬
g = "{0:>10}".format("hi")
print(g)

# 가운데 정렬
h = "{0:^10}".format("hi")
print(h)

# 공백 채우기
i = "{0:!<10}".format("hi")
print(i)

name = '홍길동'
age = 30
j = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(j)



k = "hobby"
print(k.count('b'))

#왼쪽공백 제거
l = " hi "
l.lstrip()
print(l)
