import pandas as pd
import csv
import logging as log

# data = pd.read_csv("C:\\\\Users\\shreyansh.sharan\\Desktop\\GitHub\\Raw_Data\\total_requested_stocks.csv", delimiter= ',')
# data = data.values.tolist()
# print(data[1])

read_obj = open("C:\\\\Users\\shreyansh.sharan\\Desktop\\GitHub\\Backend\\Raw_Data\\total_requested_stocks.csv") 

csv_reader = csv.reader(read_obj)
list_of_csv = list(csv_reader)[0]

print(list_of_csv)

def data_load_selection(user_list):
    print("Hey! Proceeding with the extraction")
    for i in user_list:
        if i in list_of_csv:
            print("Hellos")
            pass
        else:
            print(list_of_csv)
            list_of_csv.append(i)
            #finance_full_load(i)
            print(list_of_csv)
            with open('C:\\\\Users\\shreyansh.sharan\\Desktop\\GitHub\\Backend\\Raw_Data\\total_requested_stocks.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(list_of_csv)
            pass
            return "failed"

# print(data_load_selection())


