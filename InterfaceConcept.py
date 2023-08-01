from tkinter import *
from tkinter import ttk
import time

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
matplotlib.rcParams['toolbar'] = 'None'
if matplotlib.get_backend() == 'Qt5Agg':
    from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
    def _update_buttons_checked(self):
        # sync button checkstates to match active mode (patched)
        if 'pan' in self._actions:
            self._actions['pan'].setChecked(self._active == 'PAN')
        if 'zoom' in self._actions:
            self._actions['zoom'].setChecked(self._active == 'ZOOM')
    NavigationToolbar2QT._update_buttons_checked = _update_buttons_checked

###################################
##### GUI setup and functions #####
###################################
class GUI:
    def __init__(self):
        pass

    def genWindow(self,visuals,windowName):
        self.fullScreen = visuals[2]

        self.window = Tk(className=windowName)
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

    def addUserEntry(self,inText,gridPos,visuals):
        self.showText = inText
        self.gridCollumn = gridPos[0]
        self.gridRow = gridPos[1]

        self.bgndColor = visuals[0]
        self.fgndColor = visuals[1]

        value = Entry(self.window,
            text=self.showText,
            #width=25,
            #height=5,
	        #command=self.execFunc,
            fg=self.fgndColor,  # Set the text color to white
            bg=self.bgndColor  # Set the background color to black
        ).grid(column=self.gridCollumn, row=self.gridRow)
        return value

    def addGraph(self,X1,X2,X3,time,visuals):
        #self.showText = inText
        #self.gridCollumn = gridPos[0]
        #self.gridRow = gridPos[1]

        self.bgndColor = visuals[0]
        self.fgndColor = visuals[1]

        fize = (8,3)

        f1 = Figure(figsize=fize, dpi=70)
        x1 = f1.add_subplot(111)
        x1.set_title('Position')
        x1.set_ylabel('Mass position [m]')
        x1.set_xlabel('Time [s]')
        x1.plot(time,X1)
        f2 = Figure(figsize=fize, dpi=70)
        x2 = f2.add_subplot(111)
        x2.set_title('Velocity')
        x2.set_ylabel('Mass velocity [m/s]')
        x2.set_xlabel('Time [s]')
        x2.plot(time,X2)
        f3 = Figure(figsize=fize, dpi=70)
        x3 = f3.add_subplot(111)
        x3.set_title('Acceleration')
        x3.set_ylabel('Mass acceleration [m/s^2]')
        x3.set_xlabel('Time [s]')
        x3.plot(time,X3)

        #x2 = f.add_subplot(312)
        #x2.set_title('Velocity')
        #x2.set_ylabel('Mass velocity [m/s]')
        #x1.set_xlabel('Time [s]')
        #x2.plot(time,X2)
        #x3 = f.add_subplot(313)
        #x3.set_title('Acceleration')
        #x3.set_ylabel('Mass acceleration [m/s^2]')
        #x1.set_xlabel('Time [s]')
        #x3.plot(time,X3)
        canvas1 = FigureCanvasTkAgg(f1, self.window)
        canvas1.get_tk_widget().grid(row=0,column=4,columnspan=1,rowspan=2)
        canvas1.draw()
        canvas2 = FigureCanvasTkAgg(f2, self.window)
        canvas2.get_tk_widget().grid(row=2,column=4,columnspan=1,rowspan=2)
        canvas2.draw()
        canvas3 = FigureCanvasTkAgg(f3, self.window)
        canvas3.get_tk_widget().grid(row=4,column=4,columnspan=1,rowspan=2)
        canvas3.draw()

        toolbarFrame = Frame(self.window)
        toolbarFrame.grid(row=22,column=4)
        toolbar = NavigationToolbar2Tk(canvas1, toolbarFrame)
        toolbar = NavigationToolbar2Tk(canvas2, toolbarFrame)
        toolbar = NavigationToolbar2Tk(canvas3, toolbarFrame)
        #canvas.show()
        #canvas.get_tk_widget().pack()

        #value = Entry(self.window,
        #    text=self.showText,
        #    #width=25,
        #    #height=5,
	    #    #command=self.execFunc,
        #    fg=self.fgndColor,  # Set the text color to white
        #    bg=self.bgndColor  # Set the background color to black
        #).grid(column=self.gridCollumn, row=self.gridRow)

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

#########################################
##### All functions for setup 3 --> #####
#########################################
def setup3():

    visuals[0:2] = stdVisuals[3:5]
    mainScreen.addButton("Taking measurement...",[3,0],passFunc,visuals)
    mainScreen.updt()

    ## Simple example for measurement
    dis = measDis(2)
    plotDis(dis)

    visuals[0:2] = stdVisuals[0:2]
    mainScreen.addButton("Setup 2 start",[3,0],setup3,visuals)


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
teta = [2,4,8,14]
omega = [0,2,4,6]
alpha = [2,2,2,2]
t = [1,2,3,4]

mainScreen = GUI()
mainScreen.genWindow(visuals,' ProfielWerkstuk')
mainScreen.addButton("Setup 1 start",[1,0],setup1,visuals)
mainScreen.addButton("Setup 2 start",[2,0],setup2,visuals)
mainScreen.addButton("Setup 3 start",[3,0],setup3,visuals)
mainScreen.addButton("Setup 3 start",[3,1],setup3,visuals)
#mainScreen.addLabel("Graphs for students to see will be placed here",[0,0],visuals)
mainScreen.addGraph(teta,omega,alpha,t,visuals)

#graphScreen = GUI()
#graphScreen.genWindow(visuals,' Graphs')
#graphScreen.addLabel("Graphs for students to see will be placed here",[0,0],visuals)

#graphScreen.show()
mainScreen.show()
