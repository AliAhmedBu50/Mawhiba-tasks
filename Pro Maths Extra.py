import math
while True:
    print("----------------------------")
    print("Made by: Ali Bu-Khamsin")
    print("----------------------------")
    print("Press 1 for Area")
    print("Press 2 for Free Calculator")
    print("Press 3 for Perimeter")
    print("Press 4 to quit")
    choice = int(input("Enter the number of your choice"))
    if choice == 1:
        print("Please choose from the options below")
        print("Enter 1 for the Area of Rectangle")
        print("Enter 2 for the Area of Triangle")
        print("Enter 3 for the Area of square")
        print("Enter 4 for the Area of circle")
        print("Enter 5 to quit")
        choice2 = int(input("Now you may choose"))
        if choice2==1:
            rectanglebase=float(input("Please enter the base of your rectangle "))
            rectangleheight=float(input("Please enter the height of your rectangle"))
            print("The area of your rectangle is",(rectangleheight*rectanglebase))
            break
        if choice2==2:
            trianglebase=float(input("Please enter the base of your triangle"))
            triangleheight=float(input("Please enter the height of your triangle"))
            print("The area of your triangle is",(triangleheight*trianglebase))
            break
        if choice2==3:
            sideofsquare=float(input("Please enter the side of your square"))
            print("The area of your square is",sideofsquare**2)
            break
        if choice2==4:
            radius=float(input("Please enter the radius of your circle"))
            print("The area of your circle is almost",(3.14159*(radius**2)))
            break
        if choice2==5:
            break
    elif choice>4:
        print("ERROR 404 (INVALID NUMBER)")
    elif choice<1:
        print("ERROR 404 (INVALID NUMBER)")
    if choice==2:
        print("====================================")
        print("Welcome to the Free Calculator")
        print("====================================")
        print("Press 1 for addition")
        print("Press 2 for subtraction")
        print("Press 3 for multiplication")
        print("Press 4 for division")
        print("Press 5 for Power")
        print("Press 6 for square root")
        print("Press 7 to exit ")
        choice3 = int(input("You may choose now"))

        if choice3==1:
            addn1=float(input("Enter the first number for your addition"))
            addn2=float(input("Enter the second number for your addition"))
            print("The sum of your addition is ",(addn1+addn2))
            break
        if choice3==2:
            subn1=float(input("Enter the first number for you subtraction"))
            subn2=float(input("Enter the second number for  your subtraction"))
            print("The total of your subtraction is ",(subn1-subn2))
            break
        if choice3==3:
            multin1=float(input("Enter the first number for your multiplication"))
            multin2=float(input("Enter second number for your multiplication"))
            print("The total of your multiplication is ",(multin2*multin1))
            break
        if choice3==4:
            divn1=float(input("Enter the first number for your division"))
            divn2=float(input("Enter the second number for your division"))
            print("the total of your division is ",(divn1/divn2))
            break
        if choice3==5:
            powern1=int(input("Enter first number for your action"))
            powern2=int(input("Enter second number for your action"))
            print("The total for ",powern1,'in the power of ',powern2,"is ",(powern1**powern2))
            break
        if choice3==6:
            sqr_rt=int(input("Enter the number"))
            print("th square root of ",sqr_rt,"is",math.sqrt(sqr_rt))
        if choice3==7:
            break

    if choice==3:
        print("=====================================================")
        print("Press 1 for the perimeter of the square")
        print("Press 2 for the perimeter of the triangle")
        print("Press 3 for the perimeter of the rectangle")
        print("Press 4 for the perimeter of the circle")
        print("Press 5 to quit")
        choice4=int(input("Enter the number of the option you want to use"))
        if choice4==1:
            square_side=float(input("Enter the side of your square"))
            print("The perimeter of your square is ",(square_side*4))
            break
        if choice4==2:
            side1tri=float(input("Enter first side of your triangle"))
            side2tri=float(input("Enter second side of your triangle"))
            side3tri=float(input("Enter third side of your triangle"))
            print("The perimeter of your triangle is ",(side1tri+side2tri+side3tri))
            break
        if choice4==3:
            width=float(input("Enter the width of your rectangle"))
            length=float(input("Enter the length of yur rectangle"))
            print("The perimeter of your rectangle is ",(length+width)*2)
        if choice4==4:
            break
    if choice==4:
        break
