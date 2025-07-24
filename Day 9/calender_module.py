import calendar

calendar.setfirstweekday(calendar.MONDAY) # Starts the calendar from the specified day
print(calendar.month(2025,7)) #prints the calendar of the given year and month
print(calendar.weekday(2025,7,24)) # Prints day of the week in integer format

hc = calendar.TextCalendar(calendar.SUNDAY) #Returns calendar in text format
print(hc.formatmonth(2025, 7))

hc=calendar.HTMLCalendar(calendar.MONDAY) # Prints HTML code for displaying a calendar
print(hc.formatmonth(2025,8))

