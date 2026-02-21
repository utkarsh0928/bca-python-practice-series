#This program is used to convert the km to miles
km=float(input("Enter the kilometers:"))
#conversion factor : 1KM =  0.621371 miles
conversion_factor=0.621371
miles=conversion_factor*km
print(f"{km} kilometers is equal to the {miles} miles.")