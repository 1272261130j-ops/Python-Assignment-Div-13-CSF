def right_triangle(a,b,c):
    sides=[a,b,c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

a=float(input("Enter first side: "))
b=float(input("Enter second side: "))
c=float(input("Enter third side: "))

if right_triangle(a,b,c):
    print("The triangle is a right-angled triangle")
else:
    print("The triangle is not a right-angled triangle")
