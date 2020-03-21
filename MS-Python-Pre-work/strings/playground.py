# raw strings
# we introduce the r before the string to ignore the escape character
# print(r'Beyonce\'s lemonade stand')

# string methods
# isalpha() - returns True if the string consists of letters only and is not blank
# isalnum() - returns True if the string consists of numbers and letters and is not blank
# isdecimal() - returns True if the string contains only numeric characters
# isspace() - returns True if the string contains only space,tabs or new lines
# istitle() - returns True if the string contains words that start with uppercase letters

# print out users name and age
name = str(input('What is your name? '))
age = int(input('What is your age? '))

print('Your name is {} and you are {} years old.'.format(name, age))