number = int(input("กำหนดจำนวนชั้น : "))
for x in range(number):
    print(" "*(number-x),("*")*(x*2+1))