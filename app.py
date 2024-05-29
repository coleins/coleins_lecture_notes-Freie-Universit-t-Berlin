# #Mosh Hamedani @ Youtube...................................
# python interpretor executes the code line by line

# # VARIABLES..............................................

# print("0----")
# print(" ||||")
# # the code below is an expression
# print("*" * 10)

# # integers are numbers without decimal point

# price = 10
# # update the value of the price variable
# price = 20
# # don't add quotes as it will print price instead of the value of the price variable
# print(price)


# # floating point is number with decimal point(float)
# rating = 4.9
# print(rating)
# # string
# name = "Collins"

# # booleans
# # python is case sensitive
# is_published = False
# print(is_published)

# # Exercise
# def patient(name, age, patient_status):
#     print(f"Patient's name is {name}.")
#     print(f"Patient's age is {age} years old.")
#     print(f"{patient_status } patient ")
# patient("Mark", 20, "new")
# patient("Mike", 30, "existing")


# # RECEIVING INPUT.....................................

# # instead of print we are going to use input funtion
# # the parenthesis calls the input function
# # expression is a piece of code that provides a value
# name = input("What is your name? ")
# # concatinate
# print("Hi " + name)

# name = input("What is your name?")
# color = input("What is your favorite color?")
# print(name + " likes " + color)

# # TYPE CONVERSION.........................................................

# birth_year = input("Birth year: ")
# age = 2024 - int(birth_year)
# print(age)

# name = input("What is your name?")
# school = input("Where do you study?")
# print("My name is " + name + ". I attend " + school + ".")

# weight_lbs = int(input("Weight (lbs): "))
# weight_kgs = (weight_lbs) * 0.453592

# print("The user weighs " + str(weight_kgs) + " Kgs!")

# # using tripple quotes for strings
# course = '''
# Hi John,
# Here is our first email to you
# Thank you,
# The support team
# '''
# print(course)

# # index
# course = "Python for beginners"
# print(course[0])

# print(course[-1])

# # the indexing below runs from index 0 but excludes the but excludes index 3
# print(course[0:3])
# # if you dont supply the end index, python will supply all the characters to the end of the end of the string
# print(course[1:])
# print(course[:5])
# # make a copy of the original
# another = course[:]
# print(another)
# # the code below prints the indexes from 1 to -1 excluding the character at index -1
# name = "Jennifer"
# print(name[1:-1])
# #FORMATTED STRINGS.....................................................
# # string concatination vs formatted string
# first = "John"
# last = "Smith"
# # string concatination
# message = first + " [" + last + "] is a coder"
# print(message)
# mes = first + " " + last + " is a coder"
# print(mes)
# # formated strings
# mess = f"{first} {last} is a coder"
# print(mess)
# # formated sptrings make it easier to visualize the output
# # the square bracket do not add any value to the code and thus can be omitted
# msg = f"{first} [{last}] is a coder"
# print(msg)

# # STRING METHODS..............................................

# course = "Python for Beginners"

# # len is a general purpose function used to count number of items in a string and list
# print(len(course))
# # we can use function. to access all other string methods
# # for instance this .upper method changes the entire string to upper case
# print(course.upper())
# # changes to lower case
# print(course.lower())

# # find a character or sequence of character in a string
# # it is case sensitive
# # in the case below we get 4 because the first "o" is at index 4
# print(course.find("o"))
# # we get 11 because beginners starts at index 11
# print(course.find("Beginners"))
# # to replace a sequence of characters in a string we use replace method. we add a comma to pass absolute beginners to replace beginners
# print(course.replace("Beginners", "Absolute Beginners" ))
# # moreover we can also replace a single character for instance. this prints out Jython
# print(course.replace("P", "J"))
# # we can revert the process by replacing the "j" with "P"
# print(course.replace("j", "p"))
# # the in operator
# # to check existence of a character or sequence of characters 
# # for instance to chech if Python is in the course variable
# # the outcome is a boolean value either True or False
# print("Python" in course)


# # #ARITHMETIC OPERATIONS........................................
# # + - * /
# print(10 + 2)
# print(10 - 2)
# print(10 * 2)
# print(10 / 3) #in this we get a floating point number
# # other thaan these common arithmetic operators we have more
# # the other kind of division
# # when we use 2 division operators we get an integer instead of a floating point number
# print(10 // 3)
# # modules which is a percentage sign(%) returns a remainder of the division (%)

