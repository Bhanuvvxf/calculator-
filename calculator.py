print("Wellcome to the Basic Calculator!\n")

print("1.Addition","2.Subtraction","3.Multiplication","4.Division",sep="\n")

option = int(input("Enter your choice (1/2/3/4): "))

if option == 1 :
    a , b  = int(input("Enter the frist number : ")) , int(input("Enter the second number : "))
    c = a + b
    print(f"The result of {a} + {b} is {c}")
elif option == 2 :
    a , b  = int(input("Enter the frist number : ")) , int(input("Enter the second number : "))
    c = a - b
    print(f"The result of {a} + {b} is {c}")
elif option == 3 :
    a , b  = int(input("Enter the frist number : ")) , int(input("Enter the second number : "))
    c = a * b
    print(f"The result of {a} + {b} is {c}")
elif option == 4 :
    a , b  = int(input("Enter the frist number : ")) , int(input("Enter the second number : "))
    c = a / b
    print(f"The result of {a} + {b} is {c}")

else:
    print("option not valid")
    

