from window import *

# Create main window
#createBasicLayout()

# Show app title

# Define size of app window
windowWidth = 1400
windowHeight = 700 # 900



class WakLabOrg(tk.Tk):
    appName = 'WAK-Lab Organizer'
    appVersion = '0.1.0-alpha.2'
    appCopyright = chr(64) + ' WAK-Lab e.V.'
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(self.appName + ' - v' + self.appVersion)

        # Get screen resolution
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        # Get offset for center position
        centerX = int(screenWidth/2 - windowWidth/2)
        centerY = int(screenHeight/2 - windowHeight/2)

        # Fixed window size
        self.minsize(windowWidth, windowHeight)
        self.maxsize(windowWidth, windowHeight)

        # Place window and create Canvas
        self.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

app = WakLabOrg()
app.mainloop()
