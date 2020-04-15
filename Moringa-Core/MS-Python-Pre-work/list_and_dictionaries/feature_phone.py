# This program counts the number clicks a user has to make to write a character in a feature phone
user_input = str(input('Enter the text: ').lower().strip())

text_input = ''
for character in user_input:
    if character.isalnum():
        text_input += character

keypad = {1: [], 2: ['a', 'b', 'c']}

print(user_input)