# Program reads an input of a day from the User and then Returns the Spanish Equivalent of the same
# Using the time library to make a small delay in order to make the user something is really happening

import time


day = raw_input("Enter a Day in English (Example: Sunday) :")

print(" Reading your Input and Processing Please wait... ")

for i in range (1,10):

	print("#")
	time.sleep(.5)

#convert the input data into lower case
day= day.lower()

if day == "sunday":
	print("Domingo is the Spanish Equivalent")
	
elif day == "monday":
	print("Lunes is the Spanish Equivalent")

elif day == "tuesday":
	print("Martes is the Spanish Equivalent")

elif day == "wednesday":
	print("Miercoles is the Spanish Equivalent")

elif day == "thursday":
	print("Jueves is the Spanish Equivalent")

elif day == "friday":
	print("Vrnes is the Spanish Equivalent")

elif day == "saturday":
	print("Sabado is the Spanish Equivalent")

