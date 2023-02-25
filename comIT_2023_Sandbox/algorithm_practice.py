# Let's develop an algorithm that requests the input of two
# numbers and calculate its product.

def calculate_product():

    print("Please enter the first number: ")
    number_1 = input()

    print("Please enter the second number: ")
    number_2 = input()

    number_1 = float(number_1)
    number_2 = float(number_2)

    product = number_1 / number_2
    
    print("The product of " + str(number_1) + " and " + str(number_2) + " was " + str(product))

calculate_product()







