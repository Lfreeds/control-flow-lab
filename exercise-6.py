# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


month = (input("Enter a month of the year (Jan - Dec) as 3 characters: ").lower())
day = int(input("Enter the day of the month: "))

if month in ["jan", "feb", "mar"]:
    season = "Winter"
    if month == "mar" and day >= 20:
        season = "Spring"
    print(f"{month} {day} is in {season}")
elif month in ["apr", "may", "jun"]:  
    season  = "Spring"
    if month == "jun" and day >= 21:
        season = "Summer"
    print(f"{month} {day} is in {season}")
elif month in ["jul", "aug", "sep"]:
    season = "Summer"
    if month == "sep" and day >= 22:
        season = "Fall"
    print(f"{month} {day} is in {season}")
elif month in ["oct", "nov", "dec"]:
    season = "Fall"
    if month == "dec" and day >= 21:
        season = "Winter"
    print(f"{month} {day} is in {season}")