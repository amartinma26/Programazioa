a = [
    1,
    2,
    3,
    4,
]
b = a
b.append(4)
print(a)

c = a.copy()
c.append(5)
print(a, c)
