import file_manager as fM

def say_hi():

def new_client():
    pass
    
def new_transaction():
    bank_clients = fM.clientlists()
    print ("Here are the clients", bank_clients)
    client_debtor = input("Name of person who will borrow money: ")
    client_creditor = input("Name of person who will lend money: ")
    transaction_amount = input("Transaction amount: ")
    fM.add_banktransaction(client_debtor, client_creditor, transaction_amount)

def look_credit():
    pass
