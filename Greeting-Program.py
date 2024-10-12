# Excersice 2: Good Mornig 

import time
name = input('Enter your name: ')
timm = time.strftime('%I:%M:%S:%p')
print('The time in 12 hour formet is', timm)
tiim = time.strftime('%H:%M:%S:%p')
print('The time in 24 hour formet is', tiim)

tim = int(time.strftime('%H'))
if tim >= 00 and tim < 12:
    print("Good Morning",name)
elif tim >= 12 and tim < 17 :
    print("Good Evening",name)
elif tim >= 17 and tim < 22 :
    print("Good Afternoon",name)
else :
    print("Good Night",name) 
