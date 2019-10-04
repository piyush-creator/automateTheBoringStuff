def reverse(usr):
    x = ''
    for i in range(len(usr)):
        x += usr[len(usr)-1-i]

    return x


usr = input("Enter a name> ")
rus = reverse(usr)

if usr == rus:
    print("Its a palindrone")
else:
    print("Its not a palindrone")
