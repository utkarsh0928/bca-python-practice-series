'''
This program is used to find the LCM of two numbers.
'''

def lcm_find(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))

print(f'The L.C.M. of {num1} and {num2} is {lcm_find(num1,num2)}.')