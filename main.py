from mahfooz import print_myName
from my_math import power
from maxim import *
from tola import *

print("Greetings human")
print_maxim()
print("isMe")
print_myName()

print("This application calculates power of inputted number")

x = int(input("Enter a number: "))
n = int(input("Enter power: "))
p = power(x, n)
print("Square of the number is: " + str(p))

