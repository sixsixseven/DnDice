#	IMPORTS
import secrets
import os



#	FUNCTIONS (Alphabetical)
def clear():
	"""Clears the display buffer and resets the title. Better GUI."""
	os.system('clear')
	title()

def dicer():
	"""Main dice logic. Accepts no arguments."""
	looper = True
	while looper:
		looper = False
		clear()
		dice = []
		total = 0
		looper = True

		#	How many dice, and what size? And;
		#	Roll, increment the total, then append the value of each die into 'dice'.
		h = input("How many dice? (1 - 1000) > ")
		if h.isdigit() == True and int(h) >= 1 and int(h) <= 1000:
			i = input("What size of die? 1 - 1000) > ")
			if i.isdigit() == True and int(i) >= 1 and int(i) <= 1000:
				for count in range(int(h)):
					roll = secrets.randbelow(int(i)) + 1	#	The +1 moves the index away from 0 and into the range we specify.
					total += roll
					dice.append(roll)

				print(f"\nYou rolled the following: {h}d{i}")
				#	Make conditional print here, if len(dice) == 1, then print "The face of your die reads:"
				print(f"The face(s) of your dice read: {str(dice)[1:-1]}")
				print(f"The total of your dice are: {total}\n")
				looper = False
			else:
				print(input("Your die size was outside the allowable range. Press Return to try again."))	
				looper = True
		else:
			print(input("Your dice count was outside the allowable range. Press Return to try again."))
			looper = True


def title():
	"""Prints a nifty title. But not just yet."""
	print(" ____        ____  _          ")
	print("|  _ \\ _ __ |  _ \\(_) ___ ___ ")
	print("| | | | '_ \\| | | | |/ __/ _ \\")
	print("| |_| | | | | |_| | | (_|  __/")
	print("|____/|_| |_|____/|_|\\___\\___|")
	print("by: sixsixseven\t  License: MIT\n")                               
	
def yesno(i):
	"""Handles yes/no logic. Accepts exactly 1 string argument in the
	form of a yes/no question."""
	x = input(f"{i}	Y/N > ").lower()
	
	yeslist = ["y", "yes", "ye", "yea", "yeah"]
	nolist = ["n", "no", "na", "nah", "nope"]

	if x in yeslist:
		return True
	elif x in nolist:
		return False
	else:
		return yesno(i)


#	MAIN
gamestate = True

while gamestate == True:
	title()
	dicer()
	gamestate = yesno("Would you like to roll more?")