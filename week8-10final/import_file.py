import os.path
import shutil
import time

"""removes bad characters from customer_export.txt and then writes output to a new csv file"""
temp_output = ""
other_temp_output = ""
with open("week8-10final/text_files/customer_export.txt") as text_file:
    data = text_file.read()
    data = data.replace("#", "")
    data = data.replace("|", ", ")
    temp_output = temp_output + data
    if os.path.isfile("week8-10final/docs/customers.csv"):
        shutil.copy2("week8-10final/docs/customers.csv", "week8-10final/docs/customers.csv.backup" + str(time.time()))
    with open("week8-10final/docs/customers.csv", "w") as file_output:
        file_output.write(temp_output)

# """removes bad characters from customer_export.txt and then writes output to a new json file"""
# with open("week8-10final/text_files/customer_export.txt") as other_text_file:
#     data = other_text_file.read()
#     data = data.replace("#", "")
#     data = data.replace("|", ", ")
#     temp_output = temp_output + data
#     if os.path.isfile("week8-10final/docs/customers.json"):
#         shutil.copy2("week8-10final/docs/customers.json", "week8-10final/docs/customers.json.backup" + str(time.time()))
#     with open("week8-10final/docs/customers.json", "w") as file_output:
#         file_output.write(temp_output)


# if os.path.isfile("text_files/cleaned_data.txt"):
#     shutil.copy2("text_files/cleaned_data.txt", "text_files/cleaned_data.txt.backup" + str(time.time()))

#     with open("text_files/cleaned_data.txt", "w") as file_output:
#         file_output.write(temp_output)
