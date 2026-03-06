'''
This program is used to find the HCF of two numbers.
'''

def hcf_find(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x

    for i in range(1,smaller+1):
        if ((x%i==0) and (y%i==0)):
            hcf=i
    return hcf

num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))

print(f"The H.C.F. of {num1} and {num2} is {hcf_find(num1,num2)}")
