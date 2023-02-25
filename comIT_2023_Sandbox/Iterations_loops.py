# Let's make an algorithm that sums the first "N" even numbers. 

algortihm sum_n_event_numbers

    var Number: number, counter, sum, n 
    
    input(n)                # 2 
    number = 0              # 2
    sum = 0                 # 2
    even_counter = 0        # 1

    while even_counter < n : 
        number = number + 2
        even_counter = even+counter + 1  
        sum = sum + number               
        
    end while

    print("The sum of the first " + n + " event numbers was: " + sum)

end algorithm 



Assume N is 5



# 1 2 3 4 5 -> two even numbers
# 1 2 3 4 5 6 7 8 9 10 11 12 -> 5 even numbers
#         2 4 6 8 10 -> sum 30 (5 even numbers)




