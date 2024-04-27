print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
oneName = name1 + name2
lowerOneName = oneName.lower()

t = lowerOneName.count("t")
r = lowerOneName.count("r")
u = lowerOneName.count("u")
e = lowerOneName.count("e")

true = t+r+u+e

l = lowerOneName.count("l")
o = lowerOneName.count("o")
v = lowerOneName.count("v")
e = lowerOneName.count("e")

love = l+o+v+e

loveScore = int(str(true)+str(love))

if (loveScore < 10) or (loveScore > 90):
  print("Your score is " + str(loveScore) + ", you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
 #I have failed when I submit the code because I used 'OR'.
 #Correct answer is 'AND'
 print("Your score is " + str(loveScore) + ", you are alright together.")
else:
  print("Your score is " + str(loveScore) + ".")