def get_user_info():
    print("Welcome to the World Bank")
    name = input("Enter your name: ")
    saving = float(input("Enter an initial amount to set up your saving account: "))
    checking = float(input("Enter an initial amount to set up your checking account: "))

    bank_account = {
        "Name": name,
        "Saving": saving,
        "Checking": checking,
    }
    return bank_account


def make_deposit(bank_account, account_type, deposit_amount):
    bank_account[account_type] += deposit_amount
    print(f"\nDeposited ${deposit_amount} into {bank_account['Name']}'s {account_type} account")


def make_withdrawal(bank_account, account_type, withdrawal_amount):
    if bank_account[account_type] >= withdrawal_amount:
        bank_account[account_type] -= withdrawal_amount
        print(f"\nWithdrew ${withdrawal_amount} from {bank_account['Name']}'s {account_type} account")
    else:
        print("\nCannot withdraw. Balance too low!")


def display_account_details(bank_account):
    print("\nCurrent Account Details:")
    for key, value in bank_account.items():
        if key == "Name":
            print(f"{key}: {value}")
        else:
            print(f"{key}: ${value}")


# Program start
my_account = get_user_info()
status = True

while status:
    display_account_details(my_account)

    account_type = input("Which account (Saving / Checking): ").title()
    action = input("Deposit or Withdraw: ").title()
    amount = float(input("Enter amount: "))

    if account_type in ['Saving', 'Checking']:
        if action == 'Deposit':
            make_deposit(my_account, account_type, amount)
        elif action == 'Withdraw':
            make_withdrawal(my_account, account_type, amount)
        else:
            print("Invalid action!")
    else:
        print("Invalid account type!")

    user_choice = input("Continue? (y/n): ").lower()
    if user_choice != 'y':
        print("\nFinal Summary:")
        display_account_details(my_account)
        print("Thank you!")
        status = False
