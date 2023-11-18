#Conditional execution: a block of one or more statements will be executed if a certain expression is true
#Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true


month =input('Enter the month of the year: ').lower()
season = ''
if month in ["september" "october" , "november"]:
   season = 'Autumn'
elif month in ["january" , "february"]:
   season = 'winter'
elif month in ["march", "april" , "may"]:
    season = 'Spring'
elif month in["june", "july" , "august"]:
    season = 'Summer'
else:
   print('Invalid month')
   
if season:
   print(f'The season in{month.capitalize()} is: {season}')