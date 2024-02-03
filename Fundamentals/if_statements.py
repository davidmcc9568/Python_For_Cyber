# Objective:
# Write a program that takes an age and will tell you if you are able to drive assuming a legal driving age of 16

age = input('Please enter your age to continue>> ')
age = int(age)

if age > 16:
    print('Here are the car keys.')
elif age == 16:
    print('Congrats for finally being old enough to drive!')
else:
    print('Sorry, you are not old enough to drive.')


# If you as the programmer do not handle the exceptions, the hacker will.
'''
try:
    age = int(input('Enter your age to see how old uou will be in 30 years>>> '))
    print(age + 30)

except: # Would usually name the exception here
    print('Something went wrong, please try again...')
'''
