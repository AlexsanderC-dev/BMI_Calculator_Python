# 🚨 BMI CALCULATOR


my_height = float(input("\nEnter your height in m: ")) # Use the " . " to separate the meter from the centimeter

my_weight = float(input("\nEnter your weight in kg: "))

bmi = round(my_weight / my_height ** 2)
if bmi < 18.5:
    print(f"\nYou are Underweight, your bmi is {bmi}. Go to the Doctor !\n\n")
elif bmi < 25:
    print(f"\nYou're Healthy Weight, your bmi is {bmi}.  Good Job!\n\n")
elif bmi < 30:
    print(f"\nYou're Overweight, your bmi is {bmi}, be careful. Do exercises\n\n")
elif bmi < 35:
    print(f"\nYou're obesity, your bmi is {bmi} Go to the Doctor !\n\n")
else:
    print(f"\nYou're clinically obese, your bmi is {bmi}. It's very important that you see a doctor  ")
