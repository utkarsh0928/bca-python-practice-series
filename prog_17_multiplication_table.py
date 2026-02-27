'''This program is used to generate the multiplication table of the number'''
num=int(input("Enter the number:"))
print(f"The multiplication table of the number {num}:")
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")