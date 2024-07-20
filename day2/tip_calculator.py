
print ('Welcome to the tip calculator')

bill = float(input('What was the total bill '))

# total_friends = 5

tip = int(input('How much tip would you like to give? 10, 12, or 15? '))

people = int(input('How many people to split the bill?'))

tip_percentage = (tip/100)* bill

total_bill = bill + tip_percentage

split_bill = total_bill / people

print(f'each person need to pay {split_bill}')
# print(split_bill)