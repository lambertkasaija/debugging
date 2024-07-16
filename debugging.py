user = [
    {'name': 'Peter', 'amount': 2500000},
    {'name': 'Isaac', 'amount': 150000},
    {'name': 'Jane', 'amount': 300000},
    {'name': 'John', 'amount': 4000000},
    {'name': 'Betty', 'amount': 700000}  
]

totalAmount = sum(user['amount'] for user in user)  

for element in user:
    print(f"{element['name']} deposited {element['amount']} and your interest is {element['amount'] * 0.1} and your total amount is {element['amount'] * 1.1}")
