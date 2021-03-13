#FUNCTION IMPORT LIST
#   csv is built in
import csv

#Define the directory here relative to where this file is stored
monthlyStatementDirectory = "DETAILS/monthlyStatement.csv"
paymentDirectory = "DETAILS/database.csv"

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