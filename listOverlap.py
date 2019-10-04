import random

a = []
b = []
c = []

for i in range(5):
    x = random.randint(0, 100)
    a.append(x)

for i in range(5):
    x = random.randint(50, 100)
    b.append(x)

for i in b:
    if i in a:
        c.append(i)

print("List a --->"+ str(a))
print("List b --->"+ str(b))
print(c)
