from values import *



def start():
    print("Menu")
    print("")
    for i in range(0,len(menu)):
        print(f"{menu[i][0]} - {menu[i][1]} - {menu[i][2]}")

    print("Choose the items from the menu")
    print("Type 1 to exit.")
  
def receive():
    global item
    global first  
    global count
    
    while True:  #Receive list
        try:
            while item!=1:
                if first==0:
                    item=int(input("Enter the item code:"))
                else:
                    item=int(input("Anything else?"))
                    
                if item==1:
                    break
                
                for i in range(0,len(menu)):       
                    if item==menu[i][0]:
                        order.append([str(menu[i][1]),float(menu[i][2])])
                        print(order)
                        break
                    else:
                        count+=1

                while count==len(menu):
                    while True :
                        try:
                            item=int(input("Type a valid number:"))
                            if item==1:
                                count=0
                                break
                            else:
                                for i in range(0,len(menu)):
                                    if item==menu[i][0]:
                                        order.append([str(menu[i][1]),float(menu[i][2])])
                                        print(order)
                                        count=0 
                                break   
                        except ValueError:
                            print("Type a number!")

                first=1
                count=0

            break
        except ValueError:
            print("Type a number!")