from sys import version_info
print(version_info)

from window import *

# Create main window
#createBasicLayout()

class WakLabOrg(tk.Tk):
    # Show app title
    appName = 'WAK-Lab Organizer'
    appVersion = '0.1.0-alpha.2'
    appCopyright = chr(64) + ' WAK-Lab e.V.'
    # Define size of app window
    windowWidth = 1400
    windowHeight = 700 # 900    
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(self.appName + ' - v' + self.appVersion)

        # Get screen resolution
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        #print(screenWidth,'x',screenHeight)

        # Get offset for center position
        centerX = int(screenWidth/2 - self.windowWidth/2)
        centerY = int(screenHeight/2 - self.windowHeight/2)
        #print(windowWidth,'x',windowHeight)

        # Fixed window size
        self.minsize(self.windowWidth, self.windowHeight)
        self.maxsize(self.windowWidth, self.windowHeight)

        # Place window and create Canvas
        self.geometry(f'{self.windowWidth}x{self.windowHeight}+{centerX}+{centerY}')
        
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
