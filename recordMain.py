##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

###Datafields of a Record###
# album (string)     -> name of album
# artist (string)    -> name of artist
# price (int)        -> price of record
# publisher (string) -> name of publishing company

###String definitions###
options = "Enter a command: insert record (a) | delete record (d) | look up
record (l) | exit program (q): "
askAlbum = "Enter album name: "
askArtist = "Enter artist name: "
askPrice = "Enter price (omit '$'): "
askPublisher = "Enter publisher name (press ENTER if not applicable): "
confirmation = "are these datafields correct? (y/N)"
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
while (userInput != 'q'):##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

###Datafields of a Record###
# album (string)     -> name of album
# artist (string)    -> name of artist
# price (int)        -> price of record
# publisher (string) -> name of publishing company

###String definitions###
options = "Enter a command: insert record (a) | delete record (d) | look up record (l) | exit program (q): "
askAlbum = "Enter album name: "
askArtist = "Enter artist name: "
askPrice = "Enter price (omit '$'): "
askPublisher = "Enter publisher name (press ENTER if not applicable): "
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
while (userInput != 'q'):
	userInput = input(options)

	if userInput == 'a':
		while(answer == 'N'):
			#ask user for datafields
			album = input(askAlbum)
			artist = input(askArtist)
			price = input(askPrice)
			publisher = input(askPublisher)
			#convert strings to lower case
			album = album.upper()
			artist = artist.upper()
			if len(publisher) == 0:
				publisher = nA
			else:
				publisher = publisher.upper()
			print("Album: " + album)
			print("Artist: " + artist)
			print("Price: $" + price)
			print("Publisher: " + publisher)
			answer = input(confirmation)
		#saves changes
		changes = changes +"[" + "Album: " + album + " | Artist: " + artist + " | Price: $" + price + " | Publisher: " + publisher + "]\n"
		answer = 'N'

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


	userInput = input(options)

	if userInput == 'a':
		while(answer == 'N'):
			#ask user for datafields
			album = input(askAlbum)
			artist = input(askArtist)
			price = input(askPrice)
			publisher = input(askPublisher)
			#convert strings to lower case
			album = album.upper()
			artist = artist.upper()
			if len(publisher) == 0:
				publisher = nA
			else:
				publisher = publisher.upper()
			print("Album: " + album)
			print("Artist: " + artist)
			print("Price: $" + price)
			print("Publisher: " + publisher)
			answer = input(confirmation)
		#saves changes
		changes = changes +"[" + "Album: " + album + " | Artist: " + artist + " | Price: $" + price + " | Publisher: " + publisher + "]\n"
		answer = 'N'

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

