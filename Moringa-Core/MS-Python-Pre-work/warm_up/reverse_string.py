'''
This program reverses every string you input.
'''

# user_input = str(input('Write the string you want reversed: ').strip())
user_input = 'nakolah'

print(user_input[-1:])

string_list = []

while True:
    i = 1
    if i < len(user_input)+1:
        string_list.append(user_input[-i])
        i += 1
    else:
        break
print(string_list)