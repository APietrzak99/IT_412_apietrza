import json
import os
import shutil
import time

def load_config():
    """verifies if the file config_override.json exists, and if it does, loads and display it's contents, if the file doesn't exist, it loads basic_config.json and displays
    that instead
    Arguments:
        n/a
    returns:
        n/a
    """
    if os.path.isfile("text_files/config_override.json"):
        with open("text_files/config_override.json") as json_obj:
            config_data = json.load(json_obj)
            print(config_data)
    else:
        with open("text_files/basic_config.json") as json_obj:
            config_data = json.load(json_obj)
            print(config_data)

def save_config(passed_input, passed_key, passed_value):
    """processes input that is passed to it, then overwrites data if save option is accepted, discard will pass through the function 
    Arguments:
        passed_input
    returns:
        new file version of config_override if save is accepted, nothing if discarded
    """
    config_override_dict = {"memory": "32MB", "safe_mode": "on", "error_log": "logs/errors.log","allow_file_uploads": "Yes", "use_caching":"Yes", "caching_file":"cache/filecache.cache", "mail_host": "mail.apphost.com"}
    if passed_input == "S":
        if os.path.isfile("text_files/config_override.json"):
            shutil.copy2("text_files/config_override.json", "text_files/config_override.json.backup" + str(time.time()))
            with open("text_files/config_override.json") as json_obj:
                modify_config_data = json.load(json_obj)
                modify_config_data.update({passed_key: passed_value})
            with open("text_files/config_override.json","w") as json_obj:
                json.dump(modify_config_data, json_obj)
        else:
            config_override_dict.update({passed_key:passed_value})
            with open("text_files/config_override.json","w") as file_output:
                file_output.write("")
            with open("text_files/config_override.json","w") as json_obj:
                json.dump(config_override_dict, json_obj)
    elif passed_input == "D":
        pass

def add_config(add_config_input, add_config_info_input):
    """processes two input strings add_config_input, and add_config_info_input, verifies that they exist, then passes them to save_config alongside an input for saving
    Arguments:
        add_config_input, add_config_info_input
    returns:
        N/A
    """
    if add_config_info_input and add_config_input:
        save_input = input("Would you like to save this? Press S to save or D to discard.")
        save_config(save_input,add_config_input,add_config_info_input)
    else:
        print("You did not enter anything.")

def modify_config(passed_modify_config,passed_modify_info):
    """ processes two input strings modify_config_input, and modify_config_info_input, verifies that they exist, then passes them to save_config alongside an input for saving
    Arguments:
        passed_modify_config,passed_modify_info
    returns:
        N/A"""
    if passed_modify_config and passed_modify_info:
        if os.path.isfile("text_files/config_override.json"):
            with open("text_files/config_override.json") as json_obj:
                modify_config_data = json.load(json_obj)
                if passed_modify_config in modify_config_data:
                    save_input = input("Would you like to save this change? Type S to save or D for discard.")
                    save_config(save_input,passed_modify_config,passed_modify_info)
                else:
                    print("You did not enter a piece of data that is in the file. ")
        else:
            with open("text_files/basic_config.json") as json_obj:
                modify_config_data = json.load(json_obj)
                if passed_modify_config in modify_config_data:
                    save_input = input("Would you like to save this change? Type S to save or D for discard.")
                    save_config(save_input,passed_modify_config,passed_modify_info)
                else:
                    print("You did not enter a piece of data that is in the file. ")

"""This segment involves classes that will delete config options"""

def delete_config(passed_delete_input):
    """processes save input that is passed to it, then deletes data if save option is accepted, discard will pass through the function and will change nothing
    Arguments:
        passed_input,passed_key
    returns:
        nothing
    """
    if passed_delete_input:
        if os.path.isfile("text_files/config_override.json"):
            with open("text_files/config_override.json") as json_obj:
                delete_config_data = json.load(json_obj)
            with open("text_files/basic_config.json") as json_obj:
                delete_basic_config_data = json.load(json_obj)
                if passed_delete_input not in delete_basic_config_data and passed_delete_input in delete_config_data:
                    save_input = input("Would you like to save this change? Type S to save or D for discard.")
                    delete_save_config(save_input,passed_delete_input)
                else:
                    print("You can not delete anything that is also in the basic config file. ")
        else:
            print("You can not delete anything from the basic config file.")
    else:
        print("You didn't type anything.")

def delete_save_config(passed_input, passed_key):
    """processes save input that is passed to it, then deletes data if save option is accepted, discard will pass through the function and will change nothing
    Arguments:
        passed_input,passed_key
    returns:
        new file version of config_override if save is accepted, nothing if discarded
    """
    if passed_input == "S":
        if os.path.isfile("text_files/config_override.json"):
            shutil.copy2("text_files/config_override.json", "text_files/config_override.json.backup" + str(time.time()))
            with open("text_files/config_override.json") as json_obj:
                delete_config_data = json.load(json_obj)
                delete_config_data.pop(passed_key)
            with open("text_files/config_override.json","w") as json_obj:
                json.dump(delete_config_data, json_obj)
        else:
            print("Modify the file before attempting to delete a config option.")
    elif passed_input == "D":
        pass