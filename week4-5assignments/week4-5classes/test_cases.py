from classes.pizza import Pizza

pizza_done = False

my_pizza = Pizza("Mike's Pizza")

while not pizza_done:
    done_answer = input("Are you done with your pizza? (Y/N) ")
    if done_answer.lower() == "n":
        pizza_action = input("Do you want to add or remove a topping from your pizza? (A/R) ")
        if pizza_action.lower() == "a":
            pizza_topping = input("Please type what topping you'd want on your pizza: ")
            my_pizza.addTopping(pizza_topping)
        else:
            pizza_topping = input("Please type what topping you want to remove from your pizza: ")
            my_pizza.removeTopping(pizza_topping)
    else:
        pizza_done = True

print("Here are the toppings you requested: ")
print(my_pizza.toppings)