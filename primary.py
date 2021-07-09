# author: <name here>
# date: <date here>

# -------------------- Section 1 -------------------- #

# Input | Saving String Responses to Variables

# Objectives:
#   1. Name in Reverse
#       a. Prompts input from the user in the form of a first name and last name.
#           Save these values to variables first_name and last_name.
#       b. Print the first and last names in reverse order.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> first name... elia
#   >> last name... deppe
#   deppe, elia
#
# ---- WRITE CODE BELOW ---- #
first_name = input('first name...')
last_name = input('last name...')

print(last_name, ', ', first_name)

#   2. Pyramid
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#   $
#   $$
#   $$$
#   $$
#   $
#
# ---- WRITE CODE BELOW ---- #
print()
symbol = input('Enter a symbol: ')
print(symbol)
print(symbol * 2)
print(symbol * 3)
print(symbol * 2)
print(symbol)

#   3. Parallelogram
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> @
#
#   @
#   @@
#   @@@
#   @@@@
#    @@@
#     @@
#      @
#
# ---- WRITE CODE BELOW ---- #
print()
symbol = input('Enter a symbol: ')
print(symbol)
print(symbol * 2)
print(symbol * 3)
print(symbol * 4)
print(' ' + symbol * 3)
print(' ' * 2 + symbol * 2)
print(' ' * 3 + symbol)

# -------------------- Section 2 -------------------- #

# Casting | Getting Integers and Floats from the User

# Objectives:
#   1. Comparison
#       a. Prompt the user to enter a number, and save it to a variable named num1. DO NOT CAST IT.
#       b. Prompt the user to enter a number, and save it to a variable named num2. CAST IT TO AN INTEGER.
#       c. Prompt the user to enter a number, and save it to a variable named num3. CAST IT TO A FLOAT.
#       d. Print out each variable multiplied by 10.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> num1... 45
#   >> num2... -132.45
#   >> num3... 2132.24
#
#   num1 (str)   | 45454545454545454545
#   num2 (int)   | -1320
#   num3 (float) | 21322.4
#
# ---- WRITE CODE BELOW ---- #
print()
num1 = input('Enter a number: ')
num2 = int(input('Enter a number: '))
num3 = float(input('Enter a number: '))

print(num1 * 10)
print(num2 * 10)
print(num3 * 10)

# Objectives:
#   2. Diameter of a Circle
#       a. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       b. Compute the diameter, and print it to the user.
#           diameter = radius * 2
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 12.3
#
#   diameter = 24.6
#
# ---- WRITE CODE BELOW ---- #
print()
radius = int(input('Enter a radius: '))
diameter = radius * 2

print(diameter)

# Objectives:
#   3. Area of a Circle
#       a. Define a function named area_circle(). Accept the parameters listed below.
#           Name   | Type(s)         | Description
#           radius | Integer / Float | The radius of the circle.
#
#           The function should compute the area of a circle, and print it to the terminal.
#               area = 3.14 * radius ** 2
#       b. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       c. Compute the radius by calling the function area_circle(), sending num as a parameter.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 44.2
#
#   area of the circle: 6134.4296
#
# ---- WRITE CODE BELOW ---- #
print()


def area_circle(radius):
    area = 3.14 * radius ** 2
    return area


num = int(input('Enter a radius: '))
print(area_circle(num))

# -------------------- Section 4 -------------------- #
#
# Create a conversation with a faux (fake) AI, using input and print().
# See the example in example.py
print()
name = input('Hello, what\'s your name?: ')
print(name, 'what a lovely name. My name is Nani.')

numberFav = int(input('Enter your favorite number: '))
numberLeast = int(input('Enter your least favorite number: '))

print('With the power of addition, the combination of the two numbers are', numberFav + numberLeast)

floatNumber = float(input('Any favorite decimal number?: '))
print('What a coincidence, my favorite number is also', floatNumber)

feeling = input('How are you liking this so far?: ')

print('Okay, I know it\'s short but I\'m running out time and ideas.')
print('Goodbye :D')
