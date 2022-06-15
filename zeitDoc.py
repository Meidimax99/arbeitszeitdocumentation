#!/usr/bin/python

import calendar
import datetime
import form
from random import seed
from random import random
from random import randint

cal = calendar.Calendar()



seed(40)

class WorkTime:
    #Constructor
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

#A Object of the Class TimeDocumention represents a List of WorkTimes
#
class TimeDocumentation:
    def __init__(self, name):
        self.name = name
        self.workDates = []
        #TODO Needs more metrics here!!!
        self.overallHours = 0
        #self.avrgMonthlyHours = 0
        self.daysWorked = 0

    #TODO Problem: More dates are added to a month in which all hours are already worked
        # Simple approach: Just count hours worked in the month and stop adding dates after the maximum is reached
        # Better: Randomize how the hours are added, skip some days, etc and draw workhours from a normal distribution

    def addDates(self, monthlyHours, startDate, endDate):

        #TODO Count actual work days in the time period, excluding local holidays
        daily_work_hours = monthlyHours / (4*5)

        currentHours = 0

        currentMonth = startDate.month
        currentYear = startDate.year
        #Iterate through specified period month by month
        while not (currentYear == endDate.year and currentMonth == endDate.month + 1):
            #iterate through a month day by day
            for x in cal.itermonthdates(currentYear, currentMonth):
                #Is the day not on a weekend
                if x.weekday() not in range(5, 7):
                    #Iteration through month days can include edge days, like the first of the next month etc ...
                    if x.month != currentMonth:
                        continue
                    self.workDates.append(WorkTime(x,daily_work_hours))
                    currentHours += daily_work_hours
                    if currentHours >= monthlyHours:
                        currentHours = 0
                        break

            if currentMonth == 12:
                currentMonth = 1
                currentYear += 1
            else:
                currentMonth += 1


#TODO split iterate function up:
    def _iterateYear(self):
        pass
    def iterateMonth(self,year,month):
        pass

    def generatePDF(self):
        form.setUp(self.name)
        for entry in self.workDates:
            form.addEntry(entry)

    def printMetrics(self):
        print("Hours Worked: ",self.overallHours, "Days worked: ", self.daysWorked)

    def generateMetrics(self):
        self.daysWorked = len(self.workDates)
        self.overallHours = 0
        for entry in self.workDates:
            self.overallHours += entry.hours


def last_day_of_month(dateFormat):
    day = datetime.datetime.strptime(dateFormat, "%Y-%m").date()
    # this will never fail https://stackoverflow.com/questions/42950/how-to-get-the-last-day-of-the-month?page=1&tab=votes#tab-top
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)



#setupPDF()

#iterateMonths()

#Set end date for last document 
#entry = last_day_of_month(endDate)
#fill_field(str(entry.day)+"."+str(entry.month)+"."+str(entry.year), "(bis)")

#pdf_full()
#print(str(filecount) + " File(s) generated!")

#print("Filled in " + summe + " Hours")
def start(name,hours,startDate, endDate):
    print("Process init with params: \n",name,hours,startDate, endDate)
    timeDoc = TimeDocumentation(name)
    timeDoc.addDates(hours,startDate,endDate)
    timeDoc.generateMetrics()
    timeDoc.printMetrics()
    timeDoc.generatePDF()


        







