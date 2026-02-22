'''
This program is used to display the calender based on user input year and month
'''
import calendar
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
print(calendar.month(year,month))