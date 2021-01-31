"""
Date Started: Jan 11th 2021
Author : Naveen Kumar Xavier
Last Update: Jan 31st 2021
"""
import sqlite3

imagefile = open(r"D:\Code\image_search.jpg", "rb") #Enter your path here with image file name
#Binary data of image file
matcher = imagefile.read()
#for temperory usage
flag = 0

try:
    conn = sqlite3.connect(r"D:\Code\database.db")
    print("DB connection success")
except:
    print("Some error occurred")

sql = 'SELECT * FROM `images`'
temp = conn.execute(sql)
results = temp.fetchall() #SQL query results are stored in 'results'

for rows in range(len(results)):
    
    if results[rows][2] == matcher:
    #In my database the image BLOB data are available in Second column of the table
        flag = 1
        print(rows)
        print(results[rows][0])
        break
    else:
        print("No match found")
    rows = rows+1
print("Flag value is", flag)
    
if flag == 1:
    print("Match found - Check the log prints")

else:
    print("Mission Failed")

