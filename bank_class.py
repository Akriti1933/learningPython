balance =1000
print("Welcome to Atm")

choice =input("choose an option\n 1.check balance \n 2.Deposite \n 3.Withdraw \n 4. Exit \n")

if choice == "1":
    print(f"your balance is: {balance}")
elif choice == "2":
    amount = input("enter the amount to deposite:")

    balance = balance + int(amount)
    print("your balance is",balance)

elif choice =="3":
    amount = int(input("enter the amount to withdraw:"))
    if balance< amount:
        print("have to enough balanace")
    else:
        print(f"{amount} is withdrawn from your account:")
        balance =balance-amount
        print("your balance is:",balance)

elif choice =="4":
    print("thank you for visiting")

else:
    print("Invalid choise! please enter the choice form(1-4)")






