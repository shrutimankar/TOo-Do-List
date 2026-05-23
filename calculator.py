def main():
    while True:
        print("\n calculator")
        print("1.add")
        print("2.subract")
        print("3.multiply")
        print("4.divide")

        choice = input("enter your choice(1-5):")

        if choice in ['1','2','3','4']:
            num1 = float(input("enter first number:"))
            num2 = float(input("enter second number:"))

            if choice == '1'
            print(f"the result is:{add(num1,num2)}")
            eilf choice == '2':
            print(f"the result is:{subract(num1,num2)}")
            eilf choice == '3':
            print(f"the result is;{multiply(num1,num2)}")
            eilf choice == '4'
            print(f"the result is:{divide(num1,num2)}")
            eilf choice == '5'
            print(f"exiting the calculator:")
            break
        else:
            print("invalid choice")

            if_name_=="_main_":
            main()