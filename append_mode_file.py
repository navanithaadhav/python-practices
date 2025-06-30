#APPEND mode file in pi
"""
Created on Mon Nov 28 10:36:45 2022

@author: ADMIN
"""

try:
   file=open('Nava.txt','a')
   file.write('Nava open a new IT company')
   file.close()
   file=open('Nava.txt','r')
   print(file.read())
except FileNotFoundError:
    print('Error:File Not Found')
else:
    file.close()