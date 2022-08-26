# 🚨 BMI CALCULATOR

my_height = input("\nEnter your height in m: ")

my_weight = input("\nEnter your weight in kg: ")

bmi = (float(my_weight) / float(my_height) ** 2)

print(round(bmi,2))

if bmi < 18.6:
    print("\nYou are Underweight. Go to the Doctor !\n\n")
elif bmi <= 24.9:
    print("\nYou're Healthy Weight. Good Job!\n\n")

elif bmi <= 29.9:
    print("You're Overweight, be careful. Do exercises\n\n")

elif bmi > 29.9:
    print("You're obesity. Go to the Doctor !\n\n")
