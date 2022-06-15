
import sys
import zeitDoc
import datetime
from calendar import monthrange

def processCommandLineARGS():
    global name, hours, startDate, endDate

    name = sys.argv[1]
    startDateString = sys.argv[2]
    endDateString = sys.argv[3]
    hours = float(sys.argv[4])

    startYear = int(startDateString.split('-')[0])
    startMonth = int(startDateString.split('-')[1])
    endYear = int(endDateString.split('-')[0])
    endMonth = int(endDateString.split('-')[1])

    startDate = datetime.datetime(startYear, startMonth, 1)
    endDate = datetime.datetime(endYear, endMonth, monthrange(endYear,endMonth)[1])


def main():
    processCommandLineARGS()
    zeitDoc.start(name,hours,startDate, endDate)

main()

#Beispielaufruf python zeitDoc.py "Meidinger, Max" 2020-10 2021-2 10

#TODO Use Normal Distribution Random Number

#TODO Make input dependent on hours/month not week

#TODO exclude holidays

