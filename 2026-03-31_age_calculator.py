def birth_year(a):
    x = int(2026 - a)
    return x

def retirement_year(a):
    x = int(2026 + (65 - a))
    return x

name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter your city: ')

if age < 18:
    print(f'Sorry {name}, you are not old enough to access this content. Please come back when you are at least 18 years old.')
elif age >= 18 and age < 30:    
    print(f'Welcome {name}! You are eligible to access this content.')
else:
    print(f'Welcome {name}! You are eligible to access this content, but please be aware that it may not be suitable for all ages.')

print(f'{name}, you were born in {birth_year(age)} and you will retire in {retirement_year(age)}.')