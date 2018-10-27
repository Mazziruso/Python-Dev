# import cmath
# num = 16
# num_sqrt = cmath.sqrt(num)
# #print(type(num_sqrt.real))
# print('the value of num is %d but the real value of num_sqrt is %f' % (num, num_sqrt.real))
# seat1 = 13.50
# seat2 = 12.00
# seat3 = 14.64
# seat4 = 22.70
# seat5 = 16.73
# app = 9.99
# total = (seat1 + seat2 + seat3 + seat4 + seat5 + app)
# total = total + total * 0.05
# print('the total bill is %f' % total)
# price = 10
# cut_price = price * 0.3
# tax = (price - cut_price) * 0.05
# fee = 7.50
# total = price - cut_price + tax + fee
# # print('the total price is %f' % total)

# if total > 10:
# 	print(total)

# name = 'Doug'
# if name == 'Doug':
# 	print(name)
# print('How are you today?')

# a = 1
# try:
# 	a = 5 / 1
# 	printf(a)
# except NameError:
# 	# print('Please donot do that')
# 	pass
# print('a is %d' % a)

# total = 19 + 9.99 + 13.97 + 20 + 15.97 + 9.97 + 10 * 2
# party = 8

# print('Receipt for your meal')

# if party >= 8 :
# 	total = total + total * 0.2
# 	print('we have added the tip automatically, since your party is eight or larger')

# print('Total: %d' % total)
# print('Thank you for dining with us today')

# a = -10

# try:
#     if a > 0 :
#         print('you have money')
#     elif a == 0 :
#         print('you are out')
#     else:
#         print('you seem to be in debt')
# except NameError:
#     print('your spell is wrong!')

# a = 7
# title = 'Apple: '
# print(title,end = '')
# print(' $ 1.99 / 1b')
# title_len = len(title)
# print("the title's length is %d" % title_len)
# name = 'the instructor tell us that we should learn the Python carefully'
# name1 = name.capitalize()
# name2 = name.upper()
# name3 = name2.lower()
# name4 = name.title()
# print(name)
# print(name1)
# print(name2)
# print(name3)
# print(name4)
# print(len(name))
# print(name.isdigit())
# print(name.isalpha())
# print(title * a)

# rythm = 'Little Miss Mu\
# ffett\nSat on a\
# tuffet'
# print(rythm)

# header = 'Dish\tPrice\tType'
# print(header)

# first_name = 'Zheng   '
# last_name = 'eeeeeKuneeeee'
# print(first_name + ' ' +last_name)

# first_name = first_name.strip()
# last_name = last_name.strip('e')
# print(first_name + ' ' + last_name)

# email = 'this email is very urgent and is emergency email'
# if email.count('joke'):
#     print('Do you want to set this email as non-urgent?')
# elif email.count('emergency'):
#     print('Do you want to make this email urgent?')
# else:
#     print('You hava a general email!')

# for x in range(1,11):
#     print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
#     print(repr(x*x*x).rjust(4))
# print('this is end'.capitalize())

# age = '20'
# name = 'Zheng Kun'
# country = 'China'
# nationality = 'Chinese'
# education = 'Bachelor'
# university = 'Hangzhou Dianzi university'

# s1 = '{0} is my name,{1} years old and come from {2}'
# s2 = 'I am a {0}, and I just graduate form {1}, now I am a {2}'

# print(s1.format(name,age,country))
# print(s2.format(nationality,university,education))

# print('{0:.04f}'.format(1.0/7)); print('{0:-^25}'.format('world'))
# print('{name1} wrote {book}'.format(name1='Swaroop',book='A Byte of Python'))

# number = 23

# guess = eval(input('Please enter an interger: '))

# if guess == number :
#     print('Congratulations, you guess it.')
#     print('(But you do not have any prizes!)')
# elif guess >= number :
#     print('No, it is a little higher than it')
# else :
#     print('No, it is a little lower than it')

# print('Dones!')

# number = 23

# running = True

# while running :

#     guess = eval(input('Please enter an integer: '))

#     if guess == number :
#         print('Congratulation, you guess it.')
#         print('(But you do not win any prizes!)')
#         running = False
#     elif guess > number :
#         print('No, it is a little higher than it.')
#     elif guess <= 5 :
#         break
#     else :
#         print('No, it is a little lower than it.')

# else :
#     print('Loop is over here! Having your fun in the next games.')
#     # break

# print('Dones!')

# for i in range(1,101,9):
#     if i%7 == 0:
#         print(i,'could be divided by {0:.01f}'.format(i))
#         break
#     print('the value is',i)

# else :
#     print('Loop is over here')

# print('Done!')

# while True :

#     state = input('Please enter a statement here: ')

#     if state == 'quit' :
#         break

#     print('the length of the statement you input is',len(state))

# else :
#     print('Just over!')

# print('Dones!')

# while True :

#     s = input('Enter somthing here now: ')

#     if s == 'quit' :
#         break
#         print('you input is quit')
#     elif len(s) <= 3 :
#         continue
#         print('your input is lower than three word')

#     print('Input is of sufficient length')

# else :
#     print('Loop is over now')

# print('Dones!')

def Statement_input() :
    #函数块开始
    while True :

        s = input('Enter something here now: ')

        if s.lower() == 'quit' :
            break
        elif len(s) <= 3 :
            print('your input is lower than 3 words')
            continue

        print('Input is of sufficient length')

        print('Your input statement is', s.title())

    else :
        print('Loop is over now!')

    print('Dones!')
#函数块结束

def sort_input(arg):

    for i in range(0,len(arg)) :
        for j in range(i,len(arg)) :
            if arg[j] > arg[i] :
                temp = arg[i]
                arg[i] = arg[j]
                arg[j] = temp

    for k in range(0,len(arg)):
        print(arg[k],end=' ')

    print(end='\n')



# Statement_input()
while True :
    data = list(input('Please enter a list here: '))

    if data == ['q','u','i','t'] :
        print('you are quit now')
        break
    elif data == [] :
        print('Please reenter a new data list due to NULL of you input')
        continue

    sort_input(data)

print('Done!')
