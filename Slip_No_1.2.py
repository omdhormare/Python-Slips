import datetime
d = int(input("Enter Day of Your Birthdate: "))
m = int(input("Enter Month of Your Birthdate: "))
y = int(input("Enter Year of Your Birthdate: "))

today = datetime.date.today()
dd = today.day
mm = today.month
yy = today.year

age_year = yy - y
age_month = mm - m
age_day = dd - d

if age_day < 0:
    age_day += 30  
    age_month -= 1

if age_month < 0:
    age_month += 12
    age_year -= 1

print("Day: ", age_day, " Month: ", age_month, " Year: ", age_year)
