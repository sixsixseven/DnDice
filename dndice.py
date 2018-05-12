'''
Things this program needs to do:
[]	Display neat title "DnDice by sixsixseven and License MIT"
[]	Ask user for number of dice
[]	Ask user for size of dice
[]	Print the roll to the screen
'''
#	IMPORTS
import secrets
import os



#	FUNCTIONS (Alphabetical)
def clear():
	"""Clears the display buffer and resets the title. Better GUI."""
	os.system('clear')
	title()

def dicer():
	"""Main dice logic."""
	clear()
	dice = []
	total = 0
	#	How many dice, and what size?
	h = input("How many dice? > ")
	i = input("What size of die? > ")
	#	Roll, increment the total, then append the value of each die into 'dice'.
	for count in range(int(h)):
		roll = secrets.randbelow(int(i)) + 1	#	The +1 moves the index away from 0.
		total += roll
		dice.append(roll)

	rollAverage = sum(dice)/len(dice)
	print(f"\nYou rolled the following: {h}d{i}")
	print(f"The face(s) of your dice read: {str(dice)[1:-1]}")
	print(f"The total of your dice are: {total}\n")


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