import pandas as pd

data = pd.read_csv('data.csv')
items = data['Item']
total = data['Total']
#calculate the numbers of stacks and the rest if not a full stack
#like 5 stacks 25 cobblestone
stacks = total // 64
missing = total % 64
stacksnotfull = 64 - missing
stacks = stacks.astype(str) + ' stacks ' + missing.astype(str)
missing = data['Missing']
available = data['Available']

# save the new columns to an excel file
df = pd.DataFrame({'Item': items, 'Total': total, 'Stacks': stacks, 'Missing': missing, 'Available': available})
df.to_excel('data.xlsx', sheet_name='sheet1', index=False)
