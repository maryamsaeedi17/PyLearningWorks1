w=float(input("Please enter your weight(kg):"))
h=float(input("Please enter your height(m):"))

bmi=w/h**2

if bmi<18.5:
    print("Your BMI is:", bmi, "Your Status: Under weight")
elif bmi>=18.5 and bmi<25:
    print("Your BMI is:", bmi, "Your Status: Normal weight")
elif bmi>=25 and bmi<30:
    print("Your BMI is:", bmi, "Your Status: Over weight")
elif bmi>=30 and bmi<35:
    print("Your BMI is:", bmi, "Your Status: Obesity")
elif bmi>=35 and bmi<40:
    print("Your BMI is:", bmi, "Your Status: Extreme obesity")   
else:
    print("Your BMI is:", bmi, "Maybe your data is False!")
