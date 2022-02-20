#hw 2.1
print("Programming", "Essentials", "in", sep="***", end="...")
print ("Python", sep="...", end="\n")
print()

#hw 2.2(a)
print("     ", end="*\n")
print("    ", " ", sep="*", end="*\n")
print("   ", "   ", sep="*", end="*\n")
print("  ", "     ", sep="*", end="*\n")
print(" ", "   ", sep="***", end="***\n")
print("   ", "   ", sep="*", end="*\n")
print("   ", "   ", sep="*", end="*\n")
print("   ", end="*****\n")

#hw 2.2(b)
print(" "*12, end="*\n")
print(" "*10, " "*3, sep="*", end="*\n")
print(" "*8, " "*7, sep="*", end="*\n")
print(" "*6, " "*11, sep="*", end="*\n")
print(" "*4, " "*6, sep="* "*3, end="* * *\n")
for i in range(2):
    print(" "*8, " "*7, sep="*", end="*\n")
print(" "*8, " "*4, sep="* "*5, end="\n")

#hw 2.2(c)
print("     ", "     "*2, " ", sep="*")
print("    ", " ","    "*2, " ", sep="*", end="*\n")
print("   ", "   ", "   "*2, "   ", sep="*", end="*\n")
print("  ", "     ", "  "*2, "     ", sep="*", end="*\n")
print(" ", "   ", " "*2, "   ", sep="***", end="***\n")
print("   ", "   ", "   "*2, "   ", sep="*", end="*\n")
print("   ", "   ", "   "*2, "   ", sep="*", end="*\n")
print("   ", "   "*2, " ", sep="*****")
print()

#hw 2.3
str='''"I'm" \n""learning"" \n"""Python"""'''
print(str)
print()

#hw 2.4
john = 2
mary = 3
adam = 4
print("john", "mary", "adam", sep=", ")
total_apples = john + mary + adam
print(total_apples)
print(mary*adam + john%mary)
print("Total number of apples:", total_apples)
print()

#hw 2.5
kilometers = 12.25
miles = 7.38
print(miles, "is", round(miles*1.61), "kilometers")
print(kilometers, "is", round(kilometers/1.61), "miles")
print()

#hw 2.6
x = float(0)
y = 3*x**3 - 2*x**2 + 3*x - 1
print(y)
x = float(1)
y = 3*x**3 - 2*x**2 + 3*x - 1
print(y)
x = float(-1)
y = 3*x**3 - 2*x**2 + 3*x - 1
print(y)
print()

#hw 2.7
a = 2
seconds = 3600
print("Hours: ",  a)
print("Seconds in Hours: ", a * seconds)
print("Goodbye")
print("Seconds in 3 Hours: ", 3 * seconds)
print("Enter your name:", end=" ")
x = input()
print("Hello, " + x)
print()

#hw 2.8
x = int(input("Введите число: "))
y = int(input("Введите второе число: "))
print(x + y)

#hw 2.9
x = float(input("Введите число: "))
y = (1 / (x+ (1 / (x + 1 / (x + 1/ x)))))
print(y)
print()

#hw 2.10
print("Hello world!")
print()

#hw 2.11
x = 11111
y = 1111111
print(x * y)
print()

#hw 2.12
x = 42 / (4 + 2 * (-1))
#-2 заменил на -1, иначе останавливается
print(x)
print()

#hw 2.13
print(2014 ** 14)
print()

#hw 2.14
seconds = 3600
hours = 24
days = 30
print(seconds * hours * days)
print()

#hw 2.15
x = float(2014)
print(x ** 14)
print(2014)
