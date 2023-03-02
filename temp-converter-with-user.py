
def convert_temp(ce) : 
    
    Farenheit = float(ce) * 9/5 +32

    print (ce , 'degrees celsius are ', Farenheit, 'degrees Farenheit.')

    if float(ce )> 38 : 
        print('it is too hot')

user = input('nter a temperature in degrees Celsius:')

convert_temp(user)