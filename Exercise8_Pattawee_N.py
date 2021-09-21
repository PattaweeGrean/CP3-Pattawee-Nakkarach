print("Please login")
usernameInput = input("Username : " )
passwordInput = input("Password : " )
if usernameInput == "user" and passwordInput == "user" :
    print("Login success!")
    print("--------------------------------")
    print("Please select the desired product!!")
    print("!!-----product list-----!!")
    a = "1.T-shirt      "
    b = "2.hoodie       "
    c = "3.trousers     "
    d = "4.belt         "
    e = "5.shoe         "
    sum ="total : "
    vat = 7
    print(str(a), 350,"THB")
    print(str(b), 450,"THB")
    print(str(c), 390,"THB")
    print(str(d), 150,"THB")
    print(str(e), 650,"THB")
    ProductSelected = int(input("Selected Your Product : "))
    amount = int(input("Amount : "))
    if ProductSelected == 1:
        print("-----------------------------------")
        print("!!-----item list-----!!")
        print(str(a), 350, "THB",amount,"piece")
        print("-----------------------------------")
        print(sum,350*amount,"THB")
        print("!!---Thank you for using the service.---!!")

    elif ProductSelected == 2:
        print("-----------------------------------")
        print("!!-----item list-----!!")
        print(str(a), 450, "THB", amount, "piece")
        print("-----------------------------------")
        print(sum, 450 * amount, "THB")
        print("!!---Thank you for using the service.---!!")
    elif ProductSelected == 3:
        print("-----------------------------------")
        print("!!-----item list-----!!")
        print(str(a), 390, "THB", amount, "piece")
        print("-----------------------------------")
        print(sum, 390 * amount, "THB")
        print("!!---Thank you for using the service.---!!")
    elif ProductSelected == 4:
        print("-----------------------------------")
        print("!!-----item list-----!!")
        print(str(a), 150, "THB", amount, "piece")
        print("-----------------------------------")
        print(sum, 150 * amount, "THB")
        print("!!---Thank you for using the service.---!!")
    elif ProductSelected == 5:
        print("-----------------------------------")
        print("!!-----item list-----!!")
        print(str(a), 650, "THB", amount, "piece")
        print("-----------------------------------")
        print(sum, 650 * amount, "THB")
        print("!!---Thank you for using the service.---!!")
    else:
        print("There is no item in your selection Please try again")
else:
    print("Please Login try again")