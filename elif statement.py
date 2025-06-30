# elif statement
"""
library late days                  fine rupees
0                                  no fine
1-5                                0.5
5-10                               1
10-30                              5
>30                                membership cancel
"""
days=int(input('Enter the days:'))
if(days==0):
    print('Good, No Fine')
elif(days>=1 and days<=5):
    print('Your Fine Amount:',days*0.5)  
elif(days>=5 and days<=10):
    print('Your Fine Amount:',days*1)
elif(days>=10 and days<=30):
    print('Your Fine Amount:',days*5) 
elif(days>=30):
    print('Your Membership was canceled')