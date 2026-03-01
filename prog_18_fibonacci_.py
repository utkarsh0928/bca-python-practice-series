'''This program is used to display the fibonacci series of the number'''
num=int(input("Enter the number terms:"))
f1,f2=0,1
if (num<0):
    print("Please enter the positive number")
elif (num==1):
    print(f'Fibonacci Series upto terms {num}:')
    print(f1)
else:
    print("Fibonacci Sequence:")
    print(f1,f2,end=" ")
    for i in range(2,num):
        nth=f1+f2
        f1=f2
        f2=nth
        print(nth,end=" ")