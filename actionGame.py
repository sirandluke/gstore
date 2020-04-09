##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

# TODO: "insert or update" in peewee. If something is a dublicate, it will update entry instead of error

import pymysql
import mysql.connector
import peewee as pw
import gameMain

print("actionGame is now running")

myDB = pw.MySQLDatabase("gstoredata",host="***",port=3306,user="***",passwd="***")

#create Base Model Game
class BaseModel(pw.Model):
    class Meta:
        database = myDB

# create Game object
class Game(BaseModel):
    gameId = pw.AutoField
    title = pw.CharField()
    console = pw.CharField()
    price = pw.DecimalField() # DECIMAL(5,2) i.e. (4 -> 4.00)
    developer = pw.CharField()
    publisher = pw.CharField()
    class Meta:
        #constraints = CompositeKey('title', 'console')
        table_name = 'games'


myDB.connect()


 # add Game to database
def insert(title,console,price,developer,publisher):
    print("inserting " + title)
    res = Game.insert({
        Game.title: title,
        Game.console: console,
        Game.price: price,
        Game.developer: developer,
        Game.publisher: publisher
    }).execute()
    print("Item has been added!")

# delete record from database using key: title
def delete(title,console):
        # get the row and delete
        #res = Game.get_by_id(title).where(Game.console == console)
        if( Game.delete().where(Game.title == title).where(Game.console == console).execute() != 1):
            print(title + " not found!")
        else:
            print(title + " deleted")
   

# look for item in database using key: title
def lookup(title):
    #try:
        # get rows with title
        cursor = myDB.cursor()
        rows = cursor.execute("select * from gstoredata.records").where(Game.title == title)
        for i in range(rows):
            print(rows)

        """ 
        res = Game.get(Game.title == title)
        title = res.title 
        console = res.console
        price = res.price
        developer = res.developer
        publisher = res.publisher
        # print the items
        print('\n' + "*Item Found*")
        print("title: " + title)
        print("console: " + console)
        print("Price: $" + str(price))
        print("Developer: $" + developer)
        print("Publisher: " + publisher + '\n')
        #lst = [Record.album, Record.artist, Record.price, Record.label]
        #print(User.select(*lst))
        ##print(album + " found!")
    except:
        print(title + " not found!")
    """

myDB.close()


#Record.insert(album = recordMain.album, artist = recordMain.artist, price = recordMain.price, label = recordMain.label)


# #rows = cursor.execute("select * from gstoredata.records")
# #for i in range(rows):
# #result = cursor.fetchall()
# #print(result)

