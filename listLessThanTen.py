a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in range(len(a)):
    if a[i] < 5:
        b.append(a[i])

print(b)
