##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

#TODO: "insert or update" in peewee. If something is a dublicate, it will update entry instead of error

import pymysql
import mysql.connector
from mysql.connector import errorcode
import peewee as pw
import recordMain

print("actionRecord is now running")

myDB = pw.MySQLDatabase("gstoredata",host="gstore.cehnumckhx7r.us-east-2.rds.amazonaws.com",port=3306,user="admin",passwd="Villeneuve")

# create Base Model Record
class BaseModel(pw.Model):
    class Meta:
        database = myDB


# add another field for genre/ somekey to use in order to know where items are in store

# create Record object
class Record(BaseModel):
    album = pw.PrimaryKeyField()
    artist = pw.CharField()
    price = pw.DecimalField()
    label = pw.CharField()
    class Meta:
        table_name = 'records'

myDB.connect()
 
# add Record to database
def insert(album,artist,price,label):
    #check if fields are valid here
    res = Record.insert({
        Record.album: album,
        Record.artist: artist,
        Record.price: price,
        Record.label: label
    }).execute()
    print("Item has been added!")

# delete record from database using key: album
def delete(album):
    try:
        res = Record.get(Record.album == album)
        res.delete_instance() # returns the number of rows deleted
        print(album + " deleted")
    except:
        print("Item not found!")
   

# look for item in database using key: album
def lookup(album):
    try:
        Record.get_by_id(album)
        print("Item found!")
    except:
        print("Item not found!")



#Record.insert(album = recordMain.album, artist = recordMain.artist, price = recordMain.price, label = recordMain.label)


# #rows = cursor.execute("select * from gstoredata.records")
# #for i in range(rows):
# #result = cursor.fetchall()
# #print(result)

