from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# All functions declared here
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt",
                            filetypes=[
                                ("All Files", "*.*"),
                                ("Text Documents", "*.txt")
                            ]
                        )
    if file == "":
        file = None
    else: 
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()



def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension = ".txt",
                                filetypes=[
                                    ("All Files", "*.*"),
                                    ("Text Documents", "*.txt")
                            ])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        #save the file
         f = open(file, "w")
         f.write(TextArea.get(1.0,END))
         f.close()   

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("About Notepad", "Notepad by Pulkit")


if __name__ == "__main__":
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("")  #for setting icon
    root.geometry("788x520")  #dimensions of notepad

    #adding Textarea
    TextArea = Text(root, font="lucida 13")
    file = None   #file to open in notepad  
    TextArea.pack(expand=True, fill=BOTH)  

    # adding menubar
    MenuBar = Menu(root)

    # -------------- File Menu Making ---------------
    FileMenu = Menu(MenuBar, tearoff = 0)

    # To open new file
    FileMenu.add_command(label="New", command = newFile)
    # To open already existing file
    FileMenu.add_command(label="Open..", command = openFile)
    # To save the current file
    FileMenu.add_command(label="Save", command = saveFile)
    # Add a seperator
    FileMenu.add_separator()
    # Exit command
    FileMenu.add_command(label="Exit", command=quit)

    MenuBar.add_cascade(label = "File", menu=FileMenu)

    # -------------- Edit Menu Making --------------
    EditMenu = Menu(MenuBar, tearoff = 0)

    # Cut,copy,paste features
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)

    MenuBar.add_cascade(label = "Edit", menu = EditMenu)

    # --------------- Help Menu Making ---------------
    HelpMenu = Menu(MenuBar, tearoff=0)

    # About section
    HelpMenu.add_command(label = "About Notepad", command = about)

    MenuBar.add_cascade(label = "Help", menu = HelpMenu)


    root.config(menu=MenuBar)
    # menubar ends here

    # Adding Scrollbar
    Scrollbar = Scrollbar(TextArea)
    Scrollbar.pack(side = RIGHT, fill=Y)
    Scrollbar.config(command = TextArea.yview)
    TextArea.config(yscrollcommand=Scrollbar.set)

    # Footer -----------
    root.mainloop()