# print(10 % 3)
# # another operator is the power( ** ) denoted by double multiplicaton symbol
# print(10 ** 3)


# # for a variable
# x = 10
# # we want to increment by 3
# x = x + 3
# # when we print x we should get 13
# print(x)
# # augmented assignment operator  (+=) (-=)
# # is a way to write the same code but in a shorter code 
# x += 3
# # the result will be the 13 which is the current value of x +3
# print(x)
# x-= 3
# print(x)

# # take into account the operator precedence- order of operations
# # BE-ODMAS
# # (B)rackets (E)xponentiation-power (O)f( D)ivision (M)ultiplication (A)ddition (S)ubtraction
# # in the case below the * has a higher precedence, is applied first then added to 10
# y = 10 + 3 * 2
# print(y)

# a = 10 + 3 * 2 ** 2
# print(a)

# b = (2 + 3)* 10 - 3
# print(b)


# # MATH FUNCTIONS.........................................................
# import math
# # built in python functions
# # given the variable
# x = 2.9
# # absolute (abs) always returns a positive number
# # the outcome of the function below is a positive 2.9
# print(abs(-2.9))

# # IMPORTANT- in order to write a program that involves complex mathematical calculation, import math modules. wWe can type math. to access all the accessible methods. Type on the browser python3 math module to practice on the different methods

# # IF STATEMENTS.................................................
# # allow us to build programmes that can make decisions based on certain conditions
# # For instance below is a text with a bunch of rules for a program
# # if it's a hot day
#     # It's a hot day
#     # Drink plenty of water
# # otherwise if it's cold
#     # It's a cold day
#     # Wear warm clothes
# # otherwise
#     # It's a lovely day


# # To start building the program start by defining the boolean variable
# is_hot = False
# # the code does not execute properly unless we create another variable 
# is_cold = False
# if is_hot:
#     print("It's a hot day!")
#     print("Drink plenty of water")
# # we then add a second condition using elif
# elif is_cold:
#     print("It's a cold day!")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
#     # the statement below will always be printed since no if-elif-else has been used
# print("Enjoy your day")


# # another senario is
# # price of a house is $1M
# # if buyer has good credit
#     # they need to put down 10% deposit
# # otherwise
#     #they need to put down 20%
# # My solution
# has_good_credit = False

# if has_good_credit:
#     print("Make a 10% deposit on house")
# else:
#     print("Make a 20% deposit on house")

# # Josh's solution
# price = 1000000
# has_good_credit = False
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

# # LOGICAL OPERATORS.............................................
# # used in a situation where we have multiple conditions
# # for instance an application for processing loans. an applicant can have a high income and good credit(both conditions True) thus eligible for loan.



# # AND: both
# # OR: at least one
# # NOT: gives the opposite of the boolean value assigned

# has_high_income = True
# has_good_credit = False
# # for the AND operator all conditions must be met for the desire outcome to be displayed
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Too bad for you")


# # for an instance where we consider whether the applicant has a good credit and criminal record we can use the (NOT) OPERATOR

# has_good_credit = True
# has_criminal_record = True
# if has_good_credit and not has_criminal_record:
#     print("Applicant can apply")
# else:
#     print("Not elgible for application")

# # COMPARISON OPERATORS..........................................
# # <  >   <=   >=   ==   !=
# # Used in situations where we want to compare a variable with a value
# # for example
# # if temperature is greater than 30
#     # it's a hot day
# # otherwise if its less than 10
#     # it's a cold day
# # otherwise
#     # it's neither hot nor cold

# # begin by defining the temperature variable/ assignment statement
# temperature = 35
# # temperature > 30 is a boolean expression as it is a piece of code that produces a value
# if temperature > 30:
#     print("It's a hot day")
# elif temperature < 10:
#     print("It's a cold day")
# else:
#     print("It's neither hot not cold")

# # Another example
# # In a login form if name is less than 3 characters long
#     # name must be atleast 3 characters
# # otherwise if it's more than 50 characters long
#     # name can be a maximum of 50 characters
# # otherwise
#     # name looks good


# # My solution
# name = "Ribashongilo Gasheshiakili Ribashongilo Gasheshiakili Ribashongilo Gasheshiakili"
# print(name)
# name_characters= len(name)
# print(name_characters)

