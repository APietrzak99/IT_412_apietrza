#this is 2-1
import os.path
import shutil

temp_output = ""

with open("text_files/movies.txt") as python_file:
    for line in python_file:
        temp_output = temp_output + line

#this is 2-3
if os.path.isfile("text_files/new_output.py"):
    pass
else:
    with open("text_files/new_output.py", "w") as file_output:
        file_output.write(temp_output)

#this is 2-2
initial_input = input("Type a meal that you would like to have this week. ")

new_input = ""

while initial_input != 'stop':
    new_input = new_input + initial_input+"\n"
    initial_input = input("Please enter a meal for the week. Type stop to end the program.")

with open("text_files/dinner_menu.txt", "w") as file_output:
    file_output.write(new_input)

#this is 2-4
import json
if os.path.isfile("text_files/my_car.json"):
    with open("text_files/my_car.json") as json_obj:
        car_data = json.load(json_obj)
        print(car_data)
    change_car_input = input("Would you like to change the model of car listed? Type a new model if you would, or else type no.")
    if change_car_input !='no':
        with open("text_files/my_car.json","w") as json_obj:
            json.dump(change_car_input, json_obj)
else:
    car_input = input("Please enter the model of the car you drive.")
    with open("text_files/my_car.json","w") as json_obj:
        json.dump(car_input,json_obj)

