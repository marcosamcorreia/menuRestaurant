from values import *

def start():
    print("Menu")
    print("")
    for i in range(0,len(menu)):
        print(f"{menu[i][0]} - {menu[i][1]} - {menu[i][2]}")

    print("\nChoose the items from the menu")
    print("Type 1 to see your order list and price.\n")
    receive()
  
def receive():
    global item
    global first  
    global count
    global bill
    while True:  #Receive list
        try:
            while item!=1:
                if first==0:
                    item=int(input("Enter the item code:"))
                elif first==-1:
                    item=int(input("Type a valid number:"))
                else:
                    item=int(input("Anything else?"))
                  
                for i in range(0,len(menu)):       
                    if item==menu[i][0]:
                        order.append([str(menu[i][1]),float(menu[i][2])])
                        bill=bill+menu[i][2]
                        print(f"{menu[i][1]} - ${menu[i][2]} added")
                        break
                    else:
                        count+=1
                if count==len(menu):
                    first=-1
                else:
                    first=1
                count=0
            orderPrice()
            break

        except ValueError:
            print("Type a number!")

def orderPrice():
    global bill
    global count
    global item
    num=len(order)
    while True:
        try:
            if num==0:
                print("\nYour order is empty.")
                print("\nEnding program...\n")
                break
            else:   
                print("\nYour order is:\n")
                showOrder()
                print(f"\nThe total price is: ${bill}\n")
                print("Type 1 to end the program.")
                print("Type 2 to remove an item")
                item=int(input(":"))
            match item:
                case 1:
                    finalOrder()
                    break
                case 2:
                    delete()
                    break
                case _: 
                    print("Type a valid number")
                    if num==0:
                        print("1 to end the program")
                    else:
                        print("1 to end or 2 to remove item(s):")

        except ValueError:
            print("Type a number!")
    
def delete ():
    global count
    global item
    global bill
    count=0
    verror=0
    while True:
        try:
            while item!=0 and len(order)>0 :
                if count==0 or verror==count:
                    if count==0:
                        print("\nType the item number to remove")
                    print("0 to end the process")
                    item=int(input(":"))
                    if item==0:
                        break
                    count=1
                else:
                    print("\nWant to remove more items?")
                    print("0 to exit")
                    item=int(input(":"))
                    if item==0:
                        break
              
                if item-1<=len(order) and item>0: 
                    bill=bill-order[item-1][1]
                    order.remove(order[item-1])
                    print()
                    showOrder()
                    print(f"\nThe total price is: {round(bill,2)}")
                else:
                    print("Type a valid number")
                    print("0 to leave")
                    item=int(input(":"))
            if len(order)<1:
                print("Your order is empty.")
                break
            else:
                return finalOrder()
        except ValueError:
            verror=1
            count=1
            print("Type a number!")

def finalOrder():
    global bill
    print("\n The final order is:\n")
    showOrder()
    print(f"\nThe final price is:${round(bill,2)}\n")
    print("Ending program...")

def showOrder():
    for i in range(0,len(order)):
        print(f"     {i+1} - {order[i][0]} - ${order[i][1]}")
    