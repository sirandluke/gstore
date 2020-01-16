##########
# author: Luke Sirand
# Intended for use at The General Store Cooperative UCSD
#########

#TODO: IMPORT USER INPUT FROM MAIN!!!!

#TODO: "insert or update" in peewee. If something is a dublicate, it will update entry instead of error

import pymysql
import mysql.connector
from mysql.connector import errorcode
import peewee as pw
import recordMain

print("actionRecord is now running")

# try:
#     cnx = mysql.connector.connect(user='#', password='#', host='#', database='#')

# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#   cnx.close()    

# cursor = cnx.cursor()


myDB = pw.MySQLDatabase("gstoredata",host="#",port=#####,user="###",passwd="####")

# create Base Model Record
class BaseModel(pw.Model):
    class Meta:
        database = myDB


# create Record object
class Record(BaseModel):
    album = pw.PrimaryKeyField()
    artist = pw.CharField()
    price = pw.IntegerField()
    label = pw.CharField()
    class Meta:
        table_name = 'records'

myDB.connect()


 # add Record to database
def insert(album,artist,price,label):
    print("inserting")
    #check if fields are valid here
    res = Record.insert({
        Record.album: album,
        Record.artist: artist,
        Record.price: price,
        Record.label: label
    }).execute()
    print("Item has been added!")

#delete record from database
def delete(album):
    print("deleting")
    res = Record.get_by_id(album)
    if (res == album):
        print(res)
        res.delete_instance()
    else:
        print("Item not found!")

def lookup(album):
    print("searching")
    res = Record.get_by_id(album)
    print(res)
    if (res == album):
        print("Item found!")
    else:
        print("Item not found!")



#Record.insert(album = recordMain.album, artist = recordMain.artist, price = recordMain.price, label = recordMain.label)


# #rows = cursor.execute("select * from gstoredata.records")
# #for i in range(rows):
# #result = cursor.fetchall()
# #print(result)

