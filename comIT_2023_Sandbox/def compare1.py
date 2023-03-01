
def compare_values():
  
    x = int(input("Enter first number to compare: "))
    y = int(input("Enter second number to compare: "))

    if x > y:
      print(str(x) + " is a bigger than " + str(y))
    
    if x < y: 
      print(str(y) + " is a bigger than " + str(x))  

    if x == y:
        print("both numbers are equal")

compare_values

