from random import randint

question = str(input('What is your question? '))

yes = ['It is certain', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.', ' Most likely.', 'Most likely.', 'Outlook good.', 'Yes', 'Signs point to yes.']
maybe = ['Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.']
no = ['Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

random_number = randint(1, 3)

if random_number == 1:
    random_number = randint(1, 10)
    print(yes[random_number])
elif random_number == 2:
    random_number = randint(1, 5)
    print(maybe[random_number])
else:
    random_number = randint(1, 5)
    print(no[random_number])