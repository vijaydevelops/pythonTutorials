from sys import intern

# Arithmetic operators
#	+ - * / 
#	% 	Modulus
#	**	Exponentiation # to power of
#	//	Floor division

print(11 % 5)	# 1
print(11 ** 5)	# 161051  
print(11 // 5)	# 2


# Asssignment operators
# = 
# += -= *= /= %= //= **= 
# &= |= ^= >>= <<=


# Comparison operators
# ==  !=  >  <  >=  <=


# Logical operators (combine conditional expressions)
# and , or , not
# Learn TRUTH TABLES FOR AND, OR, NOT, ...




# Identity operators
# comparing two objects
# to check if the values are same, and also the memory location same
# is 	eg: x is y
# is not	eg: x is not y

# to get the identity of an object, use id()
x = 10
print( id(x) ) 			# 1192942174736

# You can use sys.intern() to intern strings for performance. 
# <<< Each number is stored at a singular and fixed place in memory, which saves memory for commonly-used integers.>>>>
# This function allows you to compare their memory addresses rather than comparing the strings character-by-character:
a = 'hello world'
b = 'hello world'
# a is b 	# False

a = intern(a)
b = intern(b)
print( a is b )
# => True


# x is y
# x is not y





# Membership operators
# to find if a value is present in a sequence or list or array
# x  in  y
# x not in y



# Bitwise operators
#  & | ^ ~ << >>
# AND (both bits 1 => 1) 
# OR  (atleast one bit 1 => 1) 
# XOR (only if any one bit 1 => 1)
# NOT (reverses bits)
# Zero fill left shift
# Signed right shift