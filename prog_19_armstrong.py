'''
This program is used to check the armstrong condition for the number
'''
num=int(input("Enter the number:"))

#finding number of digits
num_str=str(num)
digits_num=len(num_str)

#varibles
sum_of_powers=0
temp_num=num

while temp_num>0:
    digit=temp_num%10
    sum_of_powers+=digit**digits_num
    temp_num//=10

if sum_of_powers == num:
    print("It was a armstrong number")
else:
    print("It was not a armstrong number")