# if name_characters < 3:
#     print("Name must be atleast 3 Characters long")
# elif name_characters > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")

# # Mosh's solution
# name = "J"
# if len(name) < 3:
#     print("Name must be atleast 3 Characters long")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")

# # WEIGHT CONVERTER PROGRAM .....................................

# # case 1
# # Weight: 160
# # (L)bs or (K)g: l
# # You are 72.0 kilos

# # case 2
# # Weight: 72
# # (L)bs or (K)g: k
# # You are 160.0 kilos

# # Mosh solution
# # input function always returns a string therefore use the upper method to always convert the users input to upper case. the weight is also a str thus necessary to convert to int to make the calculations
# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")

# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# # WHILE LOOP.....................................................
# # we use whle loop to execute a block of code multiple times. useful in building interactive programmes and games

# # Begin by writing a while statement followed by a condition. As long as the condition is True, the code written below the block will be repeatedly executed.
# # i is the short form for index
# # define variable i
# i = 1
# while i <= 5: #condition is True when i is less than 5
#     print(i) # if we just leave it at this without the expression below it will print infinitely as if i is not incremented 
#     i += 1
#     # the line below is not indented so that it prints at the end of the loop, otherwise it will be printed after every loop
# print("Done")

# # in the example below the asterics are printed with one more in each loop till it reaches 5 asterics as per the condition
# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1


# # GUESSING GAME.................................................
# # the game is to make a guess of the nmber 9

# # Josh's solution
# secret_number = 9 #defining vriable
# # we want to give the user a maximum of 3 guesses
# guess_count = 0 #represents number of guesses user has made
# guess_limit = 3 #the reason for this varale is to make the while loop readable
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")#if the code stops here the program will continue prompting the user to make the guess again even though it is the right guess therefore include a break
#         break
# else:
#     print("Sorry you failed!")# a while loop can have an else block, which gets executed if the user does not successfully guess the number

# BUILDING THE CAR GAME........................................
# (building engine for this game)
# start - to start the car(Car started... Ready to go!)
# stop - to stop the car(Car stopped.)
# quit - to exit
# else i dont understand that
# REVISIT BUILDING THE CAR GAME

# # FOR LOOP........................................................................
# # used to iterate over characters in a string and list
# for item in ["Mosh", "John", "Sarah", 1]:
#     print(item)

# for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(item)
# # since we dont want to type a list of lengthy numbers, say from 0 to 100 we use range
# for item in range(10):#the range excludes 10
#     print(item)
# # if we want to start from 5 to 10 we can run the following range function
# for item in range(5, 10):
#     print(item)
# # we can pass 2 as the step to this function and when we run the code it will go to steps foward
# for item in range(5, 10, 2):
#     print(item)
# # Calculate the total cost of shopping items
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(total) #or use formated string.....print(f"Total: {total})

# # NESTED LOOPS..................................................................
# # means adding one loop into another loop
# # for instance generating a list of coordinates
# # for the program below in the first iteration
# for x in range (4):#outer loop- this range function generates num 0-4 but not inclusing 4
#     for y in range(3):#inner loop- this range function generates num 0-3 but not inclusing 3
#         print(f"({x}, {y})") #the program iterates the inner loop first then the outer loop

# numbers = [5, 2, 5, 2, 2]
# # not the best solution though it yields same outcome
# for x_count in numbers:
#     print("x" * x_count)

# # the correct solution
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers: #at first iteration x_count willl be 5
#     output = " "#this is important to reset the output variable to an empty string
#     for count in range(x_count): #we are using this to generate a sequence of numbers from 0 upto x_count
#         output += "x"
#     print(output)


# # LISTS..........................................................................
# # the origin list is not affected in any way
# names = ["John", "Mosh", "Joan", "Mary", "Sarah"]
# print(names)

# # we can access individual items using an index [2]
# print(names[2])
# print(names[-2])
        
# # we can also get a range of items in the list
# print(names[2:])#this returns all the items starting from an index of 2 to end of the list
# print(names[2:4])#this will return all the items from the 2nd index to the 4th index excluding the item at that index
# print(names[:])#this assumes 0 as the default index thus returning all items from the beginning

# # getting maximum number in a list... we need a for loop
# numbers= [3, 6, 2, 8, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
    
