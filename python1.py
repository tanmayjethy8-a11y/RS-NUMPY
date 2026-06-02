a= float(input("Enter first number: "))
b=float(input("Enter second number: "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Addition:", a + b)
elif choice == 2:
    print("Subtraction:", a - b)
elif choice == 3:
    print("Multiplication:", a* b)
elif choice == 4:
    print("Division:", a / b)
elif choice == 5:
    print("Modulus:",a%b)
else:
    print("Choice not available!!")