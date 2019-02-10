

# def my_function():
#    print("This is my function!")
#
# Using simple arguments in the function
# def my_function(str1, str2):
#    print(str1)
#    print(str2)
#my_function("I Am", "Meumeu")

# Using Keyword argument
# set default values to argument (default values if no argument passed to the 
# function)

def print_something(name = "Someone", age= "unknown"):
    # print("My name is " +name + " and my age is " + str(age))
    # Or better
    print("my name is", name, "and my age is", age)

print_something("meu", 27)
# what about passing 1 argument
print_something("Nick")

# Keyword arguments
print_something(None, 27)
# None is the equivalent of Null : it is a keyword argument
# Other example
print_something(age=27, name="Nick")

# infinite number of argument
# * means the number of argument is unknown

def print_poeple(*people):
    # create an array named poeple
    for person in people:
        print ("this person is", person)

print_poeple("Nick", "Dan", "Jack", "David", "Meumeu" )

# Return values
def do_math(num1,num2):
    return num1 + num2

math1 = do_math(5,7)
math2 = do_math(11,34)
print("math1", math1, "math2", math2)


