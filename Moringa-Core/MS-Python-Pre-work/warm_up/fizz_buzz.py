'''
This is a program that prints integers from 1 to 100 but if a number is a mutiple of 3 it prints fizz and if it's a multiple of 5 it prints fuzz in place of the number, if the number is a multiple of both five and three the program prints fizzbuzz
'''

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print('fizzbuzz')
    elif i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print('buzz')
    else:
        print(i)