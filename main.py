from my_math import power

print("Greetings human")
print("This application calculates power of inputted number")

x = int(input("Enter a number: "))
n = int(input("Enter power: "))
p = power(x, n)
print("Square of the number is: " + str(p))
