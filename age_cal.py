from datetime import datetime,timedelta

def age_calucalator(dob):
    #Convert string to datetime object
    date_birth = datetime.strptime(dob,'%Y-%m-%d')
    today = datetime.today()
    # Calculate basic age
    age_years = today.year - date_birth.year
    if(today.month,today.day)<(date_birth.month,date_birth.day):
        age_years = age_years - 1
    next_birthday = date_birth.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year+1)
        #print(next_birthday-today)

    days_until_birthday = (next_birthday - today).days
    print(f"\nYou are {age_years} years old.")
    print(f"Days until next birthday: {days_until_birthday} days")
        
    
input_dob = input("Enter your date of birth (YYYY-MM-DD): ")
try:
    age_calucalator(input_dob)
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
