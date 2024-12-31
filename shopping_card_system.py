products = []

while True:
    choice = int(input("1: Add\n 2 : Remove \n 3: List All Items \n 4: Total Cost \n"))
    if choice ==1:
        name =input("Enter the product name:")
        price = float(input("Enter the price:"))
        quantity = int(input("enter the Quantity:"))

        item = {"name": name, "price": price, "Quantity": quantity}
        products.append(item)
        print("product Added successfully")


    
    elif choice ==2:
        #remove
        name_remove =input("Enter the product name you want to delete:")
        is_removed = False
        for item in products:
           products.remove(item)
           print("product removed successfully")
           is_removed = True
           break
        if  is_removed:
           print("The product is deleted")
        else:
            print("The product is not found")


    elif choice ==3:
        #display all items
        if not products:
            print("products are not available.")
        else: 
         for item in products:
            print(f"Name:{item['name']} Quantity:{item['Quantity']} Price:{item['price']} Total cost:{item['Quantity']*item['price']}")



    elif choice ==4:
        for item in products:
            Total_cost = sum(item['price']*item['Quantity'] for item in products )
            print(f"The total cost is rs.{Total_cost}")

    else:
        print("Invalid input, Please enter the valid ")
