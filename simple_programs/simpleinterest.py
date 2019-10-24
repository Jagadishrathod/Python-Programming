# Python3 program to find simple interest for given principal amount, time and rate of interest.  
"""
P = 1
R = 1
T = 1

# Calculates simple interest 
SI = (P * R * T) / 100

# Print the resultant value of SI 
print("fgsimple interest is", SI)

"""


"""
P = int(input("Enter Principal amount of money to be invested : "))
R = int(input("Enter Rate of interest: "))
T = int(input("Enter Time period: "))

# Calculates simple interest 
SI = (int(P) * int(R) * int(T))/100

print("simple interest = ",SI)

"""

"""
P = float(input("Enter thfge principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
#2
SI = (P * N * R)/100
print("Simple interest : {}".format(SI))

"""


"""
p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in years: "))
r = float(input("Enter the interest rate: "))
 
SI = p * t * r / 100
 
print("Simple Interest = %.2f" %SI)"""

"""

# Python Program to Calculate Simple Interest

princ_amount = float(input("Enter the Principal Amount  : "))
rate_of_int = float(input("Enter the Rate Of Interest   : "))
time_period = float(input("Enter Time period in Years   : "))

SI = (princ_amount * rate_of_int * time_period) / 100

print("\nSimple Interest for Principal Amount {0} = {1}".format(princ_amount, SI))

"""


""""
def SI(p, n, r):
    SI = 0.0
    SI = float(p*n*r)/float(100);
    return SI;

if __name__ == '__main__':
    p = float(input("Enter values\np: "));
    n = int(input("n: "));
    r = float(input("r: "));
    SI = SI(p, n, r);
    print("Simple interest value: " + "{0:.2f}".format(SI));

"""



# Python program to find simple interest 

p = int(input("Enter the principle amount : "))
r = int(input("Enter the rate of interest : "))
t = int(input("Enter the time in the years: "))

# calculating simple interest
si = (p*r*t)/100

# printing the values
print("Principle amount: ", p)
print("Interest rate   : ", r)
print("Time in years   : ", t)
print("Simple Interest : ", si)
