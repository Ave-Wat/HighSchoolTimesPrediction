# want option to graph or enter sophomore time in first pane (use buttons)
# in graph pane, use matplotlib to graph the data
# in projected time pane, have a space to input a time

import sys
import useData

try: 
    import graphics 
except ImportError:
    sys.stderr.write("Couldn't import graphics.py module.\n") 
    sys.stderr.write("You should make sure that graphics.py" +
                                " is in the correct directory.\n")

class TextTimesInterface:
    
    def __init__(self):
        """"""     
    
    def intro(self):
        """this method asks the user in the terminal if they want to see the graph or make a projection. It returns 0 if graphing, 1 projecting"""
        
        option = input("Type 0 to graph the data or 1 to make a 3200 projection: ")
        
        return option
    
    def graphScreen(self, athList):
        """this method pulls up a screen to graph the data"""
        
        newGraph = useData.Graph(athList)
        sophTimes, senTimes, numOfAth = newGraph.graphingPrep()
        newGraph.plotLine(sophTimes, senTimes, numOfAth)
           
        
    def projectionOption(self, athList):
        """this screen gets user input to spit back out a projected time"""
        
        time = input("input a sophomore time to project: ")
        project = useData.Projection(athList)
        print(project.findNearTimes(time))

        

    