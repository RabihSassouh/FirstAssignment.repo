top=float(input('please enter your top number: '))
bottom=float(input('please enter your bottom number: '))
val=float(input('please enter your third number to make sure if it is between your top and bottom numbers or not: '))
#if type(top)!= float or type(bottom)!= float or type(val)!= float:
#    print('please enter valid numbers, make sure not to enter letters or symbols...')
#else:
if top>=val>=bottom:
    print(True)
else:
    print(False)

