# Kendra Tam
# StudyBreak.py
# May 31, 2017
# This program is a mini-game application.

#importing 
from Tkinter import *
import random

#this class is for the main page
class MainGUI():
    # __init__ - creates the main page
    # @param - self(object), master(screen)
    # @return - none
    def __init__(self, master):
        #declaring attribute
        self.master = master
        
        #setting the title and size of the screen
        self.master.title("Study Break")
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main")
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #declaring an image
        self.logo = PhotoImage(file="logo.gif")
        #creating the title/header of the screen
        header = Label(self.master, image = self.logo)
        
        #create buttons to go to the games page
        playBtn = Button(self.master,text = "Play", font = ("Helvetica",18), command = self.toPlay)
        #create button to go to the scores page
        scoresBtn = Button(self.master,text = "Scores", font = ("Helvetica",18), command = self.toScores)
        #output a small introduction on the screen
        intro1 = Label(self.master, text = "Take a break from your work and enjoy", font = ("Helvetica", 15))
        intro2 = Label(self.master, text = "playing some fun minigames to relax.", font = ("Helvetica", 15))
        
        #declare an image
        self.gear = PhotoImage(file="setting.gif")
        #putting the image on to the settings button
        settingBtn=Button(self.master, command = self.toSetting, image=self.gear,width="40",height="40")
        #all the items on the page
        items = [header,playBtn,scoresBtn,intro1,intro2,settingBtn]
        
        #declaring variable that will keep track of which element we are on
        count = 0
        
        #goes through all the rows need for the grid
        for i in range(0,12):
            #goes through all the coloumns needed for the grid
            for j in range(0,3):
                #if we are on the settings button element, are on the 12th row and the first column, output the settings button on the grid
                if count == 5 and i == 11 and j == 0:
                    items[count].grid(row=i,column=0)
                
                #if we are on the second column, on an even row, and the count is not 5, output the elements
                elif j == 1 and i % 2 == 0 and count != 5:
                    #outputing the elements on the screen at the correct part of the grid
                    items[count].grid(row=i,column=j)
                    count = count + 1
                
                #if it isn't the 8th row, put fillers to fill up the grid with empty space
                elif i != 7:
                    #creating a filler label
                    filler = Label(self.master,text = "          ", font = ("Helvetica",10))
                    filler.grid(row=i,column=j)
    
    # makeNew - creates a new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSetting - goes to the settings window
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
    
    # toPlay - goes to the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
    
    # toScores - goes to the scores page
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the scores page
        root = ScoresMain(newWindow)

#this class is for the settings page
class Settings():
    # __init__ - creates the settings page
    # @param - self(object), master(screen)
    # @return - none
    def __init__(self, master):
        #declaring attributes
        self.master = master
        #setting the title and size of the screen
        self.master.title("Settings")
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main", command = self.toMain)
        pathmenu.add_command(label = "Games", command = self.toPlay)
        pathmenu.add_command(label = "Settings")
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        header = Label(self.master, text = "Settings", font = ("Helvetica",50))
        header.pack()
        
        #creates label about earsing score
        eraseLbl = Label(self.master, text = "Erase Scores:", font = ("Helvetica",15))
        #places the label
        eraseLbl.place(x = 170, y = 170, width = 180)
        
        #list of the game names
        self.gameNames = ["Memory Game", "Phonetic Alphabet", "Tic Tac Toe"]
        #creates and places the listbox storing the game's scores that you can erase
        self.eraseListbox = Listbox(self.master, font = ("Helvetica",15), selectmode = MULTIPLE)
        #places the listbox
        self.eraseListbox.place(x = 330, y = 175, width = 180, height = 75)
        
        #goes through all the games 
        for i in range(0,len(self.gameNames)):
            #inserts each game into the lisbox
            self.eraseListbox.insert(i,self.gameNames[i])
        
        #creates the back button to go back to the previous page
        backBtn = Button(self.master, text = "Back", font = ("Helvetica",15), command = self.toMain)
        #creates the save button to save which game's scores you wanted to erase
        saveBtn = Button(self.master, text = "Save", font = ("Helvetica",15), command = self.saveErase)
        
        #places the back and save button on the screen
        backBtn.place(x = 0, y = 452, width = 100)
        saveBtn.place(x = 600, y = 452, width = 100)
    
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
    
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main scores page
        root = ScoresMain(newWindow)
    
    # saveErase - erases the scores of the games the user specified
    # @param - self(object)
    # @return - none
    def saveErase(self):
        #declaring variables
        eraseScores = []
        
        #what you have selected in list box
        selections = self.eraseListbox.curselection()
        
        #finds the integer index for each selection in the list box
        selections = [int(x) for x in selections]
        
        #converting integers to game names -- for loop
        [eraseScores.append(self.gameNames[x]) for x in selections]
        
        #goes through all the games to erase
        for i in range(0,len(eraseScores)):
            #declare filename
            filename = eraseScores[i]
            
            #for every spaces there is in the filename, take out the space
            for i in range(0,filename.count(" ")):
                #taking out the space
                filename = filename[0:filename.index(" ")] + filename[filename.index(" ")+1:len(filename)]
            
            #update filename
            filename = filename + ".txt"
            
            #open the file to write it
            f = open(filename,'w')
            #variable keeps track of the ranks
            count = 1
            
            #goes through all the rows needed for the file
            for i in range(0,9):
                #if the row is even, write the ranks
                if i % 2 == 0:
                    #write the rank and the appropirate number of spaces so that it can later be read properly
                    f.writelines(str(count) + "      \n")
                    count = count + 1
                #otherwise if the row is odd
                else:
                    #write the rank and the appropirate number of spaces so that it can later be read properly
                    f.writelines("               \n")
            
            #clase the file
            f.close()
        
        #creates and places a label to show the earsing has been done
        doneLbl = Label(self.master, text = "Done", font = ("Helvetica",15), fg = "red")
        doneLbl.place(x = 600, y = 425, width = 100)
        #after 1 second destroy the label so that the label appears to flash once
        doneLbl.after(1000, lambda: doneLbl.destroy())
        
