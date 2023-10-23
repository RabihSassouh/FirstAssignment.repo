total_grade=float(input('Enter the total grade of the student: '))
if 0<=total_grade<=59:
    print('The letter grade of this student is: F')
elif 59<total_grade<=69:
    print('The letter grade of this student is: D')
elif 69<total_grade<=79:
    print('The letter grade of this student is: C')
elif 79<total_grade<=89:
    print('The letter grade of this student is: B')
elif 89<total_grade<=100:
    print('The letter grade of this student is: A')
else:
    print('The grade you entered is not a valid grade.')