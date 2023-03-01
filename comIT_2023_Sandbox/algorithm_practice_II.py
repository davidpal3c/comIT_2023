# An algorithm to read a number by keyboard and say if it is positive or negative.

print("please enter a number ")
number_1 = input()

number_1 = float(number_1)

if number_1 > 0:
  print("The number is positive")

if number_1 < 0:
  print("The number is negative")

elif number_1 == 0:
  print("The number is 0")
