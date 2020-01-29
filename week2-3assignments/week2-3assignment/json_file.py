import json
import os
import shutil
from functions.functions import load_config
from functions.functions import save_config
from functions.functions import add_config
from functions.functions import modify_config
from functions.functions import delete_config

load_config()

initial_input = input("Would you like to change any information above? Press any key if you do, or type no if you don't. ")
while initial_input != "no":
    change_type_input = input("Would you like to add something or modify an existing configuration? Type add to add something, modify to modify something, or delete to delete something.Type No to exit. ")
    if change_type_input == "add":
        add_config_input = input("Which config option would you like to add? ")
        add_config_info_input = input("What is the option going to be set to? ")
        add_config(add_config_input,add_config_info_input)
        load_config()
    elif change_type_input == "modify":
        modify_config_input = input("Which config option would you like to modify? ")
        modify_config_info_input = input("What is the option going to be set to? ")
        modify_config(modify_config_input,modify_config_info_input)
        load_config()
    elif change_type_input == "delete":
        delete_config_input = input("Which config option would you like to delete? ")
        delete_config(delete_config_input)
        load_config()
    elif change_type_input == "no":
        break
else:
    exit()
