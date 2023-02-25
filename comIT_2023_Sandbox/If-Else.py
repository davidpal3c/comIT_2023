def compare_numbers():

    print("Please enter the first number: ")
    number_1 = input()						

    print("Please enter the second number")
    number_2 = input()	

    number_1 = float(number_1)
    number_2 = float(number_2)

    if number_1 > number_2:
        print(str(number_1) + " was the largest")
    elif number_2 > number_1:
        print(str(number_2) + " was the largest")
    else: 
        print("The numbers are equal")    	

compare_numbers()