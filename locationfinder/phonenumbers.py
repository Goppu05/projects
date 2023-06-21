# track location and time zone using the phone number
import phonenumbers
from phonenumbers import timezonefinder
from phonenumbers import geocoder
 
number = input("Enter the phone number with country code : ")
 
# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)
 
# printing the timezone using the timezone module
timeZone = timezonefinder.time_zones_for_number(phoneNumber)
print("timezone : "+str(timeZone))
 
# printing the geolocation of the given number using the geocoder module
geolocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+geolocation)
 
# printing the service provider name using the carrier module
