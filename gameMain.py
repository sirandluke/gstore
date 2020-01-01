##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

###Datafields of a Game###
# title (string)     -> name of game
# console (string)   -> name of console
# price (int)        -> price of game
# dev (string)       -> name of game developer
# publisher (string) -> name of publishing company

###String question definitions###
options = "Enter a command: insert game (a) | exit program (q): "
askTitle = "Enter game name: "
askConsole = "Enter console name: "
askPrice = "Enter price (omit '$'): "
askDeveloper = "Enter developer name: "
askPublisher = "Enter publisher name (press ENTER if not applicable): "
confirmation = "are these datafields correct? (y/N)"
nA = "N/A"
exit = "\n\n\n***ADDITION(S)***\n"
changes = ""
border = "----------------------------------------------------------------------\n"

# allows the program to begin
userInput = 'a'
answer = 'N'
print("***FOR G-STORE MEMBER USE ONLY***")

# continues to execute as long as user makes inputs
while (userInput != 'q'):
	userInput = input(options)
	if userInput == 'a':
		while(answer == 'N'):
			#ask user for datafields
			title = input(askTitle)
			console = input(askConsole)
			price = input(askPrice)
			developer = input(askDeveloper)
			publisher = input(askPublisher)

			#convert strings to lower case
			title = title.upper()
			console = console.upper()
			developer = developer.upper()
			if len(publisher) == 0:
				publisher = nA
			else:
				publisher = publisher.upper()
			print("Title: " + title)
			print("Console: " + console)
			print("Price: $" + price)
			print("Developer: " + developer)
			print("Publisher: " + publisher)
			answer = input(confirmation)

		#saves changes
		changes = changes +"[" + "Title: " + title + " | Console: " + console + " | Price: $" + price + " | Developer: " + developer + " | Publisher: " + publisher + "]\n"
		answer = 'N'

print(exit)
print(border)
print(changes)
print(border)

