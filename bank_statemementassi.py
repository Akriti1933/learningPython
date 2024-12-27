Balanace = 1000
print("Welcome")

print("option 1:check_balance")
print("option 2:deposite")
print("option 3:withdraw")

choice = int(input("choose an option (1-3):"))

if choice ==1:
    print(f"your current balane is: ${Balanace}")
elif choice ==2:
    deposite_amount = float(input("Enter deposite amount: $"))
    if deposite_amount <=0:
        print("Deposite amount must be greater than 0.")
    else:
        Balanace += deposite_amount
        print(f"Successfully deposited ${deposite_amount}")
        print(f"your new balance is {Balanace}")
elif choice ==3:
    withdrawal_amount = float(input("Enter the amount you need: $"))
    if withdrawal_amount <=0:
        print("withdrawal amount must be greater than 0.")
    elif withdrawal_amount > Balanace:
        print("insuffient funds!")
        print(f"your current balance is:${Balanace}")
    else:
        Balanace -= withdrawal_amount
        print(f"successfully withdrew ${withdrawal_amount}")
        print(f"your new balance is:${Balanace}")

else:
    print("invalid choice. please select a valid option.")



    