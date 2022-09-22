# values aka literals - number values types - below:
# 3 types of numbers in python

x = 1		# int
y = 2.567	# float
z = 3 + 5j	# complex
z = 4j		# complex - j "imaginary part"

y2 = 2.567E3
y3 = 2.567e10

print( type(x) )	# <class 'int'>
print( type(y) )	# <class 'float'>
print( type(z) )	# <class 'complex'>

print( type(y2) )	# <class 'float'>
print( type(y3) )	# <class 'float'> 


# CASTING: In python, defining a type explicitly

# py uses classes to define data types

# casting done using constructor functions

print( int(1) )			# 1
print( int(2.89) )		# 2 	# value rounded down during casting :: floor operation in Math 
print( int('3') )		# 3
"""
print( int("Hi") )		# ValueError: invalid literal for int() with base 10: 'Hi'
"""

print( float(1) )		# 1.0
print( float(2.89) )	# 2.89
print( float('3') )		# 3.0

print( str('s') )		# 's' or "s" , both same ; 'hello' sames as "hello"
print( str(2) )			# '2'
print( str(3.0) )		# '3.0'


# STRINGS

# no char type, only string with length 1
# array of unicode characters (or bytes).

a = "thalam"	# a[3] = 'l'
print( a[3])

# getting a substring
print( a[2:4])  # 'al'
# syntax:
# string[start:end:step]  => all characters from start to end-1 not including only the step positions

# Get the first 5 characters of a string
strz = "freeCodeCamp"
print( strz[0:5])
print( strz[:5])

# Get the last character of a string
print( strz[-1])

# Get the last 5 characters of a string
print( strz[-5:])

# Get a substring which contains all characters except the last 4 characters and the 1st character
print( strz[1:-4])  # first char is at index 0

# Get every other character from a string
strz = "freeCodeCamp"
print( strz[::2])



#string functions
print( strz.strip()) 	# removes spaces from the start or end of string
print( len(strz) )
print( strz.lower() )
print( strz.upper() )
print( strz.replace('e', 'E') )		# find and replace all occurrences 

stry = "free,code,camp"
print( stry.split(',') )  		# ['free', 'code', 'camp']


# How to input from screen / command line === how to prompt for a value ?

x1 = input('Enter your name')
print("Hi, " + str(x1))
