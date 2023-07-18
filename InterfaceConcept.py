from tkinter import *
from tkinter import ttk
import time
import win32api


###################################
##### GUI setup and functions #####
###################################
class GUI:
    def __init__(self):
        pass

    def genWindow(self,visuals):
        self.fullScreen = visuals[2]

        self.window = Tk(className='Profielwerkstuk')
        self.window.attributes('-fullscreen', self.fullScreen)
        self.frm = ttk.Frame(self.window, padding=10)
        self.frm.grid()
        #button = Button(self.window,
        #    text="Quit",
        #    width=25,
        #    height=5,
        #    fg='white',  # Set the text color to white
        #    bg='red',  # Set the background color to black
        #    command=quit
        #).grid(column=99, row=99)

    def addLabel(self,inText,gridPos,visuals):
        self.showText = inText
        self.gridCollumn = gridPos[0]
        self.gridRow = gridPos[1]

        self.bgndColor = visuals[0]
        self.fgndColor = visuals[1]

        label = Label(self.window,
            text=self.showText,
            fg=self.fgndColor,  # Set the text color to white
            bg=self.bgndColor  # Set the background color to black
        ).grid(column=self.gridCollumn, row=self.gridRow)

    def addButton(self,inText,gridPos,funcToRun,visuals):
        self.showText = inText
        self.gridCollumn = gridPos[0]
        self.gridRow = gridPos[1]
        self.execFunc = funcToRun

        self.bgndColor = visuals[0]
        self.fgndColor = visuals[1]

        button = Button(self.window,
            text=self.showText,
            width=25,
            height=5,
	        command=self.execFunc,
            fg=self.fgndColor,  # Set the text color to white
            bg=self.bgndColor  # Set the background color to black
        ).grid(column=self.gridCollumn, row=self.gridRow)

    def updt(self):
        self.window.update()

    def show(self):
        self.window.mainloop()

############################################
##### General Functions for all setups #####
############################################
def measDis(dur):
    print('Taking new measurement...')

    ## Begin of (distance) measurement code
    #   The measurement needs to output a 2D matrix, X-axis data on the first row, Y-axis data on the second

    time.sleep(dur) #Measurement time placeholder
    dat = [[10,9,8,7,6,5],[1,2,3,4,5,6]] #Measurement data placeholder

    ## End of measurement code

    print('Measurement done')
    return dat

def plotDis(dis):
    print('Printing distance measurement onto terminal...')
    print('\n Y-axis')
    print(dis[0])
    print('\n X-axis')
    print(dis[1])

    print('\n Plotting distance measurement...')
    # Plot the (distance) measurement from here
    # The measurement data is a 2D matrix, X-axis data on the first row, Y-axis data on the second
    # !!! Do not use the command below for actual code, it will crash the programm when used incorrectly with Tkinter !!!
    win32api.MessageBox(0, 'The plotted data will be shown here probably', 'Measurement data')

def passFunc():
    pass

#########################################
##### All functions for setup 1 --> #####
#########################################
def setup1():
    visuals[0:2] = stdVisuals[3:5]
    mainScreen.addButton("Taking measurement...",[1,0],passFunc,visuals)
    mainScreen.updt()

    ## Simple example for measurement
    dis = measDis(2)
    visuals[0] = 'yellow'
    mainScreen.addButton("Data plot shown",[1,0],passFunc,visuals)
    plotDis(dis)

    visuals[0:2] = stdVisuals[0:2]
    mainScreen.addButton("Setup 1 start",[1,0],setup1,visuals)

#########################################
##### All functions for setup 2 --> #####
#########################################
def setup2():
    visuals[0:2] = stdVisuals[3:5]
    mainScreen.addButton("Taking measurement...",[2,0],passFunc,visuals)
    mainScreen.updt()

    ## Simple example for measurement
    dis = measDis(2)
    plotDis(dis)

    visuals[0:2] = stdVisuals[0:2]
    mainScreen.addButton("Setup 2 start",[2,0],setup2,visuals)


##########################################################################
##### Changes in the interface colors etc only to be done below here #####
##########################################################################

#Visuals
#  [STR:  Standard background color
#   STR:  Standard text color
#   BOOL: Full screen mode
#   STR:  Button pressed background color
#   STR:  Button pressed text color
#   }

stdVisuals = ['grey','black',False,'green','white']


#############################################################################
##### Changes in what shows on the interface only to be done below here #####
#############################################################################

visuals = stdVisuals[0:6]

mainScreen = GUI()
mainScreen.genWindow(visuals)
mainScreen.addLabel("greatest interface",[0,0],visuals)
mainScreen.addButton("Setup 1 start",[1,0],setup1,visuals)
mainScreen.addButton("Setup 2 start",[2,0],setup2,visuals)
mainScreen.addButton("Setup 3 start",[3,0],setup2,visuals)
mainScreen.show()

