def printUser():
    print("Hello " + name +".")
    print("You will be 100 years in the year " + str(cent))


name = input("Enter your name? ")
age = int(input("Enter your age "))
usr = int(input("Enter a number "))
cent = (100 - age) + 2019

for i in range(usr):
    printUser()
