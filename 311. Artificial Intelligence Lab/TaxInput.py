def get_tax(income):
    tax = 0

    if income < 10_000: # 0% tax
        tax = 0 
    elif 10_000 < income < 50_000: # 5% tax
        tax = income * 0.05 
    elif 50_000 < income < 1_00_000: # 10% tax
        tax = income * 0.1 
    else: # 15% tax
        tax = income * 0.15 

    return tax

def main():
    while True:
        choice = int(input("Enter 1 to know your tax input and 0 to exit\n"))

        if choice == 1:
            income = int(input("Enter your income in Rs."))
            print(f"Your tax is Rs. {get_tax(income)}")

        elif choice == 0:
            print("Exiting...")
            break

        else:
            print("Invalid choice.\nEnter a number between 0 and 1")

main()
