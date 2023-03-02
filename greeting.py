def greeting(gender):
    if str(gender).lower() == 'male':
        print('hello Sir')
    elif str(gender).lower() == 'female':
        print('hello madam')
    else : 
        print('unvalid input')       

user = input('what is your gender?')

greeting(user)