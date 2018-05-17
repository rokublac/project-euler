'''
You are given the following information, but you may prefer to do some research for yourself.

"1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine."

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
# *Credit to http://www.mathslovers.com for the day of specific date calculation

# Day and month codes - not really sure how these numbers came to be but I got the values from https://www.youtube.com/watch?v=w-kmTvXr85M
dayCodes = {'friday':0, 'saturday':1, 'sunday':2, 'monday':3, 'tuesday':4, 'wednesday':5, 'thursday':6}
monthCodes = {'jan':2, 'feb':5, 'mar':5, 'apr':1, 'may':3, 'jun':6, 'jul':1, 'aug':4, 'sep':7, 'oct':2, 'nov':5, 'dec':7}

def dayOfDate(dayDate, month, year):
	# Not a leap year by default
	leapYear = False
	# Check if leap year and whether it's a century
	if str(year)[-2:] == '00':
		if year % 400 == 0:
			leapYear = True
	elif str(year)[-2:] != '00' and year % 4 == 0:
		leapYear = True

	# Error checking
	if dayDate > 29 and month.lower() == 'feb' and leapYear:
		return("There are only 29 days in February for {0}.".format(year))
	if dayDate > 28 and month.lower() == 'feb' and not(leapYear):
		return("There are only 28 days in February for {0}.".format(year))
	if dayDate > 30 and month.lower() in ['sep', 'apr', 'jun','nov']:
		return("There are only 30 days in {0}.".format(month))
	if dayDate > 31 or (month not in monthCodes):
		return("Invalid date.")
	
	
	if int(str(year)) >= 2000:
		lastTwoDigitsOfYear = 100 + int(str(year)[len(str(year))-2:])
	else:
		lastTwoDigitsOfYear = int(str(year)[len(str(year))-2:])

	monthCode = monthCodes[month.lower()]
	day = int((lastTwoDigitsOfYear + (lastTwoDigitsOfYear / 4) + dayDate + monthCode) % 7)

	# Since I am trying to get the key in the dayCodes dictionary, I decided to split the keys and values into seprate lists.
	# I then find the index of the value I want and then match it to the keys in the key dictionary.
	if leapYear and (month in ['jan', 'feb']):
		try:
			result = list(dayCodes.keys())[list(dayCodes.values()).index(day-1)]
		except ValueError:
			# If there is a value error it means that it is thursday since 0-1 (friday key value - 1) equates to thursday
			result = list(dayCodes.keys())[list(dayCodes.values()).index(6)]
	else:
		result = list(dayCodes.keys())[list(dayCodes.values()).index(day)]

	return(result.capitalize())



year = 1900
firstDayOfMonthSunday = 0
for y in range (1, 101):
	year += 1
	for month in range(0, 12):
		for day in range(1,2):
			resultDay = dayOfDate(day, list(monthCodes.keys())[month], year)
			if day == 1 and resultDay == 'Sunday':
				firstDayOfMonthSunday += 1
			

print("There are {0} Sundays between 1 Jan 1901 and 31 Dec 2000".format(firstDayOfMonthSunday))
