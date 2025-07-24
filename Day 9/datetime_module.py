import datetime

dt=datetime.datetime.now() # Returns Current date and time combined together
t=dt.time() # Returns current time
print(t.strftime('%H:%M %p')) # Prints time in Hours in 24hrs format(%H) : Minutes(%M) AM/PM(%p) format

td=datetime.date.today() # Returns today's date
print(td.strftime('%d-%m-%Y, %A')) # %d-date, %m-month, %Y-Year, %A-Day of the week
print(td.year) # td.month(Returns month), td.day(Returns day)

d=datetime.date(2024,1,17) # Returns the specified date
print(d)
print(d.strftime('%j')) # Prints the day number in the year(001-365/366)