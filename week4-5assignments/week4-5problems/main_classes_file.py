from classes.inventory import *

purchase_done = False

my_purchase = InventoryItem("Anthony's Purchase")

while not purchase_done:
    done_answer = input("Are you done with your purchase? (Y/N) ")
    if done_answer.lower() == "n":
        product_add = input("Please type the quantity you want to order, or type nothing to order 1: ") 
        my_purchase.buy_item(product_add)
    else:
        purchase_done = True

print("Here is how much you purchased: ")
print(my_purchase.quantity_total_purchased)

print("Here is how much inventory was left: ")
print(my_purchase.quantity)
