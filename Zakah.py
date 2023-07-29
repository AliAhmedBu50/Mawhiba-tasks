border="=============================="
print("Welcome to Zakah Calculating Service!")
print(border)
print("Press 1 for money zakah")
print(border)
print("Press 2 for cows zakah")
print(border)
print("Press 3 for sheep zakah")
print(border)
print("Press 4 for dates and beans zakah")
print(border)
print("Press 5 for trade offers zakah")
print(border)
print("Press 6 for ore zakah")
print(border)
print("Press 7 for blunt zakah")
print(border)
print("Press 8 for gold zakah")
choice=int(input("Choose service"))
if choice == 1:
    print("Thank you for choosing the Zakah Calculating Service!")
    amount=float(input("Enter the amount of money you have"))
    print("You should pay",(amount*0.25),"riyal(s)")
if choice == 2:
    amountcows=int(print("How many cows do you have"))
    if amountcows <= 29:
        print("You dont have to pay zakah for your cows")
    elif amountcows >= 30:
        print("You should pay for 1 female 1 year old cow or 1 male 1 year old cow")
    elif amountcows >=40:
        print("You should pay for 1 female 2 year old cow")
    elif amountcows >=60:
        print("You should pay for 2 female 1 year old cows of 2 female 1 year old cows")
    elif amountcows >=70:
        print("You should pay for 1 female 2 year old cow and 2 female 1 year old cows or 1 female 2 year old cow and 2 male 1 year old cows")
    elif amountcows >= 80:
        print("Error 404 (Invalid Input)")
if choice == 3:
    amountsheep=int(input("How many sheep do you have"))
    if amountsheep <= 39:
        print("You dont have to pay zakah for your sheep")
    elif amountsheep >= 40:
        print("You have to pay for 1 goat or sheep (not less than 1 year old)")
    elif amountsheep >= 121:
        print("You have to pay for 2 goats or sheep (not less than 1 year old)")
    elif amountsheep >= 201:
        print("You have to pay for 3 goats or sheep (not less than 1 year old)")
if choice == 4:
    kg_amount=int(input("How many kilograms of date do you have?"))
    if kg_amount<=600:
        print("You dont have to pay zakah for your dates")
    elif kg_amount>=600:
        print("How do you water your palm trees?")
        water_method=int(input("If you water it using rainwater press 1 and if you use well water press 2"))
        if water_method==1:
            print("You should sell ",(kg_amount*0.1),"kilograms of your dates")
        elif water_method==2:
            print("You should sell ",(kg_amount*0.05),"kilograms of your dates")
        else:
            print("ERROR 404 (INVALID INPUT)")
