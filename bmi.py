print("Welcome to PGRSpot BMI_Calcilator")
weight = float(input("Enter your weight in kg: \n"))
height = float(input("Enter your height in meter: \n"))
BMI = round((weight) / (height) ** 2, 2)
print(BMI)
if BMI < 18.5:
    print(f'Your BMI is, {BMI} and you are UNDERWEIGHT')
elif BMI < - 24.9:
    print(f'Your BMI is, {BMI} and you are Normal Weight')
elif BMI < - 29.9:
    print(f'Your BMI is, {BMI} and you are OVERWEIGHT')
else:
    print(f'Your BMI is, {BMI} and you are OBESITY')
    print("\nThanks for using PGRSpot BMI")
