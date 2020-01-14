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

print("addRecord is now running")

# try:
#     cnx = mysql.connector.connect(user='REDACTED', password='REDACTED', host='gstore.cehnumckhx7r.us-east-2.rds.amazonaws.com', database='gstoredata')

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


myDB = pw.MySQLDatabase("gstoredata",host="gstore.cehnumckhx7r.us-east-2.rds.amazonaws.com",port=3306,user="admin",passwd="Villeneuve")

#create Base Model Record
class BaseModel(pw.Model):
    class Meta:
        database = myDB


#create record object
class Record(BaseModel):
    album = pw.CharField()
    artist = pw.CharField()
    price = pw.IntegerField()
    label = pw.CharField()
    class Meta:
        table_name = 'records'

myDB.connect()


 #add records to database
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
    print(res)


#Record.insert(album = recordMain.album, artist = recordMain.artist, price = recordMain.price, label = recordMain.label)


# #rows = cursor.execute("select * from gstoredata.records")
# #for i in range(rows):
# #result = cursor.fetchall()
# #print(result)

