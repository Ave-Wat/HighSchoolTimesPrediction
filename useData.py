import csv
import sys
import interface
import matplotlib.pyplot as plt
import time

class Athlete:
    """this class organizes my data for each individual athlete"""
    
    def __init__(self, sophTime, senTime):
        self.__sophTime = sophTime
        self.__senTime = senTime
    
    def getSoph(self):
        return self.__sophTime
    
    def getSen(self):
        return self.__senTime
    
class Graph():
    """this class does all the work for my graph screen"""
    
    def __init__(self, athleteList):
        self.__athleteList = athleteList
        
    def graphingPrep(self):
        """this method prepares the .csv data for graphing. I want to plot two different things, senior times and sophomore times, the senior time above the sophomore time for each athlete. So this method returns a list of sophomore times, senior times, and a list of the number of athletes to graph"""
        sophTimes = []
        senTimes = []
        numOfAth = []
        
        i = 0
        for athlete in self.__athleteList:
            numOfAth.append(i)
            i += 1
            
            strSophT = athlete.getSoph()            
            sophTList = strSophT.split(":") #this gets minutes [0] and the seconds(and the 100ths)[1]
            sophMins = float(sophTList[0]) #this is in secs
            sophSecList = sophTList[1].split(".")  #this separates the seconds into seconds[0] and 100ths[1]
            sophSecs = float(sophSecList[0]) / 60
            sophHundredths = float(sophSecList[1]) / 10000
            
            floatSophT = sophMins + sophSecs + sophHundredths   #this is in minutes (i.e 9.5032 minutes would be 9:30.32)
            
            strSenT = athlete.getSen()
            senTList = strSenT.split(":") #this gets minutes [0] and the seconds(and the 100ths)[1]
            senMins = float(senTList[0])
            senSecList = senTList[1].split(".")  #this separates the seconds into seconds[0] and 100ths[1]
            senSecs = float(senSecList[0]) / 60
            
            senHundredths = float(senSecList[1]) / 10000
            #print(senHundredths)
            
            floatSenT = senMins + senSecs + senHundredths
            
            
            sophTimes.append(floatSophT)
            senTimes.append(floatSenT)
            
        return sophTimes, senTimes, numOfAth
    
    def plotLine(self, y1, y2, x, title = "Sophomore and Senior 3200 Times"):
        '''Plots the values in lists x and y as two dimensional points. I got this from HW 7, from a method done by Professor Oesper
        Parameters:
        x - a list of x-coordinates for the 2-d points.
        y - a list of y-coordinates for the 2-d points.  
        Should be same length as x.
        title - a string to use for the title of the figure.
        '''

        plt.plot(x,y1, 'r')
        plt.plot(x,y2, 'b')
        plt.xlabel('x values')
        plt.ylabel('Times (in Minutes)')
        if title is not None:
            plt.title(title)
        
        plt.show()
        time.sleep(10)


class Projection():
    """this class does all the work for my projection screen"""
    
    def __init__(self, athleteList):
        self.__athleteList = athleteList
        
    def findNearTimes(self, targetTime):
        """This method takes in a target time inputed by the user and converts it to a time in minutes. It then finds sophomore times near it. It saves the senior time (the athlete's outcome) corresponding with those near sophomore times. It then takes the average of the senior times and returns that as a projection. """
        
        targetList = targetTime.split(":")
        targetMins = float(targetList[0])
        targetFloat = None
        if "." in targetList[1]:
            targetSecList = targetList[1].split(".")
            targetSecs = float(targetSecList[0]) / 60
            targetHundos = float(targetSecList[1]) / 10000
            targetFloat = targetMins + targetSecs + targetHundos
        else:
            targetSecs = float(targetList[1]) / 60
            targetFloat = targetMins + targetSecs
        
        
        nearSophTimes = []
        correspSenTimes = []
        
        for athlete in self.__athleteList:
            strSophT = athlete.getSoph()            
            sophTList = strSophT.split(":") #this gets minutes [0] and the seconds(and the 100ths)[1]
            sophMins = float(sophTList[0]) #this is in secs
            sophSecList = sophTList[1].split(".")  #this separates the seconds into seconds[0] and 100ths[1]
            sophSecs = float(sophSecList[0]) / 60
            sophHundredths = float(sophSecList[1]) / 10000
            
            floatSophT = sophMins + sophSecs + sophHundredths   #this is in minutes (i.e 9.5032 minutes would be 9:30.32)
            
            if floatSophT > targetFloat - (5 / 60) and floatSophT < targetFloat + (5 / 60):
                nearSophTimes.append(floatSophT)
                
                strSenT = athlete.getSen()
                senTList = strSenT.split(":") #this gets minutes [0] and the seconds(and the 100ths)[1]
                senMins = float(senTList[0])
                senSecList = senTList[1].split(".")  #this separates the seconds into seconds[0] and 100ths[1]
                senSecs = float(senSecList[0]) / 60
                senHundredths = float(senSecList[1]) / 10000
                floatSenT = senMins + senSecs + senHundredths
                
                correspSenTimes.append(floatSenT)
        i = 0
        total = 0
        for time in correspSenTimes:
            i += 1
            total += time
        
        avg = total / i
        
        prettyFormat = str(avg).split(".")
        minutes = prettyFormat[0]
        sec = str(float("." + prettyFormat[1]) * 60)
        
        projectedTime = minutes + ":" + sec
        return projectedTime
    
def collectTimes():
    
    athleteList = []
    
    with open("times.csv", 'r') as file:
        next(file)
        
        for line in file:
            line = line.rstrip()
            times = line.split(",")
            athlete = Athlete(times[0],times[1])
            athleteList.append(athlete)
    file.close()
    return athleteList

            
def main():
    athleteList = collectTimes()
    
    textInterface = interface.TextTimesInterface()
    
    option = textInterface.intro()
    
    if option == "0":
        if textInterface.graphScreen(athleteList):
            plt.close()
    
    if option == "1":
        textInterface.projectionOption(athleteList)
        
    
    
if __name__ == "__main__":
    main()