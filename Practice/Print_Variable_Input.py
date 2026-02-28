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

# Number Guessing (Intro to Loops)

"""
secret_number = 7
user_number = int(input("Guess the number?"))
count = 1

while user_number != secret_number:
    print("Wrong number")
    user_number = int(input("Guess the number?"))
    count += 1  #Counting the User attemps

print(f"You guessed the right number in {count} attempts")


"""
# Smart Guessing Game (Add Feedback)

"""

secret_number = 15
user_number = int(input("Guess the number: "))
count = 1
range = 10


while user_number != secret_number:
    if user_number > secret_number + range:
        print("Too high!")
    elif user_number < secret_number - range:
        print("Too low!")
    else:
        print("Wrong Number")
    user_number = int(input("Guess the number: "))
    count += 1  #Counting the User attempts

print(f"Correct! You guessed it in {count} attempts.")

"""


# Smart Receipt Formatter

"""
product_name = input("Product name: ")
quantity = int(input("Quantity: "))
price_per_unit = float(input("Price per unite: "))

sub_total = quantity * price_per_unit
tax = sub_total * 0.10
final_total = sub_total + tax

print(f"-------- RECEIPT --------")
print(f"Product : {product_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: {price_per_unit:.2f}")
print(f"Subtotal : {sub_total:.2f}")
print(f"Tax (10%): {tax:.2f}")
print(f"Total    : {final_total:.2f}")
print("------------------------")


"""

# Multi-Item Billing System



"""


total_items = int(input("How many items?"))
grand_total = 0
discount = 0

for i in range(1, total_items + 1):
    item_name = input(f"Item {i} name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    item_total = quantity * price
    grand_total += item_total



# Apply Discount If grand total ≥ 1000 → 15% discount If grand total ≥ 500 → 10% discount


if grand_total >= 1000:
    discount = grand_total * 0.15
elif grand_total >= 500:
    discount = grand_total * 0.10
else:
    discount = 0

after_discount_price = grand_total - discount
tax = after_discount_price * 0.10

final_total = after_discount_price + tax


print(f"-------- FINAL BILL --------")
print(f"Items Purchased: {total_items}")
print(f"Gross Total : {grand_total:.2f}")
print(f"Discount    : {discount:.2f}")
print(f"After Disc  : {after_discount_price:.2f}")
print(f"Tax (10%)   : {tax:.2f}")
print(f"Final Total : {final_total:.2f}")
print("-----------------------------")

"""

# Challenge — Input-Controlled Program (Loop Until Exit)

'''
count = 0
total = 0
highest = None
lowest = None  
i = 0 
average_num = 0
while  True:
    txt = input('Enter a number (or type "done"): ')
    if txt == "done":
        break
    user_input =  float(txt)
    if highest is None:       # set highest and lowest 
        highest = user_input
        lowest = user_input
    else:
        if user_input > highest:
            highest = user_input
        if user_input < lowest:
            lowest = user_input
    total  += user_input
    count  +=1 

if count == 0:
    print("No numbers were entered.")
else:
    average_num = total / count


print(f"-------- SUMMARY --------")
print(f"Numbers Entered: {count}")
print(f"Sum            : {total:.2f}")
print(f"Average        : {average_num:.2f}")
print(f"Highest        : {highest:.2f}")
print(f"Lowest         : {lowest:.2f}")
print(f"-------------------------")

'''

x = 25
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

max_value = x if x > y else y 