# # 2D LISTS [...]..................................................................
# # extremely powerful and have alot of applications in data science and machine learning
# # for instance a 3 by 3 matrix 

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix [0][1] = 20 # this moifies the value of the matrix
# # to access an individual item in the matrix we use []
# print(matrix[0][1])#to access the 2 in the marix- the [0] returns the first list [1] is the index of 2

# # WE CAN ALSO USE NESTED LOOPS TO ITERATE OVER ALL THE ITEMS IN THE MATRIX
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)#we get all the items in our list

# # LIST METHODS...................................................................

# numbers = [5, 2, 1, 7, 4]
# numbers.append(20)#adds 20 to the end of the list
# print(numbers)
# numbers.insert(0, 10)# inserts 10 to index 0 in the list
# print(numbers)
# numbers.remove(5)#removes 5 from the list
# print(numbers)
# numbers.clear()#removes everything from the list
# print(numbers)

# numbers = [5, 2, 1, 5, 7, 4]
# numbers.pop()#removes last item from our list
# print(numbers)
# print(numbers.index(5))#check the index of an item in a list
# # to also check for existence of an item in the list
# # this method will output a boolean value unlike the index method
# print(50 in numbers)#returns False unlike the index method which throws an error
# print(numbers.count(5))#another method for counting. returns the number of times an item appears in the list
# numbers.sort()#arranges the list in ascending order
# print(numbers)
# #to sort in descending we can use the reverse method which sorts the list in descending order
# numbers.reverse()
# print(numbers)
# # to make a copy of the list 
# numbers2 = numbers.copy()
# # we can the ad 10 to the copy
# numbers2.append(10)# adds 10 to the end of the copy
# print(numbers2)
# # to remove duplicates from this list
# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)#duplcates removed

# # TUPLES........................................................................
# # similar to list but are immutable... we cannot modify them
# # we can only count the number of items in the tuple and find the index of tems in the tuple
# numbers = (1, 2, 3)
# print(numbers[0])#getting the item at index 0 

# print(numbers.count(3))#counts the number of times 3 appears


# # UNPACKING....................................................................
# # can be used in lists and tuples
# # 
# coordinates = (1, 2, 3)#coordinates of x, y and z
# x, y, z = coordinates #pthyon intepretor assigns these variables to the items in the tuple
# print(x)
# print(y)
# print(z)

# # DICTIONARIES {..}............................................................
# # are the equivalent of objects in Javascript
# # used in situations where we want to store info with key value pairs
# # for instance
# # a customer has a bunch of attributes like name (Mark) email(zuckerburg@gmail.com), phone number(0791150122). The keys are name, email and phone number. Values are Mark, zuckerburg@gmail.com, 0791150122
# # we cannot duplicate the keys in dictionaries
# # just like a dictionary in the real world each key is listed only once
# # The value can be of any other data type 

# # we can define a dictionary with the following variable
# customer = {
#     "name": "John Smith",
#     "age": "30",
#     "is_verified": True

# }
# # we can access each item in the ictionary using []
# # it is case sensitive
# print(customer["name"])
# # we can only access the keys that exist in the dictionary
# # we get key error when we pass a key that does not exist
# # to get around the key error we can use get method

# # instead of using the square brackets we call the get method and specify our key
# print(customer.get("birthdate"))#thi prints out None as birthdate value does not exist in the dictionary

# # we can also supply a default value. for instance if the dictionary doesn't have a default value we can supply jan 1 1980
# print(customer.get("birthdate", "Jan 1 1980"))

# #we can also update the values 
# customer1 = {
#     "name": "Mark Odongo",
#     "age": 30,
#     "is_verified": True
# }

# customer1["name"] ="Collins Powell"#updates the name
# print(customer1["name"])

# customer1["birthdate"] ="Jan 30 1998"#adds birthdate to list
# print(customer1["birthdate"])
# print(customer1)#shows the updated name and the birthdate included

# # exercise
# # program that prints numbers to words

# phone = input("Phone : ")
# numericals = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four",
#     "5" : "Five",
#     "6" : "Six",
#     "7" : "Seven",
#     "8" : "Eight",
#     "9" : "Nine",
#     "0" : "Zero"

# }

# output = ""
# for character in phone:
#   output +=  numericals.get(character, "!") + " "
# print(output)


