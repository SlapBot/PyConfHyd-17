from sounder import Sounder

dataset = [
  ["SystemModule@MeaningOfLife", ["meaning", "life"]],
  ["SystemModule@TimeRightNow",["time","right","now"]],
  ["SystemModule@DateToday",["date","today"]],
  ["SystemModule@WakeUp",["wake","up"]],
  ["SystemModule@GoToSleep",["go","sleep"]],
  ["SystemModule@Quit",["youre","fired"]],
  ["SystemModule@TellSystemStatus",["system","status"]],
  ["AlphaSearchModule@DoASearch",["alpha","search"]],
  ["WikipediaModule@GiveASummary",["information","wikipedia"]],
  ["MovieInformationModule@GiveSomeInformation",["movie","information"]],
  ["WeatherReportModule@WeatherReportToday",["weather","today"]],
  ["WeatherReportModule@WeatherReportTomorrow",["weather","forecast","tomorrow"]],
  ["WeatherReportModule@WeatherReportWeekly",["weather","forecast","week"]],
  ["TwitterModule@GetTrending",["trending","twitter"]],
  ["TwitterModule@StatusUpdate",["tweet","something","twitter"]],
  ["TwitterModule@GetNotifications",["twitter","notifications"]],
  ["EvernoteModule@WriteNote",["note","something"]],
  ["GoogleCalendarModule@AddEvent",["add","calendar","event"]],
  ["GoogleCalendarModule@GetEventsToday",["calendar","events","today"]],
  ["GoogleCalendarModule@GetEventsTomorrow",["calendar","events","tomorrow"]],
  ["GmailModule@handle",["unread","emails"]],
  ["ReporterModule@GetNews",["get","news","detailed"]],
  ["ReporterModule@handle",["read","latest","news"]],
  ["FootballModule@handle",["football","information"]],
  ["FacebookModule@GetBirthdayReminders",["birthday","reminders"]],
  ["FacebookModule@StatusUpdate",["facebook","status","update"]],
  ["ZomatoModule@handle",["feeling","hungry","restaurant"]]
]

print("\n")

print("Kindly input your command.")

print("\n")

user_string = input()

print("\n")

print("Your command: %s" % user_string)

key_words_array = []
for a in dataset:
	key_words_array.append(a[1])

s = Sounder(key_words_array)

def get_user_words_array(user_string):
	user_array = user_string.split()
	for user_word in user_array:
		if user_word in s.get_reserved_sub_words():
			user_array.remove(user_word)
	return user_array

user_keywords = get_user_words_array(user_string)

print("\n")

index = s.search(user_keywords)
print("Intent Predicted: %s" % dataset[index])

print("\n")

status = s.probability(user_keywords, prediction=True)
print("Status Report: %s" % status)

# https://goo.gl/HZfTWF


print("\n")