# Let's make an algorithm that sums the first "N" even numbers. 
def sum_n_even_numbers():
# take text input from user and convert into integer
    n = int(input("Enter the number of even numbers to sum: \n"))       # '\n'  or '\t'  o excape character telling to enter a new line/ or tab space (wihtout modifiying code text when pressing enter for example)
    sum = 0
    even_counter = 0

    while even_counter < n:
        even_counter = even_counter + 1  
        sum = sum + (even_counter * 2)           
# formated string: clear
    print(f"The sum of the first {n} even numbers was: {sum}")
# Instead of the usual concatenated conversion
#     print("The sum of the first " + n + " event numbers was: " + sum)
sum_n_even_numbers



