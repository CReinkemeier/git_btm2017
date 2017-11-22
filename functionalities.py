import file_manager as fM

def say_hi():
    print("Welcome")

def new_client():
    pass
    
def new_transaction():
    pass
    
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
