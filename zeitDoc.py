#!/usr/bin/python
import pdfrw
import calendar
import sys
import datetime
from random import seed
from random import random
from random import randint

cal = calendar.Calendar()



#Beispielaufruf python zeitDoc.py "Meidinger, Max" 2020-10 2021-2 10

#TODO find truly random seed ?
seed(40)

class FormEntry:
    def __init__(self, date, hours):
        self.date = date
        self.hours = hours
        self.starttime = self.determineStartTime()
        self.endtime = self.determineEndTime()

    def determineStartTime(self):
        return str(randint(10, 16)) + ":00"
    
    def determineEndTime(self):
        start = self.starttime
        return start[0] + str(int(start[1]) + self.hours) + start[2:]
         

#Should fill the zeitDoc Form with given Parameters

#Arguments
#Name - String - "Max Musterman"
#Zeitraum - Begindatum bis Endedatum -> 2 Args
#Wochenstunden

#access args with sys.argv 

#init Params here
#Just with hardcoded ones for now
#defs for fieldnames



outPath = "./Docs/"
template = pdfrw.PdfReader("template.pdf")
filecount = 0

nameField = "(Name, Vorname)"
beginDateField = "(von)"
endDateField = "(bis)"
#always takes the template.pdf in the same directory


#CL Arguments
name=sys.argv[1]
startDate=sys.argv[2]
endDate=sys.argv[3]
hours=float(sys.argv[4])

startYear = int(startDate.split('-')[0])
startMonth = int(startDate.split('-')[1])
endYear = int(endDate.split('-')[0])
endMonth = int(endDate.split('-')[1])

global summe, gesTage
summe = 0
gesTage = 0

def randomHour():
    tage = 5
    avrg = hours / tage
    #currentAvrg = summe / gesTage
    return round(random() * ((avrg*2)-1))

def last_day_of_month(dateFormat):
    day = datetime.datetime.strptime(dateFormat, "%Y-%m").date()
    # this will never fail https://stackoverflow.com/questions/42950/how-to-get-the-last-day-of-the-month?page=1&tab=votes#tab-top
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)

def first_day_of_montj(dateFormat):
    return datetime.datetime.strptime(dateFormat, "%Y-%m").date()

def find_field(ident):
    fields = template.Root.AcroForm.Fields
    for field in fields:
        if(field.T == ident):
            return field

def fill_field(string, ident):
    formfield = find_field(ident)
    formfield.V = string

def clear_Fields():
    for i in range(1,14):
        fill_field( "", "(TagRow"+ str(i) + ")")
        fill_field( "", "(vonRow"+ str(i) + ")")
        fill_field( "", "(bisRow"+ str(i) + ")")
        fill_field( "", "(StundenRow"+ str(i) + ")")

def pdf_full():
    #fix for not showing value? https://github.com/pmaupin/pdfrw/issues/84
    global filecount
    annotations = template.pages[0]['/Annots']
    for annotation in annotations:
        # ... validate / update fields here
        annotation.update(pdfrw.PdfDict(AP=''))
    
    #programmlogic
    writer = pdfrw.PdfWriter()
    writer.addpages(template.pages)
    writer.write(outPath + "ZeitDocumentation" + str(filecount) + ".pdf")
    filecount += 1

    clear_Fields()

def setupPDF():
    #fill basic fields
    #Name
    fill_field(name,nameField)

def fill_row(rowNum, entry):
    fill_field( str(entry.date.day)+"."+str(entry.date.month)+"."+str(entry.date.year), "(TagRow"+ str(rowNum) + ")")
    fill_field( entry.starttime, "(vonRow"+ str(rowNum) + ")")
    fill_field( entry.endtime, "(bisRow"+ str(rowNum) + ")")
    fill_field( str(entry.hours), "(StundenRow"+ str(rowNum) + ")")

    if rowNum == 1:
        fill_field( str(entry.date.day)+"."+str(entry.date.month)+"."+str(entry.date.year), "(von)")
    
    if rowNum == 13:
        fill_field( str(entry.date.day)+"."+str(entry.date.month)+"."+str(entry.date.year), "(bis)")

    return  


def iterateMonths():
    global summe, gesTage
    counter = 1
    currentMonth = startMonth
    currentYear = startYear
    while not (currentYear == endYear and currentMonth == endMonth):
        for x in cal.itermonthdates(currentYear, currentMonth):
            if x.weekday() not in range(5,7):
                if x.month != currentMonth:
                    continue
                #TODO Randow Hour Values
                randomNum = randomHour()
                if randomNum == 0:
                    continue
                fill_row(counter, FormEntry(x, randomNum))
                summe += randomNum
                gesTage += 1
                if counter == 13:
                    counter = 0
                    pdf_full()
                counter += 1
        if currentMonth == 12:
            currentMonth = 1
            currentYear += 1
        else:
            currentMonth += 1

setupPDF()

iterateMonths()

#Set end date for last document 
entry = last_day_of_month(endDate)
fill_field(str(entry.day)+"."+str(entry.month)+"."+str(entry.year), "(bis)")

pdf_full()
print(str(filecount) + " File(s) generated!")

print("Average " + str(summe/gesTage) + " Stunden pro Tag")
        







