data = [2, 5, 79, 4, 0, 8]
max = None
for i in data:
    if max is None or max < i:
        max = i

print(max)
