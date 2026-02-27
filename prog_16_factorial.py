'''This program generates the factorial of the number'''
num=int(input("Enter the number:"))
fact=1
if (num==0 or num ==1):
    print(f"Factorial of the number {num}:{fact}")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f"Factorial of the number {num}:{fact}")