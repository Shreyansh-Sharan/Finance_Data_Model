import pandas as pd
import csv
# data = pd.read_csv("C:\\\\Users\\shreyansh.sharan\\Desktop\\GitHub\\Raw_Data\\total_requested_stocks.csv", delimiter= ',')
# data = data.values.tolist()
# print(data[1])

with open("C:\\\\Users\\shreyansh.sharan\\Desktop\\GitHub\\Raw_Data\\total_requested_stocks.csv", 'r') as read_obj:

    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)

print(list_of_csv[0])

def data_load_selection(user_list=['GOOGL','AMZN']):
    for i in user_list:
        if i in list_of_csv[0]:
            #data_load_selection(i)
            print("Hellos")
            pass
        else:
            #finance_full_load(i)
            pass



