def login():
    user = input("กรอกusername : ")
    password = input("กรอกรหัสผ่าน :")
    if user == "admin" and password == "admin":
        print("Login Success Please select a menu ")
        return showMenu()
    else:
        print("Please Login Try Again")
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return (menuSelect())
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()
def vatCalculator():
    totalPrice = int(input("Price : "))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print(result)
    return exit()

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vat = 7
    totalPrice = price1 + price2
    result = totalPrice + (totalPrice * vat / 100)
    print(result)
    return exit()
def exit():
    ext = input("Want to do the transaction again? : (Y/N) ")
    if ext == "y" or ext ==  "Y" :
        return showMenu()
    elif ext != "n" or ext ==  "N" :
        print("Please Try Again")
        return exit()
    else:
        print("Thank you for using the service.")

print(login())