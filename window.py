from tkinter import font, ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import PIL

# Colors definition
wlGreen = '#438F49'
wlGrey = '#303030'
wlLightGrey = '#D8D8D8'

print(PIL.__version__)

def start_inventory():
    exit()

def drawTable(table_frame, table_scroll):
    my_table = ttk.Treeview(table_frame,yscrollcommand=table_scroll.set, xscrollcommand =table_scroll.set)
    #my_table.pack()

    table_scroll.config(command=my_table.yview)
    table_scroll.config(command=my_table.xview)

    #define our column
     
    my_table['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

    # format our column

    windowWidth = int(table_frame.winfo_reqwidth()) #.values.astype(int)
    print(windowWidth)
    cwidth = int((windowWidth-120)/5)
    
    my_table.column("#0", width=0,  stretch=NO)
    my_table.column("player_id",anchor=CENTER, width=cwidth)
    my_table.column("player_name",anchor=CENTER,width=cwidth)
    my_table.column("player_Rank",anchor=CENTER,width=cwidth)
    my_table.column("player_states",anchor=CENTER,width=cwidth)
    my_table.column("player_city",anchor=CENTER,width=cwidth)

    #Create Headings
    
    my_table.heading("#0",text="",anchor=CENTER)
    my_table.heading("player_id",text="Id",anchor=CENTER)
    my_table.heading("player_name",text="Name",anchor=CENTER)
    my_table.heading("player_Rank",text="Rank",anchor=CENTER)
    my_table.heading("player_states",text="States",anchor=CENTER)
    my_table.heading("player_city",text="States",anchor=CENTER)

    #add data 
    my_table.insert(parent='',index='end',iid=0,text='',
    values=('1','Ninja','101','Oklahoma', 'Moore'))
    my_table.insert(parent='',index='end',iid=1,text='',
    values=('2','Ranger','102','Wisconsin', 'Green Bay'))
    my_table.insert(parent='',index='end',iid=2,text='',
    values=('3','Deamon','103', 'California', 'Placentia'))
    my_table.insert(parent='',index='end',iid=3,text='',
    values=('4','Dragon','104','New York' , 'White Plains'))
    my_table.insert(parent='',index='end',iid=4,text='',
    values=('5','CrissCross','105','California', 'San Diego'))
    my_table.insert(parent='',index='end',iid=5,text='',
    values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
    my_table.insert(parent='',index='end',iid=6,text='',
    values=('7','RayRizzo','107','Colorado' , 'Denver'))
    my_table.insert(parent='',index='end',iid=7,text='',
    values=('8','Byun','108','Pennsylvania' , 'ORVISTON'))
    my_table.insert(parent='',index='end',iid=8,text='',
    values=('9','Trink','109','Ohio' , 'Cleveland'))
    my_table.insert(parent='',index='end',iid=9,text='',
    values=('10','Twitch','110','Georgia' , 'Duluth'))
    my_table.insert(parent='',index='end',iid=10,text='',
    values=('11','Animus','111', 'Connecticut' , 'Hartford'))
    return my_table
    

def createBasicLayout():

    # Create a window object of tk
    mainWindow = Tk()

    # Define size of app window
    windowWidth = 1400
    windowHeight = 700 # 900

    # Show app title
    appName = 'WAK-Lab Organizer'
    appVersion = '0.1.0-alpha.2'
    appCopyright = chr(64) + ' WAK-Lab e.V.'

    mainWindow.title(appName + ' - v' + appVersion)

    # Get screen resolution
    screenWidth = mainWindow.winfo_screenwidth()
    screenHeight = mainWindow.winfo_screenheight()

    # Get offset for center position
    centerX = int(screenWidth/2 - windowWidth/2)
    centerY = int(screenHeight/2 - windowHeight/2)

    # Fixed window size
    mainWindow.minsize(windowWidth, windowHeight)
    mainWindow.maxsize(windowWidth, windowHeight)

    # Place window and create Canvas
    mainWindow.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

    mainCanvas = Canvas(mainWindow, width=windowWidth, height=windowHeight, highlightthickness=0, borderwidth=0)
    mainCanvas.pack()

    ### Draw GUI elements
    
    separator = 10

    # Draw background
    
    mainCanvas.create_rectangle(0, 0, windowWidth, windowHeight, fill=wlLightGrey, width=0)

    # Draw title bar
    
    heightTitleBar = 200

    mainCanvas.create_rectangle(0, 0, windowWidth, heightTitleBar, fill=wlGreen, width=0)
    mainCanvas.create_text(30, 80, fill='white', anchor=W, font='Verdana 40 bold', text=appName)
    
    # Draw navigation bar
    
    heightNaviBar = 40
    heightSeperator = 10

    pointsOfNaviBar = [0, heightTitleBar, 560, heightTitleBar, 600, heightTitleBar-heightNaviBar, windowWidth, heightTitleBar-heightNaviBar, windowWidth, heightTitleBar+heightSeperator, 0, heightTitleBar+heightSeperator]
    mainCanvas.create_polygon(pointsOfNaviBar, fill=wlGrey, width=0)

    # Navigation
    
    btnCount = 3
    btnStartX = 610
    btnWidth = 160
    btnSeperator = (windowWidth-btnStartX-btnCount*btnWidth)/btnCount
    btnStyle = Style()
    btnStyle.configure('W.TButton', background='#232323', font=('Arial', 12))

    btnSectionMembers = Button(mainWindow, text='Mitglieder')
    btnSectionAccounting = Button(mainWindow, text='Buchführung')
    btnSectionInventory = Button(mainWindow, text='Inventar', command=lambda: start_inventory())
    # btnSectionConfig = Button(mainWindow, text='EINST')
    # btnSectionConfig = Button(mainWindow, style='W.TButton', text='EINST')
    btnSectionMembers.place(x=btnStartX, y=heightTitleBar-heightNaviBar+6, width=btnWidth, height=heightNaviBar+heightSeperator-12)
    btnSectionAccounting.place(x=btnStartX+btnWidth+btnSeperator, y=heightTitleBar-heightNaviBar+6, width=btnWidth, height=heightNaviBar+heightSeperator-12)
    btnSectionInventory.place(x=btnStartX+2*(btnWidth+btnSeperator), y=heightTitleBar-heightNaviBar+6, width=btnWidth, height=heightNaviBar+heightSeperator-12)   
    # btnSectionConfig.place(x=btnStartX+3*(btnWidth+btnSeperator), y=heightTitleBar-heightNaviBar+6, width=btnWidth, height=heightNaviBar+heightSeperator-12)  

    # Draw seperator bar
    # mainCanvas.create_rectangle(0, 200, windowWidth, 215, fill=wlGrey, width=0)

    # Draw side bar / sub navigation
    
    heightBottomBar = 40

    mainCanvas.create_rectangle(0, heightTitleBar, separator, windowHeight-heightBottomBar-separator, fill=wlGreen, width=0)

    pointsOfSideBar = [ separator, heightTitleBar+2*heightSeperator, 
                            80, heightTitleBar+2*heightSeperator, 
                            120, heightTitleBar+6*heightSeperator, 
                            120, windowHeight-heightBottomBar-8*heightSeperator, 
                            80, windowHeight-heightBottomBar-4*heightSeperator, 
                            separator, windowHeight-heightBottomBar-4*heightSeperator]

    mainCanvas.create_polygon(pointsOfSideBar, fill=wlGrey, width=0)

    # Draw Table

    table_frame = Frame(mainWindow,  width=windowWidth-separator-120, height=windowHeight-heightBottomBar-heightTitleBar-2*separator, relief='raised', borderwidth=5) 
    table_frame.pack()

    #scrollbar
    
    table_scroll = Scrollbar(table_frame)
    table_scroll.pack(side=RIGHT, fill=Y)

    table_scroll = Scrollbar(table_frame,orient='horizontal')
    table_scroll.pack(side= BOTTOM,fill=X)

    my_table = drawTable(table_frame, table_scroll)

    my_table.pack()
    table_frame.place(x=separator+120, y=separator+heightTitleBar, width=windowWidth-separator-120, height=windowHeight-heightBottomBar-heightTitleBar-2*separator)

    # Draw bottom bar
    
    mainCanvas.create_rectangle(0, windowHeight-heightBottomBar-heightSeperator, windowWidth, windowHeight-heightBottomBar, fill=wlGreen, width=0)
    mainCanvas.create_rectangle(0, windowHeight-heightBottomBar, windowWidth, windowHeight, fill=wlGrey, width=0)
    mainCanvas.create_text(10, windowHeight-heightBottomBar/2, fill='white', anchor=W, font='Verdana', text=appCopyright)
    mainCanvas.create_text(windowWidth-10, windowHeight-heightBottomBar/2, fill='white', anchor=E, font='Verdana', text=appVersion)

    # Show logo
    # logo = Image.open('images/logo-current-version.png')
    # logo = ImageTk.PhotoImage(logo)
    # logo_label = Label(image=logo)
    # logo_label.image = logo
    # logo_label.place(x=0, y=0)

    mainWindow.mainloop()
