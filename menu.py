item=0
order=[]
bill=[]
count=int(0)
menu=[
    [101,"The OG Cheeseburger",7.99],
    [102,"The Double Trouble",10.99],
    [103,"The Backyard BBQ",11.49],
    [201,"The Volcano Burger",9.99],
    [202,"The Truffle Deluxe",12.99],
    [203,"The Hawaiian Wave",10.49],
    [301,"Crispy Chicken Crunch",8.99],
    [302,"Grilled Perfection",9.49],
    [303,"The Ultimate Veggie",9.99],
    [401,"Classic Fries",3.99],
    [402,"Loaded Cheese Fries",5.99],
    [403,"Onion Rings",4.99],
    [501,"Hand-Spun Milkshakes",4.99],
    [502,"Craft Sodas",2.49],
    [503,"Churro Bites",5.49]    
]


#print(len(items)) #quantity items 
print("Menu")
print("")
for i in range(0,len(menu)):
    print(f"{menu[i][0]} - {menu[i][1]} - {menu[i][2]}")

print("Choose the items from the menu")
print("Type 1 to exit.")

while True:
        try:
            item=int(input("Enter the item code:"))
            break
        except ValueError:
            print("Type a number:")


while item!=1:
             
    if count==len(menu) :
        item=int(input("Type a valid code:"))
        count=0
    else:
        for i in range(0,len(menu)):       
            if item==menu[i][0]:
                order.append([str(menu[i][1]),float(menu[i][2])])
                print(order)
            else:
                count+=1
    item=1
    
     
    
    

    
     



