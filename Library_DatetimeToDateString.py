"""

DESCRIPTION:
    takes a native python datetime object, 
    and turns it into a 'Type_Datestring' object


ARGS:
    Datetime -> python datetime object
    
RETURNS:
    Datestring -> looks like     'yyyy_mm_dd_hh_mm_ss_mmmmmm_tzn'

TESTS:
    Test_DatetimeToDateString


"""


import Library_IntegerToStringPadWithZeros

def Main(Datetime = None, Timezone = "NO_TIMEZONE_SUPPLIED"):

	DateString = ""
	DateString += Library_IntegerToStringPadWithZeros.Main(Datetime.year,           4) + "_"
	DateString += Library_IntegerToStringPadWithZeros.Main(Datetime.month,          2) + "_"
	DateString += Library_IntegerToStringPadWithZeros.Main(Datetime.day,            2) + "_"
	DateString += Library_IntegerToStringPadWithZeros.Main(Datetime.hour,           2) + "_"
	DateString += Library_IntegerToStringPadWithZeros.Main(Datetime.minute,         2) + "_"
	DateString += Library_IntegerToStringPadWithZeros.Main(Datetime.second,         2) + "_"
	DateString += Library_IntegerToStringPadWithZeros.Main(Datetime.microsecond,    6) + "_" 
	DateString += Timezone

	return DateString
