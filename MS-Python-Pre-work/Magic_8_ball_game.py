from random import randint

question = str(input('What is your question? '))

random_number = randint(1, 3)

if random_number == 1:
    random_number = randint(1, 10)
    if random_number == 1:
        print('It is certain.')
    elif random_number == 2:
        print('It is decidedly so.')
    elif random_number == 3:
        print('Without a doubt')
    elif random_number == 4:
        print('Yes - definitely.')
    elif random_number == 5:
        print('You may rely on it.')
    elif random_number == 6:
        print('As I see it, yes.')
    elif random_number == 7:
        print('Most likely.')
    elif random_number == 8:
        print('Outlook good.')
    elif random_number == 9:
        print('Yes')
    elif random_number == 10:
        print('Signs point to yes.')
elif random_number == 2:
    random_number = randint(1, 5)
    if random_number == 1:
        print('Reply hazy, try again.')
    elif random_number == 2:
        print('Ask again later.')
    elif random_number == 3:
        print('Better not tell you know.')
    elif random_number == 4:
        print('Cannot predict now.')
    elif random_number == 5:
        print('Concentrate and ask again.')
elif random_number == 3:
    random_number == randint(1, 5)
    if random_number == 1:
        print('Don\'t count on it.')
    if random_number == 2:
        print('My reply is no.')
    if random_number == 3:
        print('My sources say no.')
    if random_number == 4:
        print('Outlook not so good.')
    if random_number == 5:
        print('Very doubtful.')

