#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator!")

#get input for total bill
total = input("Enter your total bill $")
#convert string value to int value
intTotal = int(total)

#calculate total with tips for each person
eachBill = intTotal / 5 * 1.12

print(round(eachBill,2)) #print answer using round for display decimal places
