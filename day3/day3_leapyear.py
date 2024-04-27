# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year%4 == 0 and year%100 !=0:
  print("Leap year")
elif year%400 == 0:
  print("Leap year")
else:
  print("Not leap year")

#윤년 구하기
#4로 나누어 떨어지는 값이 0 일때 윤년
#100으로 나우어 떨어지는 값이 0이 아닐 때 윤년
#400으로 나누어 떨어지는 값이 0일 때 윤년