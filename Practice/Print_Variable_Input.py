# Name and Age
'''

name = input("Enter your name:")
age = input("What is your Age?")

print(f"Hello {name}! You are {age} years old.")

'''

# Name and Age Calender


'''
print("Your Age calendar")

name = input("what is full name?")
birth_year = int(input("what is your birth year?"))
current_year = 2026
calculated_age = current_year - birth_year

print(f"{name}, Your age is {calculated_age} in 2026. Congrats!")

'''
# Global Variable

"""
global x
x = 3
def myfunc():
    x = 3
    global y 
    y = 45
    print("this is global variable", y)

print('out side func', x)
print('global', y)
#myfunc()

"""
# Age in 10 Years, 5 years ago

"""
print("Your Age calendar")

name = input("what is name?")
birth_year = int(input("what is your birth year?"))
current_year = 2026
present_age = current_year - birth_year
age_in_10years = present_age + 10
age__5years_ago = present_age - 5


print(f"{name}, You are currently {present_age} years old")
print(f"In 10 years, you will be {age_in_10years} years old.")
print(f"5 years ago, you were {age__5years_ago} years old.")

"""

# Even or Odd Checker (Introducing Logic)

"""
number = int(input('Please enter a number  '))

if number % 2 == 0:
    print(f'The number {number} is Even')
else:
    print(f'The number {number} is Odd.')

"""


# Challenge: Positive, Negative, or Zero

'''

number = float(input("Please enter a number \nto find out Positive, Negative, or Zero "))

if number > 0:
    result = "Positive"
elif number < 0:
    result = "Negative"
else:
    result = "Zero"

print(f"Your number {number} is {result}")

'''

# Grade Evaluator

"""
number = float(input("Please enter your score between 0-100...."))


if  (number >100 or number <0):       #Cheecking Invalid Number
    result = "None"
    
elif  number >= 90:
    result = "A"

elif  number >= 80:
    result = "B"

elif  number >= 70:
    result = "C"

elif  number >= 60:
    result = "D"
    
else:
    result = "F"
    

if result == "None":
    print("Invalid score...")
else:
    print(f"Your score is {number} and the Grade is {result}!")

"""
