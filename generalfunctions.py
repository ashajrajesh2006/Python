class genfunc():
    def subfields():
        a=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Subfields in AI are: ")
        for item in a:
            print(item)

    def oddeven():
        num=int(input("Enter the number: "))
        if((num%2)==1):
            print("Odd Number")
            message=("Odd Number")
        else:
            print("even number")
            message=("even number")
        return message

    def Eligible():    
        gender=input("Enter the gender: ")
        age=int(input("Enter the age: "))
        if(gender=="male"):
            if(age>=21):
                print("Eligible for marriage")
            else:
                print("not eligible to marry")
        else:
            if(age>=18):
                print("Eligible for marriage")
            else:
                print("not eligible to marry")
    def percentage():
        nam=input("Enter the name: ")
        sub1=int(input("Enter the Subject1 marks: "))
        sub2=int(input("Enter the Subject2 marks: "))
        sub3=int(input("Enter the Subject3 marks: "))
        sub4=int(input("Enter the Subject4marks: "))
        sub5=int(input("Enter the Subject5 marks: "))
        add= sub1+sub2+sub3+sub4+sub5
        print("Total",add)
        percentage=(add/5)
        print("Percentage is ",percentage)

    def triangle():
            a=float(input("Height: "))
            b=float(input("Breadth: "))
            Area=(a*b)/2
            print("Area of Triangle: ",Area)
            #perimeter of triangle
            a1=float(input("Height1: "))
            a2=float(input("Height2: "))
            b1=float(input("Breadth2: "))
            Perimeter=a1+a2+b1
            print("Perimeter of the Triangle",Perimeter)


