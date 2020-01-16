##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

#TODO: "insert or update" in peewee. If something is a dublicate, it will update entry instead of error

import pymysql
import mysql.connector
import peewee as pw
import gameMain

print("addGame is now running")

myDB = pw.MySQLDatabase("gstoredata",host="gstore.cehnumckhx7r.us-east-2.rds.amazonaws.com",port=3306,user="admin",passwd="Villeneuve")

#create Base Model Game
class BaseModel(pw.Model):
    class Meta:
        database = myDB


# create Game object
class Game(BaseModel):
    title = pw.CharField()
    console = pw.CharField()
    price = pw.IntegerField()
    developer = pw.CharField()
    publisher = pw.CharField()
    class Meta:
        table_name = 'games'

myDB.connect()


 # add Game to database
def insert(title,console,price,developer,publisher):
    print("inserting")
    #check if fields are valid here
    res = Game.insert({
        Game.title: title,
        Game.console: console,
        Game.price: price,
        Game.developer: developer,
        Game.publisher: publisher
    }).execute()
    print("Item has been added!")


#Record.insert(album = recordMain.album, artist = recordMain.artist, price = recordMain.price, label = recordMain.label)


# #rows = cursor.execute("select * from gstoredata.records")
# #for i in range(rows):
# #result = cursor.fetchall()
# #print(result)