#this class is for the play page
class MainPlay():
    # __init__ - creates the play page
    # @param - self(object), master(screen)
    # @return - none
    def __init__(self, master):
        #declaring attribute
        self.master = master
        
        #setting the title and size of the screen
        self.master.title("Study Break")
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main", command = self.toMain)
        pathmenu.add_command(label = "Games")
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        header = Label(self.master, text = "Pick A Game", font = ("Helvetica",50))
        header.pack()
        
        #declaring the game names
        gameNames = ["Memory Game", "Phonetic Alphabet", "Tic Tac Toe"]
        
        #go through all the game names to output the corresponding button
        for i in range(0,len(gameNames)):
            #creates and places the button to go the corresponding game
            btn = Button(self.master, text = gameNames[i], font = ("Helvetica",15), width = "15", command = lambda name = gameNames[i]:self.toInstruction(name))
            btn.place(x = 30 + 231*i, y = 200)
        
        #creates and places the back button to go back to the previous page
        backBtn = Button(self.master, text = "Back", font = ("Helvetica",15), command = self.toMain)
        backBtn.place(x = 0, y = 452, width = 100)
    
    # toMain - goes to main page
    # @param - self(object)
    # @return - none  
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSetting - goes to the settings page
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to be the Settings page
        root = Settings(newWindow)
        
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to be the scores page
        root = ScoresMain(newWindow)
    
    # toInstructions - goes to the instructions page for the corect game
    # @param - self(object)
    # @return - none
    def toInstruction(self,name):
        #removing the main screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #sets the new window for the game's instruction page, it is not being called during the game
        root = Instruction(newWindow,name,False)


#this class is for all the game's instructions
class Instruction():
    # __init__ - creates the settings page
    # @param - self(object), master(screen), name(str), inPlay(boolean)
    # @return - none
    def __init__(self, master, name, inPlay):
        #declaring attributes
        self.master = master
        self.name = name
        
        #setting the title and size of the screen
        self.master.title(self.name)
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main",command = self.toMain)
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        self.header = Label(self.master, text = self.name, font = ("Helvetica",50))
        self.header.pack()

        #declares all the game's names
        gameNames = ["Memory Game", "Phonetic Alphabet", "Tic Tac Toe"]
        #declares the instructions for each game and puts them into a list
        mgInst = "This game will test your memory (if it wasn't obvious\nenough). Click two squares to reveal their hidden\ncolour. If the square's colours don't match, the colour\nwill hid itself again. Try to find all the pairs of colours\nas fast as possible. You have a time limit of one\nminute before the game screen disappears."
        paInst = "This game will test your knowledge of the phonetic\nalphabet. Type and enter your answer for each letter's\ncorresponding word. If you get a correct answer, the\ntext entry will flash green, and the answer will be added\nto the table. If you answer wrong or input an answer\nyou have already entered, the text entry will flash red.\nOnce you have answered as much as you can, hit the\n\"Done\" button."
        tttInst = "This game is a classic two player game. The first\nperson to start will be Player X, and the second person\nwill be Player O. You will take alternate turns placing\nX's and O's on the board until one player gets three in\na row (either horizontally, vertically, or diagonally)\nand wins the game. Try to get three in a row with as less\nsteps as possible to get a better score. If the game\nresults in a tie, both players will not recieve any scores."
        allInst = [mgInst, paInst, tttInst]
        
        #the instrutions at the same index as the game name is will be the correct set of instructions for the game
        inst = allInst[gameNames.index(self.name)]
        
        #creates and outputs the instructions on to the screen
        self.instructHeader = Label(master, text = "Instructions\n", font = ("Helvetica",25))
        self.instructHeader.pack()
        self.instructLbl = Label(master, text = inst, font = ("Helvetica",18))
        self.instructLbl.pack()
        self.luckLbl = Label(master, text = "\nGOOD LUCK!", font = ("Helvetica",18))
        self.luckLbl.pack()
        
        #if the instructions are not being called during the game have a play and back button
        if not inPlay:
            #create a back button to go back to the previous page
            self.backBtn = Button(self.master, text = "Back", font = ("Helvetica",15), command = self.toPlay)
            #create a play button to start playing the game
            self.playBtn = Button(self.master, text = "Play", font = ("Helvetica",15), command = self.toGamePlay)
            
            #place the back and play button onto the screen
            self.backBtn.place(x = 0, y = 452, width = 100)
            self.playBtn.place(x = 600, y = 452, width = 100)
        
        #otherwise the instructions are being pulled up during the game
        else:
            #create and output a contiue playing button
            self.conBtn = Button(self.master, text = "Continue Play", font = ("Helvetica",15), command = self.master.withdraw)
            self.conBtn.place(x = 550, y = 452, width = 150)
    
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSettings - goes to the settings page
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
        
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
    
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the score page
        root = ScoresMain(newWindow)
    
    # toGamePlay - goes the the game screen
    # @param - self(object)
    # @return - none
    def toGamePlay(self):
        #removing the main screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the correct game
        #if the game is the Memory Game go to that game's screen
        if self.name == "Memory Game":
            root = MemoryGame(newWindow)
        #elif the game is the Phonetic Alphabet go to that game's screen
        elif self.name == "Phonetic Alphabet":
            root = PhoneticAlphabet(newWindow)
        #elif the game is the Tic Tac Toe go to that game's screen
        elif self.name == "Tic Tac Toe":
            root = TicTacToe(newWindow)

