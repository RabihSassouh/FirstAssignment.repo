a=int(input('enter an interger a='))
b=int(input('enter an interger b='))
c=int(input('enter an interger c='))
max=a
if a>=b:
    max=a
else:
    max=b
if c>=max:
    max=c
min= min(a,b,c)
print('The maximum value is: ',max)
print('The minimum value is: ',min)
