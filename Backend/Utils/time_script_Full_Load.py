from datetime import date
import datetime
def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))
    


d = date(2023,9,8)  
start_date = (add_years(d,-5))
print(start_date)
# start_date = datetime.strptime(start_date, "%m-%d-%y")

base_date = start_date
end_date = date(2023,9,1)

listday = []
Day1 = start_date
# print(Day1,d)
def date_binning (start_date,Day1):
    while start_date < d:
        
        Day7 = Day1 + datetime.timedelta(days=7)

        listday.append([Day1,Day7])
        # print(listday)
        Day1 = Day7

        start_date = Day7
    return listday

test =  date_binning(start_date,Day1)    
print(listday)

print(test[-1][1] > d)
diff = test[-1][1] - d
print(diff, type(diff), test[-1][1] - datetime.timedelta(days = diff.days) )
# print(test)