#this class is for the Memory Game screen
class MemoryGame():
    # __init__ - creates the Memory Game screen
    # @param - self(object), master(screen)
    # @return - none
    def __init__(self, master):
        #declaring attributes
        self.master = master
        self.selected = 0
        self.score = 0
        self.grid = []
        self.gridColours = []
        self.gridSelect = []
        self.quitted = False
        
        #sets the title and size of the screen
        self.master.title("Memory Game")
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.close)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main",command = self.toMain)
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #adding a new menu
        instmenu = Menu(menubar,tearoff=0)
        #adding command to the instructions menu
        instmenu.add_command(label = "Memory Game", command = self.toInstruction)
        #making the commands cascade
        menubar.add_cascade(label = "Instruction", menu = instmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        header = Label(self.master, text = "Memory Game", font = ("Helvetica",50))
        header.pack()
        
        #declaring the colour options
        colourOptions = ["medium blue","red","orange","yellow","dark green","purple","pink","black","lawn green","cyan","medium blue","red","orange","yellow","dark green","purple","pink","black","lawn green","cyan"]
        
        #going through all the rows of buttons
        for i in range(0,4):
            #declare variables
            rowGrid = []
            rowColours = []
            rowFound = []
            
            #going through all the columns of buttons
            for j in range(0,5):
                #generate a random integer to choose which colour the current button will hid
                randInt = random.randint(0,len(colourOptions)-1)
                colour = colourOptions[randInt]
                #remove the option from the list
                colourOptions.remove(colour)
                
                #create and place the button onto the screen
                btn = Button(self.master, bg = "grey", command = lambda row = i, col = j:self.clicked(row,col))
                btn.place(x = 128 + 90*j, y = 90 + 90*i, width = 80, height = 80)
                
                #append the button's details to the correct lists
                rowGrid.append(btn)
                rowColours.append(colour)
                rowFound.append(0)
            
            #append the row lists to the correct 2D lists
            self.grid.append(rowGrid)
            self.gridColours.append(rowColours)
        
        #create and place the quit button to quit the game
        quitBtn = Button(self.master, text = "Quit", font = ("Helvetica",15), command = self.toMain)
        quitBtn.place(x = 0, y = 452, width = 100)
        
        #after 1 minute end the game and go check if the user has a high score
        self.master.after(60000, self.checkHigh)
        
    # clicked - reveal the colour of the button when clicked
    # @param - self(object), row(int), col(int)
    # @return - none 
    def clicked(self,row,col):
        #increase the number of elements selected
        self.selected = self.selected + 1
        
        #if only one button has been selected reveal the colour
        if self.selected == 1:
            #remember the coordinates of this selection
            self.gridSelect = [row,col]
            #reveal the colour
            self.grid[row][col].configure(relief = SUNKEN, bg = self.gridColours[row][col], state = DISABLED)
        
        #if this is the second selections
        if self.selected == 2:
            #declare variables
            lastRow = self.gridSelect[0]
            lastCol = self.gridSelect[1]
            
            #if the colour of the previous selection is the same as the colour of the current selections
            if self.gridColours[lastRow][lastCol] == self.gridColours[row][col]:
                #reveal the colour of the current button
                self.grid[row][col].configure(relief = SUNKEN, bg = self.gridColours[row][col], state = DISABLED)
                #update the fact that a match has been found
                self.score = self.score + 1
            
            #if the colours do not match
            else:
                #show the colour of the current button
                self.grid[row][col].configure(relief = SUNKEN, bg = self.gridColours[row][col], state = DISABLED)
                
                #after 500 milisecond, hide the colour of the current and previous button that was selected
                self.grid[row][col].after(500, lambda: self.grid[row][col].configure(bg = "grey", relief = RAISED, state = NORMAL))
                self.grid[lastRow][lastCol].after(500, lambda: self.grid[lastRow][lastCol].configure(bg = "grey", relief = RAISED, state = NORMAL))
            
            #reset the number of buttons selected to 0
            self.selected = 0
        
        if self.score == 10:
            #create and output the done button so that the program can now show you your score
            doneBtn = Button(self.master, text = "Done", font = ("Helvetica",15), command = self.checkHigh)
            doneBtn.place(x = 600, y = 452, width = 100)
    
    # checkHigh - checks if the player got a high score
    # @param - self(object)
    # @return - none  
    def checkHigh(self):
        #if the game has not quit yet
        if not self.quitted:
            #declare variable
            scores = []
            self.quitted = True
            
            #opens textfile containing scores
            f = open("MemoryGame.txt")
            #read all the lines in the file
            for i in range(0,9):
                line = f.readline()
                #if the row number is even, collect the scores
                if i % 2 == 0:
                    #split the values in the row
                    vals = line.split('   ')
                    #append the score to the list
                    scores.append(vals[1])
            #close the file
            f.close()
            
            #hold the last score in the temp variable
            temp = scores[4]
            #if the last score is empty
            if temp == "":
                #make the last score a low number that you cannot obtain
                temp = -1
                
            #if the user has a higher value than the lowest value on the scores list, go to the new highscore page
            if self.score > int(temp):
                self.toNewHigh()
            #otherwise no high score was achieved so just go striaght to the your score's page
            else:
                self.toYourScore()
    
    # toNewHigh - goes to new high score page
    # @param - self(object)
    # @return - none  
    def toNewHigh(self):
        #removing the main screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the new high score page
        root = NewHighScore(newWindow,"Memory Game",str(self.score))
            
    # toYourScore - goes to your score page
    # @param - self(object)
    # @return - none  
    def toYourScore(self):
        #removing the main screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the your score page
        root = YourScore(newWindow,"Memory Game",str(self.score))
        
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #the game is quitting
        self.quitted = True
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # makeNew - create closes the window
    # @param - self(object)
    # @return - none
    def close(self):
        #the game is quitting
        self.quitted = True
        #removing the current screen
        self.master.withdraw()
    
    # toSettings - goes to the settings page
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #the game is quitting
        self.quitted = True
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #the game is quitting
        self.quitted = True
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
    
    # toInstruction - brings up the instructions during a game
    # @param - self(object)
    # @return - none
    def toInstruction(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the game's Instructions page
        root = Instruction(newWindow,"Memory Game",True)
        
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #the game is quitting
        self.quitted = True
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the score page
        root = ScoresMain(newWindow)

#this class is for the Phonetic Alphabet game
class PhoneticAlphabet():
    # __init__ - creates the Phonetic Alphabet screen
    # @param - self(object), master(screen)
    # @return - none
    def __init__(self, master):
        #declaring attributtes
        self.master = master
        self.score = 0
        self.ans = ["alpha","bravo","charlie","delta","echo", "foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whiskey","x-ray","yankee","zulu", " "]
        self.ansSlots = []
        self.answered = []
        
        #sets the title and size of the screen
        self.master.title("Phonetic Alphabet")
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main",command = self.toMain)
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #adding a new menu
        instmenu = Menu(menubar,tearoff=0)
        #adding command to the instructions menu
        instmenu.add_command(label = "Phonetic Alphabet", command = self.toInstruction)
        #making the commands cascade
        menubar.add_cascade(label = "Instruction", menu = instmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        header = Label(self.master, text = "Phonetic Alphabet", font = ("Helvetica",50))
        header.pack()
        
        #creating and outputting the text entry used for the user to enter in their answer
        self.answerEntry = Entry(self.master, font = ("Helvetica",13))
        self.answerEntry.place(x = 50, y = 110)
        
        #creating and outputting the enter button so the user can submit their answers
        enterbtn = Button(self.master, text = "Enter", font = ("Helvetica",13), command = self.checkAns)
        enterbtn.place(x = 250, y = 110, height = 25)
        
        #declaring variables
        countLetters = 0
        
        #go through all the columns of the grid
        for i in range(0,6):
            #go through all the rows of the grid
            for j in range(0,9):
                #if the column is even, output the letters
                if i % 2 == 0:
                    #create and output the letters
                    letterLbl = Label(self.master, text = self.ans[countLetters][0].upper(), bd = 3, relief = GROOVE, font = ("Helvetica",10))
                    letterLbl.place(x = 50 + 100*i, y = 160 + 30*j, width = 35, height = 35)
                    #update which letter is next
                    countLetters = countLetters + 1
                #otherwise the column is odd, so output the slots for the answers
                else:
                    #create and output the slots for the answers
                    ansSlotsLbl = Label(self.master, text = "", anchor = "w", bd = 3, relief = GROOVE, font = ("Helvetica",10))
                    ansSlotsLbl.place(x = 83 + 100*(i-1), y = 160 + 30*j, width = 170, height = 35)
                    #append the slot to a list
                    self.ansSlots.append(ansSlotsLbl)
        
        #create the quit button to quit the game 
        self.quitBtn = Button(self.master, text = "Quit", font = ("Helvetica",15), command = self.toMain)
        #create the done button to say the user has finished the game
        self.doneBtn = Button(self.master, text = "Done", font = ("Helvetica",15), command = self.checkHigh)

        #place the quit and done button
        self.quitBtn.place(x = 0, y = 452, width = 100)
        self.doneBtn.place(x = 600, y = 452, width = 100)
        
    # checkAns - check if the answer the user has given is correct
    # @param - self(object)
    # @return - none 
    def checkAns(self):
        #get the answer from the text entry
        userAns = self.answerEntry.get()
        
        #try to conver the answer into lower cases
        try:
            userAns = userAns.lower()
        #if you can't change the answer into an empty string
        except:
            userAns = " "
        
        #if the user's answer in the answers, is not an empty string, and has not already been entered, mark it as correct
        if userAns in self.ans and userAns != " " and not userAns in self.answered:
            #put the answer into the table
            self.ansSlots[self.ans.index(userAns)].configure(text = userAns)
            #add it to the answered list
            self.answered.append(userAns)
            #increase the score by one
            self.score = self.score + 1
            #indicate to the user they got it correct by changing the entry to green
            self.answerEntry.configure(bg = "green")
        
        #otherwise the user got it wrong and indicate it to them by making the text entry red
        else:
            self.answerEntry.configure(bg = "red")
        
        #after 400 miliseconds, return the colour back to normal and clear the text from the entry
        self.answerEntry.after(400, lambda: self.answerEntry.configure(bg = "white"))
        self.answerEntry.after(400, lambda: self.answerEntry.delete(0,'end'))
    
    # checkHigh - checks if the player got a high score
    # @param - self(object)
    # @return - none  
    def checkHigh(self):
        #declare variable
        scores = []
        
        #opens textfile containing scores
        f = open("PhoneticAlphabet.txt")
        #read all the lines in the file
        for i in range(0,9):
            line = f.readline()
            #if the row number is even, collect the scores
            if i % 2 == 0:
                #split the values in the row
                vals = line.split('   ')
                #append the score to the list
                scores.append(vals[1])
        #close the file
        f.close()
        
        #hold the last score in the temp variable
        temp = scores[4]
        #if the last score is empty
        if temp == "":
            #make the last score a low number that you cannot obtain
            temp = -1
        
        #if the user's score is greater than the lowest value on the scores list, go to the new high score page
        if self.score > int(temp):
            self.toNewHigh()
        #otherwise no high score was achieved so just go striaght to the your score's page
        else:
            self.toYourScore()
    
    # toNewHigh - goes to new high score page
    # @param - self(object)
    # @return - none  
    def toNewHigh(self):
        #removing the main screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the new high score page
        root = NewHighScore(newWindow,"Phonetic Alphabet",str(self.score))
            
    # toYourScore - goes to your score page
    # @param - self(object)
    # @return - none  
    def toYourScore(self):
        #removing the main screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the your score page
        root = YourScore(newWindow,"Phonetic Alphabet",str(self.score))
        
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSetting - goes to the settings window
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
    
    # toInstruction - brings up the instructions during a game
    # @param - self(object)
    # @return - none
    def toInstruction(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the game's Instructions page
        root = Instruction(newWindow,"Phonetic Alphabet",True)
    
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the score page
        root = ScoresMain(newWindow)

#this class is for the tic tac toe class
class TicTacToe():
    # __init__ - creates the Tic Tac Toe screen
    # @param - self(object), master(screen)
    # @return - none
    def __init__(self, master):
        #declaring attributes
        self.master = master
        self.xmoves = 0
        self.omoves = 0
        self.winScore = 0
        self.turn = "X"
        self.playgrid = []
        self.gridVals = [["","",""],["","",""],["","",""]]
        
        #sets the title and size of the screen
        self.master.title("Tic Tac Toe")
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main",command = self.toMain)
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #adding a new menu
        instmenu = Menu(menubar,tearoff=0)
        #adding command to the instructions menu
        instmenu.add_command(label = "Tic Tac Toe", command = self.toInstruction)
        #making the commands cascade
        menubar.add_cascade(label = "Instruction", menu = instmenu)
        
        #putting the menubar on the screen            
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        header = Label(self.master, text = "Tic Tac Toe", font = ("Helvetica",50))
        header.pack()
        
        #goes through all the rows
        for i in range(0,3):
            row = []
            #goes through all the columns
            for j in range(0,3):
                #creates and places the tic tac toe buttons
                btn = Button(self.master, text = "", relief = GROOVE, bd = 8, font = ("Helvetica",50),command = lambda row = i, col = j:self.place(row,col))
                btn.place(x = 90 + 90*j, y = 100 + 90*i, width = 100, height = 100)
                row.append(btn)
            self.playgrid.append(row)
        
        #creates and outputs the label labeling the x's moves
        xmovesHeaderLbl = Label(self.master, text = "# of X's moves", font = ("Helvetica",20))
        xmovesHeaderLbl.place(x = 405, y = 110, width = 250)
        #creates and outputs the number of x's moves
        self.xmovesLbl = Label(self.master, text = self.xmoves, font = ("Helvetica",40))
        self.xmovesLbl.place(x = 405, y = 150, width = 250)
        
        #creates and outputs the label labeling the o's moves
        omovesHeaderLbl = Label(self.master, text = "# of O's moves", font = ("Helvetica",20))
        omovesHeaderLbl.place(x = 405, y = 270, width = 250)
        #creates and outputs the number of o's moves
        self.omovesLbl = Label(self.master, text = self.omoves, font = ("Helvetica",40))
        self.omovesLbl.place(x = 405, y = 300, width = 250)
        
        #creates and outputs the label showing whose turn it is
        self.turnLbl = Label(self.master, text = "Player X's Turn", font = ("Helvetica",20))
        self.turnLbl.place(x = 80, y = 390, width = 300)
        
        #create and place the quit button to quit the game
        quitBtn = Button(self.master, text = "Quit", font = ("Helvetica",15), command = self.toMain)
        quitBtn.place(x = 0, y = 452, width = 100)
    
    # place - place the X/O onto the screen
    # @param - self(object), row(int), col(int)
    # @return - none 
    def place(self,row,col):
        #if it is X's turn, place a X on the grid
        if self.turn == "X":
            #change the text of the button the user clicked on to X and disable the button
            self.playgrid[row][col].configure(text = "X", state = DISABLED)
            #record the value placed in a 2D list
            self.gridVals[row][col] = "X"
            #update the number of moves x has made
            self.xmoves = self.xmoves + 1
            self.xmovesLbl.configure(text = self.xmoves)
        
        #if it is O's turn, place an O on the grid
        else:
            #change the text of the button the user clicked on to an O and disable the button
            self.playgrid[row][col].configure(text = "O", state = DISABLED)
            self.gridVals[row][col] = "O"
            #update the number of moves o has made
            self.omoves = self.omoves + 1
            self.omovesLbl.configure(text = self.omoves)
    
        #check if there has been a win
        win = self.checkWin(row,col)
        #check if the grid has been filled and the game has tied
        filled = self.checkFill()
        
        #if the current player did not make a winning move, check if the grid is full yet
        if not win:
            #if it is not filled, go to the next turn
            if not filled:
                #if the user who just went was x, it is now o's turn
                if self.turn == "X":
                    self.turn = "O"
                    self.turnLbl.configure(text = "Player O's Turn")
                
                #if the user who just went was o, it is now x's turn
                else:
                    self.turn = "X"
                    self.turnLbl.configure(text = "Player X's Turn")
            
            #otherwise the grid is filled
            else:
                #indicate that it was a tie game
                self.turnLbl.configure(text = "Tied Game")
                #show the done button to exit the game and to see you're score
                doneBtn = Button(self.master, text = "Done", font = ("Helvetica",15), command = self.toMain)
                doneBtn.place(x = 600, y = 452, width = 100)
        
        #if the current player did make a winning move, end the game
        else:
            #indicate who won
            self.turnLbl.configure(text = self.turn + " wins!")
            
            #for all the rows in the grid
            for i in range(0,3):
                #for all the columns in the grid
                for j in range(0,3):
                    #disable all the buttons so that you cannot continue playing
                    self.playgrid[i][j].configure(state = DISABLED)
            
            #show the done button to exit the game and to see you're score
            doneBtn = Button(self.master, text = "Done", font = ("Helvetica",15), command = self.checkHigh)
            doneBtn.place(x = 600, y = 452, width = 100)
    
    # checkFill - checks if the playing grid has already been filled
    # @param - self(object)
    # @return - True/False(boolean)  
    def checkFill(self):
        #for all the rows
        for i in range(0,3):
            #for all the columns
            for j in range(0,3):
                #check if the value inside it is blank
                if self.gridVals[i][j] == "":
                    #if there is an empty value, the grid is not filled
                    return False
        
        #if there were no empty values found, the grid is filled
        return True
    
    # checkwin - checks if there is a winner
    # @param - self(object), row(int), col(int)
    # @return - True/False(boolean)  
    def checkWin(self,row,col):
         #check if previous move caused a vertical win
        if self.gridVals[0][col] == self.turn and self.gridVals[1][col] == self.turn and self.gridVals[2][col] == self.turn:
            #a player won
            return True
        
        #check if previous move caused a horizontal win
        if self.gridVals[row][0] == self.turn and self.gridVals[row][1] == self.turn and self.gridVals[row][2] == self.turn:
            #a player won
            return True
        
        #check if previous move was on the main diagonal and caused a win
        if self.gridVals[0][0] == self.turn and self.gridVals[1][1] == self.turn and self.gridVals[2][2] == self.turn:
            #a player won
            return True
        
        #check if previous move was on the secondary diagonal and caused a win
        if self.gridVals[0][2] == self.turn and self.gridVals[1][1] == self.turn and self.gridVals[2][0] == self.turn:
            #a player won
            return True
        
        #if none of the conditions above were met, no one has won the game yet
        return False
    
    # checkHigh - checks if the player got a high score
    # @param - self(object)
    # @return - none 
    def checkHigh(self):
        #if the last player was X, the number of their moves are the score
        if self.turn == "X":
            self.winScore = self.xmoves
        #if the last player was O, the number of their moves are the score
        else:
            self.winScore = self.omoves
        
        #declare variable to hold the scores from the text file
        scores = []
        
        #opens textfile containing scores
        f = open("TicTacToe.txt")
        #read all the lines in the file
        for i in range(0,9):
            line = f.readline()
            #if the row number is even, collect the scores
            if i % 2 == 0:
                #split the values in the row
                vals = line.split('   ')
                #append the score to the list
                scores.append(vals[1])
        #close the file
        f.close()
        
        #hold the last score in the temp variable
        temp = scores[4]
        #if the last score is empty
        if temp == "":
            #make the last score a high number that you cannot obtain
            temp = 100
        
        #if the user has a lower score than the highest score on the score's list, go to the new high score page to record the high score
        if self.winScore < int(temp):
            self.toNewHigh()
        #otherwise no high score was achieved so just go striaght to the your score's page
        else:
            self.toYourScore()
    
    # toNewHigh - goes to new high score page
    # @param - self(object)
    # @return - none  
    def toNewHigh(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the new high score page
        root = NewHighScore(newWindow,"Tic Tac Toe",str(self.winScore))
            
    # toYourScore - goes to your score page
    # @param - self(object)
    # @return - none  
    def toYourScore(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the your score page
        root = YourScore(newWindow,"Tic Tac Toe",str(self.winScore))
            
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSetting - goes to the settings window
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
    
    # toInstruction - brings up the instructions during a game
    # @param - self(object)
    # @return - none
    def toInstruction(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the game's Instructions page
        root = Instruction(newWindow,"Tic Tac Toe",True)
        
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the score page
        root = ScoresMain(newWindow)

#this class is for the main scores page
class ScoresMain():
    # __init__ - creates the main scores page
    # @param - self(object), master(screen)
    # @return - none
    def __init__(self, master):
        #declaring attribute
        self.master = master
        self.gameNames = ["Memory Game", "Phonetic Alphabet", "Tic Tac Toe"]
        
        #setting the title and size of the screen
        self.master.title("Scores")
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main",command = self.toMain)
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores")
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        header = Label(self.master, text = "Scores", font = ("Helvetica",50))
        header.pack()
        
        #go through all the game names
        for i in range(0,len(self.gameNames)):
            #creates and ouputs a button for each game that will redirect them to the coresponding game
            btn = Button(self.master, text = self.gameNames[i], font = ("Helvetica",15), width = "15", command = lambda name = self.gameNames[i]:self.toGameScores(name))
            btn.place(x = 30 + 231*i, y = 200)
        
        #create and output the back button that will go back to the previous page
        backBtn = Button(self.master, text = "Back", font = ("Helvetica",15), command = self.toMain)
        backBtn.place(x = 0, y = 452, width = 100)
     
    # toGameScores - goes to the correct game's score page
    # @param - self(object), name(str)
    # @return - none 
    def toGameScores(self, name):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window the correct game's score page
        root = GameScores(newWindow, name)
                
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSetting - goes to the settings window
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
    
#this class is for the new high score page
class NewHighScore():
    ## __init__ - creates new high score page
    # @param - self(object), master(screen)
    # @return - none
    def __init__(self, master, gameName, score):
        #declaring attributes
        self.master = master
        self.gameName = gameName
        self.score = score
        
        #setting a title and size for the screen
        self.master.title("New High Score")
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main",command = self.toMain)
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        self.header = Label(self.master, text = "New High Score", font = ("Helvetica",50))
        self.header.pack()
        
        #creates and outputs the label indicating where to enter your name
        self.enterLbl = Label(self.master, text = "\n\nEnter Your Name:\n", font = ("Helvetica",20))
        self.enterLbl.pack()
        
        #creates and outputs the entry where you enter your name
        self.entry = Entry(self.master, font = ("Helvetica",15))
        self.entry.pack()
        
        #creates and outputs a filler to space out the objects 
        self.filler = Label(self.master, text = "     ", font = ("Helvetica",15))
        self.filler.pack()
        
        #creates and outputs the submit button to submit your high score and name
        self.submit = Button(self.master, text = "Submit", font = ("Helvetica",15), command = self.submitHigh)
        self.submit.pack()
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def submitHigh(self):
        #delcaring variables
        #gets the text from the text entry box
        username = self.entry.get()
        filename = self.gameName
        ranks = []
        scores = []
        names = []
        
        #counts the number of spaces in the game name
        spaces = filename.count(" ")
        #for every space, take out the space
        for i in range(0, spaces):
            #will the first space in the string
            filename = filename[0:filename.index(" ")] + filename[filename.index(" ")+1:len(filename)]
    
        #update filename
        filename = filename + ".txt"
        #open text file
        f = open(filename)
        #for every line in the text file
        for i in range(0,9):
            #read the line
            line = f.readline()
            #if the line is even
            if i % 2 == 0:
                #split the values
                vals = line.split('   ')
                #append the second set of values to the scores
                scores.append(vals[1])
                #append the third set of values to the names (take out the \n at the end of the string)
                names.append(vals[2][0:len(vals[2])-1])
        #close the file
        f.close()
        
        #append the new score and name to the lists
        scores.append(self.score)
        names.append(username)
        
        #create a temporary score list
        tempScores = []
        
        #for all the scores
        for i in range(len(scores)):
            #find the scores in the list
            temp = scores[i]
            
            #if the score is empty
            if temp == "":
                #if the game is tic tac toe, make the temp score unachievably high so that it will be sorted last
                if self.gameName == "Tic Tac Toe":
                    temp = "100"
                #if the game is one of the other two games, make the temp score low so that it will be sorted last
                else:
                    temp = "-1"
            
            #add the score to the temporary list
            tempScores.append(int(temp))
        
        #sort the scores
        scores,names = self.insertionSort(tempScores,scores,names)
        
        #remove the last score and name on the list so that there are only the top 5 scores
        scores.pop(len(names)-1)
        names.pop(len(names)-1)
        
        #update the scores in the text file
        self.updateScores(scores,names)
        
        #go to your score page
        self.toYourScore()
    
    # insertionSort - sorts the scores
    # @param - self(object),temp(list int),scores(list str),names(list str)
    # @return - scores(list int),names(list str)
    def insertionSort(self,temp,scores,names):
    
        #start from the second element in the list to the last element
        for i in range(1,len(temp)):
            #the val of the current element for all the lists
            tempCur = temp[i]
            scoresCur = scores[i]
            namesCur = names[i]
            
            #the index of the current element
            pos = i
            
            #if the game is tic tac toe sort the scores from least to greatest
            if self.gameName == "Tic Tac Toe":
                #keep checking the next element down the list if the elememt we are currently on is less the values below it and the index is still greater than 0 
                while tempCur < temp[pos-1] and pos > 0:
                    #switch the current element with the element below it
                    temp[pos] = temp[pos-1]
                    #doing the swtich for the acutal score and names too
                    scores[pos] = scores[pos-1]
                    names[pos] = names[pos-1]
                    
                    #reset the new index the element is
                    pos = pos - 1
            
            #otherwise, for the other two games, sort the scores from greatest to least
            else:
                #keep checking the next element down the list if the elememt we are currently on is greater the values below it and the index is still greater than 0 
                while tempCur > temp[pos-1] and pos > 0:
                    #switch the current element with the element below it
                    temp[pos] = temp[pos-1]
                    #doing the swtich for the acutal score and names too
                    scores[pos] = scores[pos-1]
                    names[pos] = names[pos-1]
                    
                    #reset the new index the element is
                    pos = pos - 1
                    
            #make the value in the position/index you are on right now be hold the value of the element you are trying to sort
            temp[pos] = tempCur
            #doing the change for the acutal score and names too
            scores[pos] = scoresCur
            names[pos] = namesCur
            
        return scores,names
    
    # updateScores - updates the score onto the text file
    # @param - self(object), master(screen), scores(list str), names(list str)
    # @return - none
    def updateScores(self,scores,names):
        #declare variables
        filename = self.gameName
        spaces = filename.count(" ")
        
        #for all the spaces in the game name, take them out
        for i in range(0, spaces):
            #takes out the first space in the string
           filename = filename[0:filename.index(" ")] + filename[filename.index(" ")+1:len(filename)]
        #updates the file name
        filename = filename + ".txt"
        
        #open file to rewrite it
        f = open(filename,'w')
        #set the rank to 1
        rank = 1
        #for all the lines to be outputed in the text file
        for i in range(0,9):
            #if the line is even
            if i % 2 == 0:
                #write the rank, score, and name
                f.writelines(str(rank) + "   " + scores[rank-1] + "   " + names[rank-1] + "\n")
                rank = rank + 1
            #otherwise the line is odd and make the appropriate amount of spaces so that it can be read later
            else:
                f.writelines("               \n")
        
        #close the file
        f.close()
    
    # toYourScore - goes to you score page
    # @param - self(object)
    # @return - none
    def toYourScore(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the your score page
        root = YourScore(newWindow,self.gameName,self.score)
        
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSetting - goes to the settings window
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
     
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the score page
        root = ScoresMain(newWindow)
    
#this class is for the your score page
class YourScore():
    # __init__ - creates the your scores page
    # @param - self(object), master(screen), name(str), score(str)
    # @return - none
    def __init__(self, master, name, score):    
        #declaring attributes
        self.master = master
        self.name = name
        self.score = score
        
        #setting the title and size of the screen
        self.master.title(self.name)
        self.master.geometry("700x492")
        
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main",command = self.toMain)
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        #creates the title/header of the screen and outputs it
        self.header = Label(self.master, text = self.name, font = ("Helvetica",50))
        self.header.pack()
        
        #creates and outputs the label indicating where your score will be shown
        self.yourScoreLbl = Label(self.master, text = "\nYour Score", font = ("Helvetica",30))
        self.yourScoreLbl.pack()
        
        #creates and outputs the lable showing your score
        self.scoreLbl = Label(self.master, text = self.score + "\n", font = ("Helvetica",45))
        self.scoreLbl.pack()
        
        #creates and outputs the button to continue
        self.done = Button(self.master, text = "Done", font = ("Helvetica",22), command = self.toMain)
        self.done.pack()
        
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSetting - goes to the settings window
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
     
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the score page
        root = ScoresMain(newWindow)

#this class is for the each game's score page
class GameScores():
    # __init__ - creates the scores page for all the game
    # @param - self(object), master(screen), name(str)
    # @return - none
    def __init__(self, master, name):
        #declaring attributes
        self.master = master
        self.name = name
        #setting the title and size of the screen
        self.master.title(self.name+" Scores")
        self.master.geometry("700x492")
    
        #creating a menubar
        menubar = Menu(self.master)
        
        #adding a new menu
        filemenu = Menu(menubar, tearoff=0)
        #adding commands to the file menu
        filemenu.add_command(label = "New", command = self.makeNew)
        filemenu.add_command(label = "Close Window", command = self.master.withdraw)
        filemenu.add_command(label = "Quit", command = self.master.quit)
        #making the commands cascade
        menubar.add_cascade(label = "File", menu = filemenu)
        
        #adding a new menu
        pathmenu = Menu(menubar,tearoff=0)
        #adding commands to the path menu
        pathmenu.add_command(label = "Main",command = self.toMain)
        pathmenu.add_command(label = "Games",command = self.toPlay)
        pathmenu.add_command(label = "Settings", command = self.toSetting)
        pathmenu.add_command(label = "Scores", command = self.toScores)
        #making the commands cascade
        menubar.add_cascade(label = "Pages", menu = pathmenu)
        
        #putting the menubar on the screen         
        self.master.config(menu = menubar)
        
        self.header = Label(self.master, text = self.name, font = ("Helvetica",50))
        self.header.pack()
        
        self.rankLbl = Label(self.master, text =  "Rank", font = ("Helvetica",20))
        self.scoreLbl = Label(self.master, text = "Score", font = ("Helvetica",20))
        self.nameLbl = Label(self.master, text = "Name", font = ("Helvetica",20))
        
        labels = [self.rankLbl,self.scoreLbl,self.nameLbl]
        
        for i in range(0,len(labels)):
            labels[i].place(x = 23 + i*233, y = 120)
        
        self.rankListbox = Listbox(self.master, width = 15, height = 10, font = ("Helvetica",15))
        self.rankListbox.pack(padx=30, side=LEFT)
        
        
        self.scoreListbox = Listbox(self.master, width = 15, height = 10, font = ("Helvetica",15))
        self.scoreListbox.pack(padx=30, side=LEFT)
        
        self.nameListbox = Listbox(self.master, width = 15, height = 10, font = ("Helvetica",15))
        self.nameListbox.pack(padx=30, side=LEFT)
        
        ranks, scores, names = self.readFile()
        
        for i in range(0,len(ranks)):
            self.rankListbox.insert(i,ranks[i])
            self.scoreListbox.insert(i,scores[i])
            self.nameListbox.insert(i,names[i])
        
        self.backBtn = Button(self.master, text = "Back", font = ("Helvetica",15), command = self.toScores)
        self.backBtn.place(x = 0, y = 452, width = 100)
    
    # readFile - reads and records the game's score files
    # @param - self(object)
    # @return - none
    def readFile(self):
        #declaring variables
        filename = self.name
        ranks = []
        scores = []
        names = []
        
        #for every spaces there is in the filename, take out the space
        for i in range(0,filename.count(" ")):
            #taking out the space
            filename = filename[0:filename.index(" ")] + filename[filename.index(" ")+1:len(filename)]
        
        #update filename
        filename = filename + ".txt"
        #open the file
        f = open(filename)
        #go through all the lines of the scores
        for i in range(0,9):
            #read the lines and split them by '   ' spaces
            line = f.readline()
            vals = line.split('   ')
            #append the first value to the ranks list
            ranks.append(vals[0])
            #append the second value to the scores lists
            scores.append(vals[1])
            #append the thrid value (no including the \n charcter to the names list)
            names.append(vals[2][0:len(vals[2])-1])
        #close the file
        f.close()
        
        return ranks,scores,names
        
    # toMain - goes to main page
    # @param - self(object)
    # @return - none
    def toMain(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the main page
        root = MainGUI(newWindow)
    
    # makeNew - create new window for the game
    # @param - self(object)
    # @return - none
    def makeNew(self):
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #creates a new window to be the main page
        root = MainGUI(newWindow)
    
    # toSetting - goes to the settings window
    # @param - self(object)
    # @return - none
    def toSetting(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the settings page
        root = Settings(newWindow)
    
    # toPlay - goes the play screen
    # @param - self(object)
    # @return - none
    def toPlay(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the play screen
        root = MainPlay(newWindow)
    
    # toScores - goes to the scores screen
    # @param - self(object)
    # @return - none
    def toScores(self):
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the score page
        root = ScoresMain(newWindow)


#runner

#creates root object
root = Tk()
#makes the window
my_gui = MainGUI(root)
#creates the window on the screen
root.mainloop()