#FUNCTION IMPORT LIST
#   csv is built in
import csv
#   datetime is built in
from datetime import date
from datetime import datetime

#Define the directory here relative to where this file is stored
monthlyStatementDirectory = "DETAILS/monthlyStatement.csv"
paymentDirectory = "DETAILS/database.csv"

#ENTER NAME
username = str("J. Sykes")


with open(paymentDirectory, 'r') as t1, open(monthlyStatementDirectory, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.txt', 'w') as outFile:
    outFile.write("\nThese entries were not found in the database: \n \t")
    for line in filetwo:
        if line not in fileone:
            outFile.write(line + "\t")

    outFile.write("\nThese entries were successfully found in the database: \n \t")
    for line in filetwo:
        if line in fileone:
            outFile.write(line + "\t")

    outFile.write("\n########################################\n ")
    outFile.write("\nThese are the entries which were tested:\n \t")
    for line in filetwo:
        outFile.write(line + "\t")
    

    outFile.write("\n########################################\n\n\n ")
    today = date.today()
    theDate = today.strftime("%d %B %Y")

    now = datetime.now()
    dt_string = str(now.strftime("%H:%M:%S"))
    metaData = str("\n This report was generated on: "+ theDate +" at "+ dt_string + " by " + username + " with software created by Joe Sykes")
    outFile.write(metaData)