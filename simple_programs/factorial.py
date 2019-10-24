# Python 3 program to find factorial of given number 
"""def factorial(n): 
      
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  
# Driver Code 
num = 5; 
print("Factorial of",num,"is",factorial(num)) """





"""def factorial(num):
  
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


# We will find the factorial of this number
num = int(input("Enter a Number: "))

# if input number is negative then return an error message
# elif the input number is 0 then display 1 as output
# else calculate the factorial by calling the user defined function
if num < 0:
    print("Factorial cannot be found for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is: ", factorial(num))"""


# Python code to demonstrate naive method to compute factorial 
"""num = 5
fact = 1

for i in range(1,num+1): 
	fact = fact * i 
	
print ("The factorial of",num, "is : ",end="") 
print (fact) """




# Python code to demonstrate math.factorial() 
"""import math 
num = int(input("Enter a number :"))
print ("The factorial of",num," is : ", end="") 
print (math.factorial(num)) """

"""def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
num = int(input("Input a number to compute the factiorial : "))
print("The factorial of",num," = ",factorial(num))"""


"""num=int(input("Enter number:"))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print("Factorial of the number is: ")
print(fact)"""




num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       factorial = factorial*i  
   print("The factorial of",num,"is",factorial)  

