import random


a, b, c = random.random()*200-100, random.random()*200-100, random.random()*200-100
print("The  values of a, b, and c:")
print("a= ", a)
print("b= ", b)
print("c= ", c,end="\n\n")

if a > b:
    if b > c:
        print("The order of abc from largest to smallest is: \na, b, c")
    elif a > c:
        print("The order of abc from largest to smallest is: \na, c, b")
    else:
        print("The order of abc from largest to smallest is: \nc, a, b")
else:
    if a > c:
        print("The order of abc from largest to smallest is: \nb, a, c")
    elif b > c:
        print("The order of abc from largest to smallest is: \nb, c, a")
    else:
        print("The order of abc from largest to smallest is: \nc, b, a")
del a, b, c
