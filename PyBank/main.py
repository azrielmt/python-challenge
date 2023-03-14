import os
import csv 

# Had an issue with a "I/O Operation on Closed File" error, was able to source this for help: https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file"
budget_csv = os.path.join("Resources", "budget_data.csv")

budget_data = []

greatest_inc = 0
greatest_dec = 0

with open(budget_csv) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]), "change": 0})

month_tot = len(budget_data)

#Personal Note: Must do this for later
prev_change = budget_data[0]["amount"]
for i in range(month_tot):
    budget_data[i]["change"] = budget_data[i]["amount"] - prev_change
    prev_change = budget_data[i]["amount"]

#Lambda: https://www.w3schools.com/python/python_lambda.asp
profit_inc = max(budget_data, key=lambda x:x['change'])
profit_dec = min(budget_data, key=lambda x:x['change'])

total = sum(row["amount"] for row in budget_data)
total_changes = sum(row["change"] for row in budget_data)
avg = round(total_changes / (month_tot-1), 2)

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {month_tot}')
print(f'Total: ${total}')
print(f'Average Change: ${avg}')
print(f'Greatest Increase in Profits: {profit_inc["month"]} (${profit_inc["change"]})')
print(f'Greatest Decrease in Profits: {profit_dec["month"]} (${profit_dec["change"]})')

#For text file.
filepath = os.path.join('.', 'Analysis', 'PyBankResults.txt')
with open(filepath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {month_tot}', file=text_file)
    print(f'Total: ${total}', file=text_file)
    print(f'Average Change: ${avg}', file=text_file)
    print(f'Greatest Increase in Profits: {profit_inc["month"]} (${profit_inc["change"]})', file=text_file)
    print(f'Greatest Decrease in Profits: {profit_dec["month"]} (${profit_dec["change"]})', file=text_file)
