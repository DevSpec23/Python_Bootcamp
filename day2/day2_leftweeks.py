age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

int_age = int(age) #convert input to int value

n = 90 * 52 #calculate 90 years weeks

answer = n - (int_age*52) #Calculate weeks left

print("You have " + str(answer) + " weeks left.")

#using str for converting int value to string value