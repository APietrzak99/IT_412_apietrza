import os.path
import shutil
import time
import json
import csv
from classes.database_access import DB_Connect

my_db = DB_Connect('root','','python_projects')

def import_file():
    """removes bad characters from customer_export.txt and then writes output to a new csv file"""
    temp_output = ""
    with open("week8-10final/text_files/customer_export.txt") as text_file:
        data = text_file.read()
        data = data.replace("#", "")
        data = data.replace("|", ",")
        temp_output = temp_output + data
        with open("week8-10final/docs/customer_export.txt", "w") as file_output:
            file_output.write(temp_output)
        """csv backup area. will create backups if the file already exists """
        if os.path.isfile("week8-10final/docs/customers.csv"):
            shutil.copy2("week8-10final/docs/customers.csv", "week8-10final/docs/customers.csv.backup" + str(time.time()))
        with open("week8-10final/docs/customers.csv", "w") as file_output:
            file_output.write(temp_output)

    """reads customer_export.txt, and formats the data into a json format """
    with open('week8-10final/docs/customer_export.txt', 'r') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        data_list = list()
        for row in filereader:
            data_list.append(row)
    data = [dict(zip(data_list[0],row)) for row in data_list]
    data.pop(0)
    """json backup area. will create backups if the file already exists """
    if os.path.isfile("week8-10final/docs/customers.json"):
        shutil.copy2("week8-10final/docs/customers.json", "week8-10final/docs/customers.json.backup" + str(time.time()))
    with open("week8-10final/docs/customers.json", "w") as file_output:
        json.dump(data, file_output)

    """reads bad characters in customers.csv, and formats the data for use in sql insert statements """
    with open('week8-10final/docs/customers.csv', 'r') as csvfile:
        my_db.executeQuery("TRUNCATE TABLE crm_data;")
        my_db.executeQuery("TRUNCATE TABLE mailings;")
        csv_data = csv.reader(csvfile)
        next(csv_data)
        for row in csv_data:
            insert_crm_statement = ('INSERT INTO crm_data (f_name,l_name,company,address,city,state,zip,primary_phone,secondary_phone,email_address) VALUES (\"' + str(row[0]) + " \",\"" + str(row[1]) + "\" ,\" " + str(row[2]) + "\",\"" + str(row[3]) + " \",\"" + str(row[4]) + "\",\"" + str(row[6]) + "\",\"" + str(row[7]) + " \",\""+ str(row[8]) + "\",\"" + str(row[9]) + "\" ,\"" + str(row[10]) + "\");")
            insert_mailings_statement = ('INSERT INTO mailings(name,company,address) VALUES (\"' + str(row[0] + " " + row[1]) + "\" ,\" " + str(row[2]) + "\" ,\"" + str(row[3]) + "\");")
            my_db.executeQuery(insert_crm_statement)
            my_db.executeQuery(insert_mailings_statement)
        my_db.conn.commit()
    
    print("IMPORT COMPLETE")
        