num1 = 42 # variable declaration, number initialize
num2 = 2.3 # variable declaration float, initialize
boolean = True # variable declaration, boolean initialize
string = 'Hello World'# variable declaration, string initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, List initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, tuple initialize
print(type(fruit)) # print to console, type check
print(pizza_toppings[1]) # print to console, list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #print to console, dictionary access value
person['name'] = 'George'# dictionary change value
person['eye_color'] = 'blue' # dictionary change value
print(fruit[2]) # print to console, tuple access data

# conditional if, evaluation, conditional else, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#conditional- if- elif- else, print to console
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop start at 0 until 5, print to console
for x in range(5):
    print(x)

# for loop start at 2 until 5, print to console
for x in range(2,5):
    print(x)

# for loop start at 2 until 10, increments by 3, print to console
for x in range(2,10,3):
    print(x)
# while loop, variable declaration
x = 0
while(x < 5):
    
# print to console  
    print(x)
# increasment by 1
    x += 1
# list delete value at end
pizza_toppings.pop()
# list delete value at index
pizza_toppings.pop(1)
# print to console of dictionary
print(person)
# dictionary delete value
person.pop('eye_color')
# print to console of dictionary
print(person)

# for loop through a list
for topping in pizza_toppings:
    # conditional if
    if topping == 'Pepperoni':
    #continue
        continue
    #print to console
    print('After 1st if statement')
    # conditional if
    if topping == 'Olives':
        
        # stops the loop
        break
# function declaration
def print_hello_ten_times():
    # for loop starts at 0 until 10
    for num in range(10):
        #print to console
        print('Hello')
# function call
print_hello_ten_times()
# function declaration
def print_hello_x_times(x):
    # for loop until a given number x
    for num in range(x):
        # print to console
        print('Hello')
# fuction call arguement of 4
print_hello_x_times(4)
# function declaration with default  paramenter
def print_hello_x_or_ten_times(x = 10):
    # for loop until x
    for num in range(x):
        # print to console
        print('Hello')
# function call goes until 10
print_hello_x_or_ten_times()
# function call goes until 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
# print to console,variable declaration
print(num3)
# variable declaration, number initialize
num3 = 72

# fruit[0] = 'cranberry'

# print(person['favorite_team'])

# print to console, list access value
print(pizza_toppings[7])

#print to console, variable
print(boolean)

#list add value
fruit.append('raspberry')

# list delete value at index
 fruit.pop(1)