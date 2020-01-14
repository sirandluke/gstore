##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

import addRecord

###Datafields of a Record###
# album (string)     -> name of album
# artist (string)    -> name of artist
# price (int)        -> price of record
# label (string)     -> name of label company

###String definitions###
options = "Enter a command: insert record (a) | delete record (d) | look up record (l) | exit program (q): "
askAlbum = "Enter album name: "
askArtist = "Enter artist name: "
askPrice = "Enter price (omit '$'): "
askLabel = "Enter Label name (press ENTER if not applicable): "
confirmation = "are these datafields correct? (y/N): "
nA = "N/A"
delete = "Entry deleted!"
found = "Entry found!"
notFound = "Entry not found!"
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
				album = input(askAlbum)
				artist = input(askArtist)
				price = input(askPrice)
				label = input(askLabel)
				#convert strings to lower case
				album = album.upper()
				artist = artist.upper()
				if len(label) == 0:
					label = nA
				else:
					label = label.upper()
				print("Album: " + album)
				print("Artist: " + artist)
				print("Price: $" + price)
				print("Lablel: " + label)
				answer = input(confirmation)
			#saves changes
			changes = changes +"[" + "Album: " + album + " | Artist: " + artist + " | Price: $" + price + " | Label: " + label + "]\n"
			answer = 'N'
			addRecord.insert(album,artist,price,label) 


		if userInput == 'd':
			album = input (askAlbum)
			album = album.upper()
			#TODO
		if userInput == 'l':
			album = input (askAlbum)
			album = album.upper()
			#TODO


print(exit)
print(border)
print(changes)
print(border)

