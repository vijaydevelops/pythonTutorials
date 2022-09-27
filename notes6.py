def my_func():
    print("Function execution")


my_func()


# FUnction with parameters / arguments
def my_func2(param1):
    print("Params: " + str(param1))


my_func2("ek")


# Functions with default params
def my_func3(param1="Rajini"):
    print("Mass Hero: " + str(param1))


my_func3("Vikram")
my_func3()
my_func3("Illayaraja")


# Functions which return values
def my_func4(param1="Rajini"):
    return ("Mass Hero: " + str(param1))


print(my_func4("Vikram"))

########
# LAMBDA Function
# any number of arguments,
# can have only one expression
# and result is returned after execution of this one expr

x = lambda a: a + 10
print(x)
print(x(5))


x = lambda a, b: a * b
print(x(5, 3))


def myFuncTest(n):
    return lambda a: a ** n

getSquareR = myFuncTest(2)          # lambda a: a**2
getCubeR = myFuncTest(3)            # lambda a: a**3

print(getSquareR(5))    #25
print(getCubeR(5))      #125

