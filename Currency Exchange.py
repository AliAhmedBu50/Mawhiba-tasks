print("Welcome to Currency Exchange!")
print("----------------------------------")
print("   Made by:Ali Bu-Khamsin")
print("----------------------------------")
print("     ")
print("Enter '1' to exchange from SAR to USD")
print("Enter '2' to exchange from SAR to CAD")
print("Enter '3' to exchange from SAR to EUR")
print("Enter '4' to exchange from SAR to EGP")
print("Enter '5' to exchange from SAR to GBP")
print("Enter '6' to exchange from USD to SAR")
print("Enter '7' to exchange from CAD to SAR")
print("Enter '8' to exchange from EUR to SAR")
print("Enter '9' to exchange from EGP to SAR")
print("Enter '10' to exchange from GBP to SAR")
print("----------------------------------")
CUR1=float(input("choose currency"))
if CUR1==1:
    print("Great choice!")
    sar2usd=float(input("How many of this currency do you have?"))
    sar2usdresult=(sar2usd/3.75)
    print("Alright so you have,",sar2usdresult,'Dollar(s)!')
elif CUR1==2:
    print("Great choice!")
    sar2cad=float(input("How many of this currency do you have?"))
    sar2cadresult=(sar2cad/2.84)
    print("Alright so you have,",sar2cadresult,'Canadaian Dollar(s)!')
elif CUR1==3:
    print("Great choice!")
    sar2eur=float(input("How many of this currency do you have?"))
    sar2eurresult=(sar2eur/4.15)
    print("Alright so you have,",sar2eurresult,'Euro(s)!')
elif CUR1==4:
    print("Great choice!")
    sar2egp = float(input("How many of this currency do you have?"))
    sar2egpresult = (sar2egp/0.12)
    print("Alright so you have,", sar2egpresult, 'Eygptian Pound(s)!')
elif CUR1==5:
    print("Great choice!")
    sar2gbp=float(input("How many of this currency do you have?"))
    sar2gbpresult=(sar2gbp/4.84)
    print("Alright so you have,",sar2gbpresult,'Pound Sterling(s)!')
elif CUR1==6:
    print("Great choice!")
    usd2sar=float(input("How many of this currency do you have?"))
    usd2sarresult=(usd2sar*3.75)
    print("Alright so you have,",usd2sarresult,'Saudi Riyal(s)!')
elif CUR1==7:
    print("Great choice!")
    cad2sar=float(input("How many of this currency do you have?"))
    cad2sarresult=(cad2sar*2.84)
    print("Alright so you have,",cad2sarresult,'Saudi Riyal(s)!')
elif CUR1==8:
    print("Great choice!")
    eur2sar=float(input("How many of this currency do you have?"))
    eur2sarresult=(eur2sar*4.15)
    print("Alright so you have,",eur2sarresult,'Saudi Riyal(s)!')
elif CUR1==9:
    print("Great choice!")
    egp2sar=float(input("How many of this currency do you have?"))
    egp2sarresult=(egp2sar*0.12)
    print("Alright so you have,",egp2sarresult,'Saudi Riyal(s)!')
elif CUR1==10:
    print("Great choice!")
    gbp2sar=float(input("How many of this currency do you have?"))
    gbp2sarresult=(gbp2sar*4.84)
    print("Alright so you have,",gbp2sarresult,'Saudi Riyal(s)!')

else:
    print("Erorr 404 (INVALID NUMBER) Please try again")

print("Thank you for using this service")