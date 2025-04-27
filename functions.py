from values import *

def start():
    print("Menu")
    print("")
    for i in range(0,len(menu)):
        print(f"{menu[i][0]} - {menu[i][1]} - {menu[i][2]}")

    print("Choose the items from the menu")
    print("Type 1 to see your order list and price.")
  
def receive():
    global item
    global first  
    global count
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
                        print(f"{menu[i][1]} - ${menu[i][2]} added")
                        break
                    else:
                        count+=1
                if count==len(menu):
                    first=-1
                else:
                    first=1
                count=0
            break

        except ValueError:
            print("Type a number!")

def orderPrice():
    global bill
    print("\nYour order is:\n")
    
    for i in range(0,len(order)):
        print(f"     {i+1} - {order[i][0]} - ${order[i][1]}")
        bill=bill+order[i][1]

    print(f"\nThe final price is: ${bill}\n")
