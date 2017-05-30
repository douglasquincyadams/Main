import Library_DatetimeToDateString
import datetime
import pytz


#TODO -> need to not use current time
#TODO -> need to check some different timezones against the output
CurrentDateTime = datetime.datetime.utcnow()
#utc = pytz.timezone('GMT')
#CurrentDateTimeGMT = CurrentDateTime.astimezone(utc)

DateString =  Library_DatetimeToDateString.Main(CurrentDateTime, "GMT")
print DateString
