lovely_loveseat_description="""Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price=254.00
stylish_settee_description="""Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price=180.50
luxurious_lamp_description="""Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price=52.15
sales_tax=0.088 #sales tax 8.8%
#first customer
customer_one_total=0 #initial cart value
customer_one_itemization="" #initial cart item
customer_one_total+=lovely_loveseat_price #purchase 1
customer_one_itemization+=lovely_loveseat_description #1st item
customer_one_total+=luxurious_lamp_price #item 2
customer_one_itemization+=luxurious_lamp_description #item 2
customer_one_tax=customer_one_total*sales_tax #adding sales tax
customer_one_itemization+="sales tax" #adding sales
customer_one_total+=customer_one_tax #adding taxes to total
print("Customer One Items") #bill header
print(customer_one_itemization) #items purchased
print("Customer One Total:")
print(customer_one_total)
#customer one reciept
#Now Customer Two arrived
customer_two_total=0 #initial cart value
customer_one_itemization="" #initial items
customer_two_total+=stylish_settee_price #value of item 1
customer_one_itemization+=stylish_settee_description #item 1
customer_two_total+=luxurious_lamp_price #value of item 2
customer_two_itemization+=luxurious_lamp_description #item 2
customer_two_tax=customer_two_total*sales_tax #implementing sales tax
customer_two_itemization+="sales tax" #adding sales
customer_two_total+=customer_two_tax
print("Customer Two Items") #bill header
print(customer_two_itemization) #items customer two purchased
print("Customer Two Total:") 
print("customer_two_total") #value customer 2 paid
#thank You
