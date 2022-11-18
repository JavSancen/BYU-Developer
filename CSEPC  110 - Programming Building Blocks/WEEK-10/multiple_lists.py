banks = []
balances = []

bank = ""
balance = 0
sum = 0

while bank != "quit":
    bank = input("What is the name of this account?: ")

    if bank != "quit":
        balance = float(input("What is the balance?: "))
        banks.append(bank)
        balances.append(balance)

print()
print("Account information:")

for i in range(len(banks)):
    print(f"{i} - {banks[i]} ${balances[i]}")
    sum += balances[i]
print()
print(f"Total: ${sum}")
print(f"Average: ${sum / len(balances):.2f}")
print()

highest_bank = None
highest_balance = -1
for i in range(len(banks)):
    bank = banks[i]
    balance = balances[i]

    if balance > highest_balance:
        highest_balance = balance
        highest_bank = bank

print(f"Highest balance: {highest_bank} - {highest_balance:.2f}")

change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account?: ")

    if change_account == "yes":
        index = int(input("What account index do you want to update?: "))
        new_amount = float(input("What is the new amount?: "))

        balances[index] = new_amount

    else:
        print("\nAccount Information:")
        for i in range(len(banks)):
            print(f"{i} - {banks[i]} ${balances[i]}")


