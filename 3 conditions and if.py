# if condition
grades = [60,70,99,89,34,56]
for grade in grades:
    print('your grade is: ',grade)
    if grade >= 60:
        print('congratulations,you passed the exam')
    else:
        print('I am sorry you did not pass the exam')

# if conditions
grade = 70
print('you have passed the exam',grade >= 60)

print('you do not pass the exam',grade < 60)

print('you get the full score',grade == 100)

print('you are not the full score',grade != 100)

print('your grade is in middle level',grade >= 70 and grade < 90)

print('you have passed the exam and your grade is end with "0" ',grade >= 60 and (grade == 60 or grade == 70 or grade == 80 or grade == 90 or grade == 100))

print('you have passed the exam and your grade is end with "0" ',grade >= 60 and grade in [60,70,80,90,100])

# if statement
# 1
grade = 70
if grade >= 60:
    print('you have passed the exam')


# use with else
if grade >= 60:
    print('you have passed the exam')
else:
    print('you can not pass the exam')

# use with elif and else and only one condition can be executed
if grade <= 60:
    print('do not pass the exam')
elif grade < 80:
    print('mediun')
elif grade <90:
    print('great')
else:
    print('excellent')

# question1:judging if the username can be used
users = ['amy','tom','jack']
user_name = input('your user name is: ')
if len(user_name) < 6:
    print('you can not register the app for the length of your user name is less than 6')
if user_name in users:
    print('your name has been used please try another one')
else:
    print('available')



