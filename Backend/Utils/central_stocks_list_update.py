import json
file = open('C:\\\\Users\\shreyansh.sharan\\Desktop\\GitHub\\Raw_Data\\stocks_metadata.json')
Total_Stocks = []
data = json.load(file)
for (k,userdetails)in data.items():
    for i in userdetails:
        # print(i['stocks_requested'])
        Total_Stocks.extend(i['stocks_requested'])
file.close()

print(Total_Stocks)

import csv

# Step 3: Opening a CSV file in write mode

with open('C:\\\\Users\\shreyansh.sharan\\Desktop\\GitHub\\Raw_Data\\total_requested_stocks.csv', 'w', newline='') as file:
    # Step 4: Using csv.writer to write the list to the CSV file
    writer = csv.writer(file)
    writer.writerow(Total_Stocks) # Use writerow for single list

