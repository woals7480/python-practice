s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)

print(s1 - s2)
print(s1.difference(s2))

s1.add(4)
print(s1)

s2.update([1, 2, 3])
print(s2)

s2.remove(2)
print(s2)