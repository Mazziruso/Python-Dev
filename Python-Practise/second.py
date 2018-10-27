# global x

# x = 50

# def func() :
# 	global x

# 	print('x is',x)
# 	x = 2
# 	print('Changed global x to',x)

# func()

# print('Value of x is',x)

# def func(a,b=1,c=100):
# 	print('a=',a,'b=',b,'c=',c)

# func(25,2)
# func(14,32,1)

# def total(a=0, *number, **phonebook):
# 	print('a',a)

# 	for i in number:
# 		print('single_item',i)

# 	for first_part, second_part in phonebook.items():
# 		print(first_part, second_part)

# total(10, 1, 2, 3, 4, Jack=1123, John=2231, Inge=1560, Mary=1209)

# def maxium(x,y):

# 	if x>y :
# 		return x
# 	elif x==y :
# 		return None
# 	else :
# 		return y


# a = int(input('Enter a: '))
# b = int(input('Enter b: '))

# print(maxium(a,b),end='\n')

# def print_max(x,y):
# 	'Prints the maxium of two numbers.打印两个数值中的最大数。'
# 	x = int(x)
# 	y = int(y)

# 	if x > y :
# 		print(x,'is maxium',end='\n')
# 	else :
# 		print(y,'is maxium\n')

# print_max(3,5)
# print(print_max.__doc__)

# import sys

# print('The command line arguments are: ')

# for i in sys.argv :
# 	print(i)

# print('\n\nThe PYTHONPATH is',sys.path,end='\n')

# import modu_test

# modu_test.say_hi()

# print('version is',modu_test.__version__)
# from modu_test import say_hi

# say_hi()

# print(type(list_a[3]))

# if __name__ == '__main__' :
# 	print('This program is being run by itself')
# else :
# 	print('I am being imported from another module')

# from modu_test import say_hi, __version__, list_a

# __version__ = 3.0

# say_hi()

# print('version is',__version__)#最终输出3.0，因为后来将__version__重赋值为3.0

# for ii in list_a :
# 	print(ii,end=' ')

# print(end='\n')

# from modu_test import *

# say_hi()

# print('the version is', __version__)#Error，因为该成员是双下划线开头

# for ii in list_a :
# 	print(ii,end=' ')

# print(end='\n')

# import modu_test

# print(dir(modu_test))

# shoplist = ['apple','peach','banana','carrot','mango']

# print('I have',len(shoplist),'items to purchase.')

# print('These items are:',end=' ')
# for item in shoplist :
# 	print(item,end=' ')

# print('\nI also have to buy rice.')
# shoplist.append('rice')
# print('My shopping list is now',shoplist)

# print('I will sort my list now')
# shoplist.sort();
# print('Sorted shopping list is', shoplist)

# print('The first item I will buy is', shoplist[0])
# olditem = shoplist[0]
# del shoplist[0]
# print('I bought the', olditem)
# print('My shopping list is now',shoplist)

# new_list = ['RedBull','noodle',shoplist]

# print('new list is', new_list)
# print('old list is', new_list[2])
# print('the last old list is', new_list[2][4])

# zoo = ('monkey','dog','cat','elephant','penguin','fox','tiger')
# print('Number of animals in the zoo is', len(zoo))

# new_zoo = 'camel','lion',zoo

# print('Number of cages in the zoo is', len(new_zoo))
# print('All animals in the new zoo are', new_zoo)
# print('Animals brought from old zoo are', new_zoo[2])
# print('Last animal brought from old zoo is', new_zoo[2][2])
# print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))

# print('the type of new_zoo is',type(new_zoo))
# print('the type of zoo is',type(zoo))
# print('all animals in the zoo is', zoo)

# shoplist = ['banana','apple','rice','carrot','mango']
# name = 'Zhengkun'

# print('Item 0 is',shoplist[0])
# print('Item 1 is',shoplist[1])
# print('Item 2 is',shoplist[2])
# print('Item 3 is',shoplist[3])
# print('Item 4 is',shoplist[4])
# print('Item -1 is',shoplist[-1])
# print('Item -2 is',shoplist[-2])
# print('Character 0 is',name[0])

# #slicing on a list
# print('Item 0~3 is',shoplist[0:3])
# print('Item 2 to end is',shoplist[2:])
# print('Item start to 4 is',shoplist[:4])
# print('Item 1 to -1 is',shoplist[1:-1])
# print('Item start to end is',shoplist[:])
# print('Character 1 to -2 is',name[1:-2])

# bri = set(shoplist)

# print('Is rice in bri?','rice' in bri)
# print('Is beef in bri?','beef' in bri)

# bric = bri.copy()
# bric.add('meat')
# print('Does bric embrace bri?',bric.issuperset(bri))
# bric.remove('apple')
# print('Does bric embrace bri?',bric.issuperset(bri))
# print('Intersections are',bric.intersection(bri))

shoplist = ['banana','apple','rice','carrot','mango']

mylist = shoplist

del mylist[0]

print('shoplist is',shoplist[:])
print('mylist is',mylist[:])

print('Copy by making a full slice')

shoplist = ['banana','apple','rice','carrot','mango']

mylist = shoplist[:]

del shoplist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)