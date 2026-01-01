""" I've made this factorial program without using recursion and with very basic code with steps for better understanding"""

n = int(input("Enter Number for its Factorial: ")) # Asking a Number from user to do its Factorial 

fact=1    # Flag created to store factorial value

for i in range (n,0,-1):    # Descending Loop  
    if fact == 1:
        print("!",end='')
    else:
        print (fact,"x",i,"=", end=' ')    # Will print factorial steps
    fact *= i    
    print (fact)
print ("Factorial of",n,"=",fact)    # Printing the final result
