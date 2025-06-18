#딕셔너리

a = {1: 'a', 3: 'c'}
a[2] = 'b'
print(a)

del a[1]
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a.get('d'))
print('c' in a)
a.clear()
print(a)