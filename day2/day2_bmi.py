#this code will calculate your BMI

#Question
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
int_height = float(height) #get Float value for height
int_weight = int(weight) #get int value for weight

bmi = int_weight / (int_height*int_height) #bmi = weight/(height*height)

print(int(bmi)) # finally convert float value to int value