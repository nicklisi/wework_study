import sys
import requests
import getopt
import re
from lxml import html
from lxml.html import builder as E


# Helper methods
def StripNT(title):
	title = title.replace("\n","")
	title = title.replace("\t","")
	return title

def StripComma(venue):
	venue = venue.replace(", ","")
	venue = venue.replace(" (Seattle)","")
	venue = venue.replace(" (Tacoma)","")
	venue = venue.replace(" (Bellevue)","")
	venue = venue.replace(" (Auburn)","")
	venue = venue.replace("Seattle, Seattle","Seattle")
	return venue

def TestDateFormat(date):
	return re.match(r'\w{4}-\w{2}-\w{2}',date)

# Prompt for dates and use to build URLs
dates = []
urls = []

# Get input 
while True:
	try:
		input_date = input("Enter date, in quotes, in the format 'yyyy-mm-dd' to get events data. \nYou can add more dates one at a time. \nType 'done', in quotes, if you've entered all the dates you want. \n")
		print "You typed " + input_date
		
		# Check for Enter = done
		if input_date == "done":
			print "Grabbing your data for you.."
			break

		# Check for correct format
		if TestDateFormat(input_date):
			dates.append(input_date)
			print "Ok! The list of dates to check is " + str(dates)
		else:
			print "Hmm something wrong with that date format.. try 'yyyy-mm-dd', in quotes!"
	
	# Gracefully catch name and type errors
	except NameError as e:
		print str(e)
	except TypeError as e:
		print "Hmm something wrong with that date format.. try 'yyyy-mm-dd', in quotes!"

for date in dates:
	urls.append("http://livemusicproject.org/calendar/" + date + "/")

# FIXED URLS - COMMENT OUT WHEN ACTIVATING INPUT
# urls = [
# 	"http://livemusicproject.org/calendar/2016-03-18/",
# 	"http://livemusicproject.org/calendar/2016-03-19/",
# 	"http://livemusicproject.org/calendar/2016-03-20/"
# 	]

# Create lists for performers, events
ALL_EVENTS = []
ALL_PERFORMERS = []

# Go through each URL and get data, assemble events and dump into ALL_EVENTS
for url in urls:
	# Get data from url and parse into a tree
	page = requests.get(url)
	tree = html.fromstring(page.content)

	# Extract data from tree into topic array
	EVENT_URLS = tree.xpath('//h2[@class="tribe-events-list-event-title summary"]/a/@href')
	EVENT_TITLES_RAW = tree.xpath('//h2[@class="tribe-events-list-event-title summary"]/a/text()', trim = True)
	EVENT_START_TIMES = tree.xpath('//span[@class="date-start dtstart"]//text()')
	VENUE_NAMES_RAW = tree.xpath('//span[@class="lmp-venue-name"]//text()')
	VENUE_CITIES_RAW = tree.xpath('//span[@class="lmp-wenue-city"]//text()')
	EVENT_COST = tree.xpath('//div[@class="tribe-events-event-cost"]/a/text()')
	PERFORMER_NAMES = tree.xpath('//span[@class="lmp-performer"]//text()')

	# Dump performer names into ALL_PERFORMERS
	for name in PERFORMER_NAMES:
		ALL_PERFORMERS.append(name)

	# Eliminate duplicates from ALL_PERFORMERS
	ALL_PERFORMERS = list(set(ALL_PERFORMERS))

	# Strip \n \t from titles
	EVENT_TITLES = list(map(StripNT,EVENT_TITLES_RAW))

	# Strip comma, dublicate cities and from venue city and name
	VENUE_CITIES = list(map(StripComma,VENUE_CITIES_RAW))
	VENUE_NAMES = list(map(StripComma,VENUE_NAMES_RAW))

	# Build array of html formatted events with event data 
	EVENTS = [
			[
			"<span style='font-size:13px'>",
			"<a href='",
			EVENT_URLS[i],
			"' target='_blank'><span style='font-size:18px'>",
			EVENT_TITLES[i],
			"</span></a><br />",
			EVENT_START_TIMES[i],
			"<br />",
			# Fix Seattle, Seattle condition
			(VENUE_NAMES[i] + ", " + VENUE_CITIES[i]).replace("Seattle, Seattle","Seattle"),
			"<br /><strong>",
			EVENT_COST[i],
			"</strong><br /><br /></span>"
			]
			for i in range(len(EVENT_URLS))
		]

	# Dump each event into ALL_EVENTS
	for event in EVENTS:
		ALL_EVENTS.append(event)

# Output to file

# Prepare file name
date_range_set = [date[5:] for date in dates]
date_range = " ".join(date_range_set)

filename = "LMP wknd email data (" + date_range + ").txt"
# filename = sys.argv[1]
target = open(filename,'w')

# Write performers
performers_list = ", ".join(ALL_PERFORMERS)
target.write(performers_list.encode("utf-8") + "\n\n")

# Write events
for event in ALL_EVENTS:
	event_string = "".join(event)
	target.write(event_string.encode("utf-8") + "\n\n")

# Close file
target.close()
print "All done! Your file " + filename + " awaits in the directory where this tool is saved."
print "(c) Live Music Project 2016"
print "Made by Samuel Lyon"

