# relational operators
# flow control

gender = input("enter 'm' for male, 'f' for female, 'o' for others:\n")
age = int(input("enter your age\n:"))

if age > 45 and age < 60:
    if gender == 'f':
        print("you get a 10% discount")
    else:
        print("you get a 5% discount")
elif age >= 60 and age < 75:
    if gender == 'f':
        print("you get a 15% discount")
    else:
        print("you get a 10% discount")
elif age >= 75:
    print("you get 18% discount")
else:
    print("you get 30% discount")


    
