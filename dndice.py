'''
Things this program needs to do:
[]	Display neat title "DnDice by sixsixseven and License MIT"
[]	Ask user for number of dice
[]	Ask user for size of dice
[]	Print the roll to the screen
'''
#	IMPORTS
import secrets



#	FUNCTIONS (Alphabetical)
def dicer():
	"""Main dice logic."""
	#	How many dice?
	h = input("How many dice? > ")
	#	What size of die?
	i = input("What size of die? > ")
	#	Return the value of each die, and the total.

def title():
	"""Prints a nifty title. But not just yet."""
	pass
	
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
dicer()