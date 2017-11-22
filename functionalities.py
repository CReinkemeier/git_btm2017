import file_manager as fM

def say_hi():
    print("Welcome")

def new_client():
    new_client = input("...Please enter name of new client. ")
    if not new_client in fM.get_clients():
        fM.add_client(new_client)
        print("Client added !")
    else:
        print("Client already exist !")
    
def new_transaction():
    bank_clients = fM.clientlists()
    print ("Here are the clients :", bank_clients)
    client_debtor = input("Name of person who will borrow money: ")
    client_creditor = input("Name of person who will lend money: ")
    transaction_amount = input("Transaction amount: ")
    fM.add_banktransaction(client_debtor, client_creditor, transaction_amount)


def look_credit():
    client_list = fM.get_clients()
    print(client_list)
    client_name = input("Which client's account would you like to check? ")
    if client_name not in client_list:
        print("Unknown client")
        return
    transactions = fM.get_transactions()
    solde = 0
    for transaction in transactions:
        if transaction[0] == client_name:
            solde -= float(transaction[2])
        elif transaction[1] == client_name:
            solde += float(transaction[2])
    print(client_name+" have "+str(solde)+" gazillions")
