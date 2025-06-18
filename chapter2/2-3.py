odd = [1, 3, 5, 7, 9]
print(type(odd))

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][1])

b = [1, 2, 3, 4, 5]
print(b[0:2])

c = [1, 2, 3]
d = [4, 5, 6]
print(c + d)
print(c * 3)
print(len(c))

e = [1, 2, 3, 4, 5]
del e[2:4]
print(e)

f = [1, 2, 3]
f.append(4)
print(f)
print(f.index(2))

f.insert(0,5)
print(f)

f.pop(2)
print(f)

g = [1, 2, 3]
g.extend([4, 5])
g
print(g)

h = [6, 7]
g.extend(h)
g
print(g)