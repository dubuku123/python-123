string = input('Enter any string: ')

upper, lower = 0, 0
for i in string:
   
    if(i.islower()):
        lower = lower + 1
    
    elif(i.isupper()):
        upper = upper + 1


print('Lowercase characters:',lower)

print('Uppercase characters:',upper)
