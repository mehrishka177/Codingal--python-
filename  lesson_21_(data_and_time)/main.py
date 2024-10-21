import random #importing module
import time

def getRandomDate(startDate, endDate ): #defining function
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    
    
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    sndTime = time.mktime(time.stripetime(endDate, dateFormat))
    
    
    randomTime = startTime + randomGenerator * (endTime - 
startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))
    #display resultprint("Random Date =", getRandomDate("1/1/2016", "12/12/2018"))
    
    