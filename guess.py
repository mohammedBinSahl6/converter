# user_guess = input('Guess the secert Word ?  ')

# secret_word = 'Greatful'

# if user_guess== secret_word : 
#     print('correct answer')

# else:
#     print('wrong answer')    

# user = input('what is the resault of   5+2 ? ')

# if user == '7':
#     print('Congratulations! You found the correct result.')
# else:
#     print('wrong answer')

# print('The program terminated successfully')        

secret_num = '2'
secret_color = 'red'

guess_num = input('Guess the number between 1 to 20 > ')
guess_color = input('Guess the color > ')

if guess_color == secret_color and guess_num == secret_num :
    print("You've found both the secret number and the secret color!")
elif guess_color == secret_color or guess_num == secret_num :
    print("You found at least one of the secrets!")
else:
    print("You didn't find any of the secrets! and Better luck next time!")    
print('try Again')    
