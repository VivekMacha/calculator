
while(True):
    print()
    Print("Welcome To Calculator")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Division")
    print("4: Multiplication")
    print("5: Exit")
    print()

    op = input("Enter Your Choice-: ")
    if (op=="1"):
        x=int(input("enter 1st number:-"))
        y=int(input("enter 2nd number:-"))

        print(f"{x} + {y} = {x+y}")
    elif (op=="2"):
        x=int(input("enter 1st number:-"))
        y=int(input("enter 2nd number:-"))

        print(f"{x} - {y} = {x-y}")
     elif (op=="3"):
        x=int(input("enter 1st number:-"))
        y=int(input("enter 2nd number:-"))

        print(f"{x} / {y} = {x//y}")

    elif (op=="4"):
        x=int(input("enter 1st number:-"))
        y=int(input("enter 2nd number:-"))

        print(f"{x} * {y} = {x*y}")

   
    elif(op=="5"):
        break        
    else:
        print("invalid input")



