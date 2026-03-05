"""
This program checks armstrong condition within the user defined interval
"""
#Input the intervals
lower=int(input("Enter the lower limit of the interval:"))
upper=int(input("Enter the upper limit of the interval:"))
#Iterating the numbers
for num in range(lower,upper+1):
    order=len(str(num)) #Finding the number of digits in 'num'
    temp_num=num
    sum=0

    while temp_num>0:
        digit=temp_num%10
        sum+=digit**order
        temp_num//=10
#Checking if 'num' is an Armstrong
    if sum==num:
        print(sum) 