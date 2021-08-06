# Input birthdate
b_day = int(input('Enter your birth date (1-31): '))
b_month = int(input('Enter your birth month (1-12): '))
b_year = int(input('Enter your birth year (1900-2021): '))

# Present date
p_year = 2021

# Calculate age
age = p_year - b_year
print('You are', age, 'years old')