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
month = input("Please enter the 3 ditig month (Jan - Dec): ")
day = int(input("Please enter the 2 digit day of the month (01-31)"))

from datetime import datetime
test = datetime.strptime(f"2022-{month}-{day}", '%Y-%b-%d')
spring = datetime(2022, 3, 20)
summer = datetime(2022, 6, 21)
fall = datetime(2022, 9, 22)
winter = datetime(2022, 12, 21)
if test >= spring and test < summer:
    season = "Spring!"
elif test >= summer and test < fall:
    season = "Summer"
elif test >= fall and test < winter:
    season = "Fall"
else:
    season = "Winter"
print(f"{month}-{day} is in {season}")