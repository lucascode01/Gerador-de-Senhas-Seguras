import random

print('welcome to yout password generator')


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKELMNOPQRSTUVWXYZ!@&^$%().,?0123456789'

number = input('Ammount of passwords to generate: \n')
number = int(number)


length = input('input your password length: \n')
length = int(length)

print('\n here are your passwords: ')

for pwd in range(number) :
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)    