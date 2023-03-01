# Example 1: Count Even and Odd numbers from the given list using for 
#           loop Iterate each element in the list using for loop and 
#           check if num % 2 == 0, the condition to check even numbers. 
#           If the condition satisfies, then increase the even count else increase odd count. 

# Python program to count Even
# and Odd numbers in a List
 
# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 1]
 
even_count, odd_count = 0, 0
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
 
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)