# # EMOJI CONVERTER Application
# message = input(">") #we pass > as an indicator for user to enter message
# words = message.split(" ") #this will split the string by a space so that the input is spaced. We pass the string with one space as a separator. the split method goes throgh the string and when it finds the " " it uses that as a boundary to separate the string into multiple words.
# # we need to define a dictionary for mapping special characters like :) into a smilling face emoji.
# emojis = {
#     ":)": "😁",
#     ":(": "😒"
# }
# output = ""
# #we need to loop through the list get each word and potentially map it to an emoji using for loop. if there is no word supply a default emoji
# for word in words:#we want to go to the dictionary and see if we have an item with word as a key if the item exists we use its value otherwise we want to use thesame word by supplying a default value. we use get method to supply a default value
# # we need an output variable. we get the return value of our get method and add it to our output variable 
#    output += emojis.get(word, word) + " "
# print(output)


# # FUNCTIONS...................................................................
# # function is a container or a line of code that perform a specific task
# # when building large complex programmes we should break up our code into smaller reusable chunks, functions to better organize our code
# # program for printing a greeting message

# def greet_user():#the colon is telling python we are defining a block of code
#     print("Hi there")#before this line declare the function in the space above
#     print("Welcome")
# print("Start")
# greet_user()
# print("Finish")
# # in the code above the output is start, hi there, welcome, and finish in that order.
# # explanation
# # When python runs the code it doesn't actually print the indented mesaage which are inside the function. They only get executed when we call the function. if the function is not called the two indented lines will not get executed
# # The execution of the program starts at the print("Start"), after that python recognizes that we are calling the greet_user function, so it jumps inside the greet_user function and execute the two indented lines. then it wil jump outside of the function and continue the normal execution of the program print("Finish")


# # PARAMETERS...................................................................

# # def greet_user():
# #     print("Hi there")
# #     print("Welcome")
# # print("Start")
# # greet_user()
# # print("Finish")
# # what is the different between calling the greet_user() function and the print("Start") function in python.... the difference is that print function takes some information- the message we want to print whereas the greet_user function doesn't take any information

# # to pass information to the function 
# # parameters are placeholders for receiving information
# # for instance we can have the (name) parameter in our function and pass the users name when calling the function

# def greet_user(name):
#     print(f"Hi there {name}")#so we use the formated string to include the name when calling the function.this allows the function to be reusable. when we want to print a different name, no need to declare the name variable.
#     print("Welcome")
# print("Start")
# greet_user("Shadrack")#when a function has a parameter we are obligated to pass a value. we get Type error if we do not pass the value for the parameter
# # argument in programming is the value we supply to a function. in our example Shadrack is the argument that we pass to the name parameter.
# # parameters are placeholders defined in a function for receiving information
# # arguments are the actual pieces of information that we supply to the function
# greet_user("Waweru")
# print("Finish")

# # we can define multiple parameters in a function
# # we should always pass an argument for the parameters we define to avoid Type Error
# the type of argument in the illustration below is positional argument
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name}")
#     print(f"Welcome {last_name}")
#     print(f"Do your homework {last_name} {first_name}")
# print("Start")
# greet_user("John", "Smith")
# print("Finish")

# # KEYWORD ARGUMENTS........................................................
# # Keyword arguments are the combination of having the parameter name followed by its value
# # with the keyword arguments the position does not matter

# def greet_user(first_name, last_name):
#     print(f"Hi {first_name}")
#     print(f"Welcome {last_name}")
#     print(f"Do your homework {last_name} {first_name}")
# print("Start")
# greet_user("John", last_name="Smith")#keyword arguments used. We dont have to worry about the order of the parameters. important in certain scenarios
# print("Finish")

# # keyword arguments are suitable to allow readability. for intance in a situation where we are calculating costs
# #  calc_cost(total= 50, shipping=5, discount=0.1)

# # for the most part use positional arguments, unless you are usingvalues that contain numbers, so that you enable readability.
# # keyword arguements should always come after positional arguments when calling a function to avoid erros.... for instance in-  greet-user("James", first_name="Luke") function

# # RETURN STATEMENT..............................................................
# # create functions that returns values
# def square(number):
#     return number * number#the return statement returns value to the caller of a function
# result = square(3)#this is the caller which calls the square of 3. we have stored the returned value in a variable called result
# print(result)
# # to write shorter code we could avoid creating the result variable and instead call the returned value inside the print
# def sum(a, b):
#     return a + b
# print(sum(1, 2))

