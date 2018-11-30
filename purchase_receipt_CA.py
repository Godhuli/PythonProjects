# Create Purchasing Information and Receipts for Lovely Loveseats
######################################################

# Description for loveseat
lovely_loveseat_description = '''lovely loveseat. Tufted
polyester blend on wood. 32
inches high x 40 inches wide x
30 inches deep. Red or white
'''

# Price for loveseat
lovely_loveseat_price = 254.00

# Description for settee
stylish_settee_description = ''' Stylish Settee. Faux leather on
birch. 29.50 inches high x
54.75 inches wide x 28 inches
deep. Black.'''

# Price for settee
stylish_settee_price = 180.50

# Description for lamp
luxurious_lamp_description = ''' Luxurious Lamp. Glass an iron.
36 inches tall. Brown with
cream shade.'''

# Price for lamp
luxurious_lamp_price = 52.15

# Sales tax is 8.8%
sales_tax = 0.088

# Expenses for first  customer
customer_one_total = 0
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# First Customer receipt
print("Customer One Items: ")
print(customer_one_itemization)
print()
print("Customer One total: ")
print(customer_one_total)
print()

# Expense for second customer
customer_two_total = 0
customer_two_itemization = ""
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description
customer_two_tax = customer_one_total * sales_tax
customer_two_total += customer_one_tax

# Second Customer receipt
print("Customer two Items: ")
print(customer_two_itemization)
print()
print("Customer two total: ")
print(customer_two_total)









