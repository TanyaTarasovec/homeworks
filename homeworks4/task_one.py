a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

ab = dict()

for key, value in a.items():
    if key in b:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [value, None]


for key, value in b.items():
    if key in a:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [None, value]

print(ab) 