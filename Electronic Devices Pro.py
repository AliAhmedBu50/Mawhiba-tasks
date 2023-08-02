gaming={
    "list" : [
        {"name" : "gaming mice",
        "price" : 100},
        {"name" : "gaming consoles",
        "price" : 1799}
    ],
    "message" : "gaming accessory"}
Pc={"list" : [
        {"name" : "Lenovo",
        "price" : 3000},
        {"name" : "HP",
        "price" : 2900}
    ],
    "messsage" : "Pcs"
        }
Phones={"list" : [
        {"name" : "Apple",
        "price" : 3000},
        {"name" : "Android",
        "price" : 2900}
    ],
    "message" : "Phones"
        }

category= [gaming,Pc,Phones]
no = ["n" or "no" or "NO" or "No" or "nO" or "N"]
yes = ["y", "yes", "YES", "Yes", "yEs", "YeS", "yes", "yES", "yeS", "YEs "]
border=("===============================")
cart = []
#cartprice = []
print("Made by:Ali Bukhamsin")
print(border)
print("Welcome to this Online store program")
print(border)
def start1() :
    start = str(input("Enter yes to continue and enter no to stop "))
    if start in yes:
        print(border)
        print("What category would you like to buy from")
        print(border)
        print("Enter 1 for gaming accessories")
        print(border)
        print("Enter 2 for pc")
        print(border)
        print("Enter 3 for phones and phone accessories")
        print(border)
        service1 = int(input("Please choose a service"))
    #print(category[service1-1])
    print("What ", category[service1-1]["message"], "would you like?")
    index = 1
    for i in category[service1-1]["list"]:
        print("Enter ",index,'for ', i["name"]," the price is ", i ["price"])
        index+=1
    choice1=int(input("Please choose now"))
    print(category[service1-1]["list"][choice1-1])
    ch_cart1=(input("would you like to add it into cart? yes to add it no to discard"))
    if ch_cart1 in yes:
        cart.append(category[service1-1]["list"][choice1-1])
        print("Product is added to cart")
        start_again1=input("Do you want to continue shopping yes or no ")
        if start_again1 in yes:
            start1()
        else:
            print("Your total is")

start1()
total=0
for i in cart:
    print(i["name"]," Price is ",i["price"])
    total=total+i["price"]
print("Your total is", total)