"This is a template for the basic, starting point for Tkinter programs"

from tkinter import *
from tkinter import ttk       

class gui_template():
    
    def __init__(self):
        
        "This is the init method, it'll set up all the variables needed in the app"
        
        self.__title = "Test Application"                   #This sets the title of the app, which appears at the very top left
        self.__screen_geometry = "1920x1080"                #This sets up how big the screen will be
        self.__mainScreenFile = "bacground_image.png"       #This sets up an instance of the Tk libary
        self.__MainWindow = Tk()

        self.var1 = StringVar()
        self.var2 = StringVar()
        
        
    def screen(self):
        mainScreen = self.__MainWindow                  #This loads the Tk instance
        mainScreen.title(self.__title)                  #This sets the title to what was assigned in init
        mainScreen.geometry(self.__screen_geometry)     #This sets the geometry to what was assigned in init
        
        mainScreen.attributes("-topmost", False)        #This makes it so the app appears ontop of other open apps, False means it wont       
        mainScreen.resizable(False, False)              #This decides if the user can change the size of the window
        background = ttk.Label(mainScreen , text = "")  #This adds a label to the screen, so a backing image can be applied
        background.place(x=0, y=0)                  #Place is one of Tkinters 2 methods of placing something on the screen (other is "pack")

        logo = PhotoImage(file = self.__mainScreenFile, master=mainScreen)    #This assigns the image defined in init to a local variable
        background.config(image = logo)     #This applies the image to the previously declared label
        background.img = logo
        background.config(image = background.img)
        
        txtCityName = ttk.Entry(mainScreen,textvariable= self.var1, width=40)  #This sets up a text box and what where the entered text will be stored
        txtCityName.place(x=748, y=217) 
        btnSearch = ttk.Button(mainScreen,command=self.var2,text=" Search ")  #This sets up a button and assigns a command to run when clicked
        btnSearch.place(x=828, y=257)
        
        txtCityName.focus_set()  #This makes it so the user doesn't have to click the text box to begin typing
        
        mainScreen.option_add('*tearOff', False) #This disables the ability for the user to freely move anything put on the screen(buttons, menus, etc)
    
        mainScreen.mainloop()   #This begins the main loop, the app will now run till its closed, it will wait for events to happen and respond accordingly
        