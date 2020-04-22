#!python3
from math import floor,ceil,sqrt

#format print
print("test1\ntest2")
#string
name="Thomas"
print("There a man mamed "+name+",")
print(name.lower())
print(name.upper().islower()) #upper and lower functions
print(len(name)) #length
print(name[0]) #string as a char array
print(name.index("a"))
print(name.replace("Thomas","Laughing"))
#number
interger=1
floatnumber=2.40
negative=-3
print(interger+floatnumber+negative) #0.3999999999999999
print(12%5)
print(str(interger) + " my number")
print(abs(negative)) #absolute value
print(pow(3,300)) #number and power
print(max(1,43) + min(1,43))
print(floor(3.3))
print(ceil(363.2236235))
print(sqrt(pow(3,2)))
#get input
user=input("Enter your name: ")
print("hi " + user + "!")