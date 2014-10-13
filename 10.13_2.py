x = int(input("please enter an integer:"))

if x < 0:
    x = 0
    print("x changed to zero")
elif x == 0:
    print("x is zero")
elif x == 1:
    print("x is one")
else:
    print("x is not zero")