# # CREATING A REUSABLE FUNCTION....................................................
# # message = input(">")
# # words = message.split(" ")
# # emojis = {
# #     ":)": "😁",
# #     ":(": "😒"
# # }
# # output = ""
# # for word in words:
# #    output += emojis.get(word, word) + " "
# # print(output)
# # we want to reorganize this code into a function. we want to extract a funtion in this code. because the algorithm for converting the smiling faces into emojis is something that we would want to use in alot of different other applications, the lines from words to output above belong to our algorithm. we should put them in a separate function.
# #our funtionss should not include receiving input and printing output as in the code above
# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😁",
#         ":(": "😒"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
    

# message = input(">")
# print(emoji_converter(message))


# # EXCEPTIONS- HOW TO HANDLE ERRORS IN THE INPUT FUNCTION...........................
    
# # age = int(input("Age: "))
# # print(age)#when we enter a numerical value the program terminates successfully with no errors but when when we input a different value that is not a number it shows a valueError: invalid literal for int() with base 10:
# # this message tells us that the input does not have a valid whole number that can be converted to an integer.
# # to print a proper error message we use try accept to handle errors
# try:
#     age = int(input("Age: "))
#     print(age)
# except ValueError:#we added a type of error that our program may encounter(value error)
#     print("Invalid value")#we are instructing our program to run the error message instead of crushing our program. this error is an exception. 
# #An exception is the kind of error that crushes our program.
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age#when we print age (0) we get a zero division error since we cannot divide a number by zero. we  need another exception of type zerodivision error
#     print(age)
# except ValueError:
#     print("Invalid value")
# except ZeroDivisionError:
#     print("Age cannot be zero")
# # as a good programmer we should always anticipate these kind of errors and handle the maccordingly using exception

# COMMENTS.....................................................................
# comments are ignored
# we can use them as reminders to fix things or communicate with other developers
# too much comments are not good
# use them to explain why's and how's not what's



# # CLASSES.....................................................................
# # classes are extremely important in python
# # used to define new types eg numbers, strings, booleans, lists, dictionaries, tuples
# # classes are therefore used to define new types to model real concepts eg. shopping cart, cars

# # start by defining a class using class keyword
# # we give the class a name
# # in naming our classes we use the Pascal naming convention eg class EmailClient
# class Point:
#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")

# # object is the instance of a class. class simply defines a blueprint or template for creating our object. Object are the actual instances based on that blueprint

# # to create an object we type out the name of our class and call it like a function
# point1 = Point()
# # the dot operator has the two methods that we defined draw, and move and other magic methods
# point1.draw()#by running this program dra is printed in the terminal

# # other than methods these objects can have attributes. they are like variables that belong to a particular object.
# point1.x = 10
# point1.y = 20
# # print(point1.x)#these prints out the x coordinates in the terminal

# # each object is a different instance of our first object
# # we can create another object
# point2 = Point()
# # when we print(point2.x) we get a tributeError because point 2 does not have an attribute called (x)
# point2.x = 1
# print(point2.x)

# # RECAP
# # we use classes to define new types, these classes can have methods that can be defined anywhere inside our class eg move, draw, and also have attributes that can be set anywhere in our programs

# # CONSTRUCTORS.....................................................
# # it is possible to have a point object without the x and y coordinates as in the case above. that will not work unless we know where that point is located.
# #the problem is, we get an attribute Error stating point object has no attribute called x
# # a constructor is function that gets called at the time of creating an object
# # 

# class Point:
#     def __init__(self, x, y):#parameters x, and y passed alongside self
#         self.x = x #we use self to reference the current object and set x attribute to the x argument passed in this function
#         self.y = y#referene to the y object(coordinate)
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
# point = Point(10, 20)#here we are creating an object point passing the value 10 and 20 which are the x and y coordinates initialized. therefore on the top we define a new function using the __init__(initialized). we pass the parameters (self, x, y)

# point.x = 11# to change/update the x value
# print(point.x)



# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi I am {self.name}")

# john = Person("John Smith")
# john.talk()

# bob = Person("Bob Smith")
# bob.talk()

# INHERITANCE...................................................











