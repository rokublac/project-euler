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
# Still in progress
# Not really sure how the process came to be but I got the values and instructions from https://www.youtube.com/watch?v=w-kmTvXr85M
# So credit to http://www.mathslovers.com for the day of specific date calculation

# Get the day of a specific date
def dayOfDate(dayDate, month, year):
	
	dayCodes = {'friday':0, 'saturday':1, 'sunday':2, 'monday':3, 'tuesday':4, 'wednesday':5, 'thursday':6}
	monthCodes = {'jan':2, 'feb':5, 'mar':5, 'apr':1, 'may':3, 'jun':6, 'jul':1, 'aug':4, 'sep':7, 'oct':2, 'nov':5, 'dec':7}
	leapYear = False

	# Check if a leap year
	if year % 4 == 0:
		leapYear = True

	if int(str(year)) >= 2000:
		lastTwoDigitsOfYear = 100 + int(str(year)[len(str(year))-2:])
	else:
		lastTwoDigitsOfYear = int(str(year)[len(str(year))-2:])

	monthCode = monthCodes[month.lower()]
	day = int((lastTwoDigitsOfYear + (lastTwoDigitsOfYear / 4) + dayDate + monthCode) % 7)

	# Since I am trying to get the key in the dayCodes dictionary, I decided to split the keys and values into seprate lists.
	# I then find the index of the value I want and then match it to the keys in the key dictionary.
	if leapYear and (monthCode == 2 or monthCode == 5):
		try:
			result = list(dayCodes.keys())[list(dayCodes.values()).index(day-1)]
		except ValueError:
			# If there is a value error it means that it is thursday since 0-1 (friday key value - 1) equates to thursday
			result = list(dayCodes.keys())[list(dayCodes.values()).index(6)]
	else:
		result = list(dayCodes.keys())[list(dayCodes.values()).index(day)]

	print("On {0} {1} {2}, the day is {3}.".format(dayDate,month,year,result.capitalize()))

dayOfDate(20, 'jan', 2028)
