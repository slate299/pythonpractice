# Create a program that prints the largest of 3 numbers
x=int(input("input variable x: "))
y=int(input("input variable y: "))
z=int(input("input variable z: "))
if x > y and x > z:
    print(f"The largest number is {x}")
elif y > x and y > z:
    print(f"The largest number is {y}")
else:
    print(f"The largest number is {z}")