'''
Created on Feb 14, 2014

@author: Filipchyk_YP
'''

DATE = 0
PAYMENT = 1
AMOUNT = 2

from datetime import datetime

file = open("MyExpensesStmt1392367389278.csv", "r", encoding='cp1251')
 
payments = []
FIELDS_COUNT = 3

for line in file.readlines():
    fields = line.split(";")
    if len(fields) == FIELDS_COUNT:
        if fields[DATE].find(".") != -1:
            fields[DATE] = datetime.strptime(fields[DATE].strip(), '%d.%m.%Y')
            fields[PAYMENT] = fields[PAYMENT].strip()
            fields[AMOUNT] = float(fields[AMOUNT].strip().replace(",", "."))
            payments.append(fields)

# for payment in payments:
#     print(payment)

from categories import categories_by_payments

payments_by_category = {}
for payment in payments:
    category = categories_by_payments[payment[PAYMENT]]
    if payments_by_category.__contains__(category):
        payments_by_category[category] += payment[AMOUNT]
    else:
        payments_by_category[category] = payment[AMOUNT]
        
for category in payments_by_category:
    print(category + ": " + str(payments_by_category[category]))
# print(payments)
     
file.close()