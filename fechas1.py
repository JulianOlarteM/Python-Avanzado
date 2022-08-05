import datetime

my_time = datetime.datetime.now() #el modulo datetime contiene una clase  llamada tambien datetime,  el metdodo now
print (my_time)   
print('-' *60) 

my_day = datetime.date.today()
print(my_day)
print('-' *60) 

my_day2 = datetime.date.today()
print(f'Year: { my_day2.year}')
print(f'Month: { my_day2.month}')
print(f'Day: { my_day2.day}')

print('-' *60) 

