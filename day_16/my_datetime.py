from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
print("Today is" , day,month,year,hour,minute)
#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)
#Today is 5 December, 2019. Change this time string to time.
date_string = '5 December, 2019'
print('date_string =', date_string)
#Calculate the time difference between now and new year.
t1 = datetime(year=2023,month=11,day=25)
t2 = datetime(year = 2024,month =1,day =1)
t3 = t2-t1
print("Difference between new year and now is :",t3)
#Calculate the time difference between 1 January 1970 and now.
today = datetime(year=2023,month=11,day=25)
day_1970 = datetime(year=1970,month=1,day=1)
time_difference = today-day_1970
print("Difference between Jan 1970 and now is:", time_difference)
