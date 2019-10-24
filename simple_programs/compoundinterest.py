# Python3 program to find compound interest for given values. 
"""
def compound_interest(principle, rate, time): 

	# Calculates compound interest 
	CI = principle * (pow((1 + rate / 100), time)) 
	print("Compound interest is", CI) 

# Driver Code 
compound_interest(10000, 10.25, 5) 

"""


"""
# Python program to find compound interest 

p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))

# calculating compound interest
ci =  p * (pow((1 + r / 100), t)) 

# printing the values
print("Principle amount  : ", p)
print("Interest rate     : ", r)
print("Time in years     : ", t)
print("compound Interest : ", ci)

"""


"""
def compound_interest(principle, rate, time):

    result = principle * (pow((1 + rate / 100), time))
    return result
 
 
p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))
t = float(input("Enter the time in years: "))
 
amount = compound_interest(p, r, t)
interest = amount - p
print("Compound amount is %.2f" % amount)
print("Compound interest is %.2f" % interest)

"""

"""
# User must input principal, Compound rate, annual rate, and years.
P = int(input("Enter starting principle please: "))
n = int(input("Enter Compound intrest rate :(daily, monthly, quarterly, half-year, yearly) "))
r = float(input("Enter annual interest amount : (decimal) "))
t = int(input("Enter the amount of years : "))

final = P * (((1 + (r/n)) ** (n*t)))
#displays the final amount after number of years.
print ("The final amount after", t, "years is", final)

"""

import math

princ_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_int = float(input(" Please Enter the Rate Of Interest   : "))
time_period = float(input(" Please Enter Time period in Years   : "))

ci_future = princ_amount * (math.pow((1 + rate_of_int / 100), time_period)) 
compound_interest = ci_future - princ_amount

print("Future Compound Interest for Principal Amount {0} = {1}".format(princ_amount, ci_future))
print("Compound Interest for Principal Amount {0} = {1}".format(princ_amount, compound_interest))



