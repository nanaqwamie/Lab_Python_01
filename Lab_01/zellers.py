#archibold_acheampong

A = input('Please enter the month from 1-12 :')
B = input('Please enter the day from 1-31 :')
C = input('Please enter the year (from 0 - 99, eg. 88 in 1988 ):')
D = input('Please enter the century (from 0 - 99, eg. 19 in 1988 :')
if A==11:
    C=C-1
if A==12:
    C=C-1

W = (13*A - 1) / 5
X=C/4
Y=D/4
Z = W + X + Y + B + C - 2*D
R = Z % 7

if R<0:
    R=R+7

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
         'Thursday', 'Friday', 'Saturday']
day_of_the_week = days[R]
    
print'the day is :',day_of_the_week

