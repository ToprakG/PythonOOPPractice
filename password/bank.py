class User:
    def __init__(self, name, surname, location, country, postal_code):
        self.name = name
        self.surname = surname
        self.location = location
        self.country = country
        self.postal_code = postal_code
    
    def get_private_details(self):
        print("Your full name:")
        print(self.name and self.surname)
        print("Your location:")
        print(self.location and self.country)
        print("Your postal code:")
        print(self.postal_code)
    
class Account(User):
    def __init__(self, name, surname, location, country, postal_code, money, transactions, id):
        super.__init__(name, surname, location, country, postal_code)
        self.money = money
        self.transactions = []
        self.id = id
    
    def get_money(self):
        print(self.money)
    
    def transaction(self):
        starting_transaction = input("Do you wanna do a transaction?")
        if starting_transaction == "Yes":
            print("First of all you need to fill these details listed...")
            transaction_name = input("Name:")
            transaction_surname = input("Surname:")
            transaction_id = input("Id:")
            transaction_payed = int(input("How much payed?"))
            try:
                if transaction_payed < self.money:
                    print("Starting...")
                    try:
                        if transaction_name and transaction_surname and transaction_id is in User:
                            print("User found!")
                            print("Paying..")
                            self.money -= transaction_payed
                            self.transactions.append(transaction_name, transaction_surname, transaction_id, transaction_payed)
                            print("Done!")
                else:
                    print("Not enough money..")

        