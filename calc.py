loop = True
result = 0
while loop : 
    try:
      
        number = int(input('put your number > '))

        if  number == 0:
            print('the total is : ', result)
        else:
            result += number
            print('if you want to see the total put 0')     
    except:
        print('unvalid input xxxxx')      
   

   
      

    
    
   