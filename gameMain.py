##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

import addGame

###Datafields of a Game###
# title (string)     -> name of game
# console (string)   -> name of console
# price (int)        -> price of game
# dev (string)       -> name of game developer
# publisher (string) -> name of publishing company

###text file format for bulk insert###
# b -> specify bulk insert insert
# game name 
# console name
# price 
# developer name
# publisher name ('na' if not available)
# q -> when done

###String definitions###
options = "Enter a command: insert game (a) | delete game (d) | look up game (l) | exit program (q): "
askTitle = "Enter game name: "
askConsole = "Enter console name: "
askPrice = "Enter price (omit '$'): "
askDeveloper = "Enter developer name: "
askPublisher = "Enter publisher name (press ENTER if not applicable): "
confirmation = "are these datafields correct? (y/N): "
delete = "Entry deleted!"
found = "Entry found!"
notFound = "Entry not found!"
nA = "N/A"
exit = "\n\n\n***ADDITION(S)***\n"
changes = ""
border = "----------------------------------------------------------------------\n"

# allows the program to begin
userInput = 'a'
answer = 'N'
print("***FOR G-STORE MEMBER USE ONLY***")

# continues to execute as long as user makes inputs
if __name__ == "__main__":
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
			addGame.insert(title,console,price,developer,publisher) 

		if userInput == 'd':
			title = input(askTitle)
			title = title.upper()
			#deleteGame()
			#TODO

		if userInput == 'l':
			title = input(askTitle)
			title = title.upper()
			#lookupGame()
			#TODO
		if userInput == 'b':
			title = input(askTitle).upper()
			console = input(askConsole).upper()
			price = input(askPrice)
			developer = input(askDeveloper).upper()
			publisher = input(askPrice)
			if publisher == 'na':
				publisher = nA
			else:
				publisher = publisher.upper()
			changes = changes +"[" + "Title: " + title + " | Console: " + console + " | Price: $" + price + " | Developer: " + developer + " | Publisher: " + publisher + "]\n"
			addGame.insert(title,console,price,developer,publisher) 
	print(exit)
	print(border)
	print(changes)
	print(border)

	

