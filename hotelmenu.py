menu={
 'pizza':40,
 'pasta':50,
 'burger':60,
 'coffee':80,
 'salad':50 ,
}


print("welcome to PYTHON restaurant")
print("pizza: Rs40\npasta: Rs50\nburger: Rs60\ncoffee: Rs80\nsalad: Rs50 ")

order_total = 0

item1= input("enter the name of item you want to order=")
if item1 in menu:
    order_total += menu[item1]
    print(f"your item {item1} has been added to your order")

else:
    print(f"ordered item {item1} is not avaialable yet!")

another_order = input("do you want to add another item? (yes/no)")
if another_order == "yes":
    item2 = input("enter the name of second item =") 
    if item2 in menu:
        order_total +=menu[item1] 
        print(f"item {item2} has been added to order")

    else:
       print(f"ordered item {item2} is not avaialable yet!")  

print(f"the total amount of item to pay is {order_total}")       
print("your order is:
")