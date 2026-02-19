class multiplefunctions():
    def oddeven():
        num=int(input("Enter the number: "))
        if ((num%2) ==1):
            print("Odd Number")
            message=("Odd Number")
        else:
            print("Even Number")
            message=("Even Number")
        return message
    def BMI():
        BMI =float(input("Enter the BMI: "))
        if(BMI<18.5):
            print(f"Underweight")
            BodyMass=("Underweight")
        elif(BMI<24.9):
            print(f"Idealweight")
            BodyMass=("Idealweight")
        elif(BMI<34.9):
            print(f"Overweight") 
            BodyMass=("Overweight")
        else:
            print(f"Obese")
            BodyMass=("Obese")
        return BodyMass