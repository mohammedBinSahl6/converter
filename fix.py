# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# num_one = int(input("Enter a number: "))
# num_two = int(input("Enter another number: "))

# message = "The result of " +str(num_one) + " + "+str(num_two) + " is " +str( add(num_one, num_two))
# print(message)

# message = "The result of " + str(num_two) + " - " + str(num_one) + " is " + str(subtract(num_one, num_two))
# print(message)


# def greet(name, age):
#     message = "Your name is " + name + " and you are " + str(age) + " years old."
#     return message

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(greet(name, age))

def get_result(answer):
    if answer == 'a':
        return True
    else:
        return False

print("Do you like programing?")
print("a. Yes")
print("b. No")
result = input("Enter a or b: ")

if get_result(result):
    print("Awesome! Programming is really fun!")
else:
    print("Hang in there! It's an acquired taste!")