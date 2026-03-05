'''
This program is used to find the sum of natural numbers with the interval
'''
limit=int(input("Enter the limit:"))
sum=0
for i in range(1,limit+1):
    sum+=i

print(f"The sum of natural numbers of the limit {limit} is {sum}")