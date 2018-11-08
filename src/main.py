## Refined Notepad Python Code:
# Imports:
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox

class TextEditor: #set class
    @staticmethod
    def quit_app(event = None): # function for quitting the program
        root.quit() # quits the program

    def save_file(self, event = None): # function for saving files
        # Opens the save as dialog box
        file = tkinter.filedialog.asksaveasfile(mode = 'w')
        if file != None:
            data = self.text_area.get('1.0', END + '-1c')
            file.write(data) # saves the data/info to the file
            file.close() # closes the file

    def open_file(self, event = None): # function for openign a file
        txt_file = tkinter.filedialog.askopenfilename(parent = root, initialdir = '') # does variety of tasks, sets the initial directory.
        if txt_file:
            self.text_area.delete(1.0, END)
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())
                root.update_idletasks()

    def __init__(self, root): # initializes the notepad program
        self.text_to_write = ""
        root.title("Refined Notepad") # sets the program title
        root.geometry("600x550") # sets the window size for program
        frame = Frame(root, width = 600, height = 550) # sets the frame size for program
        scrollbar = Scrollbar(frame) # creates a scrollbar for scrolling through text
        self.text_area = Text(frame, width = 600, height = 550, yscrollcommand = scrollbar.set, padx = 10, pady = 10) # sets area where text will be, with scrollbar
        scrollbar.config(command = self.text_area.yview)
        scrollbar.pack(side = "right", fill = "y") # sets scrollbar location
        self.text_area.pack(side = "left", fill = "both", expand = True)
        frame.pack()

        the_menu = Menu(root) #creates menu
        file_menu = Menu(the_menu, tearoff = 0) #creates menu

        file_menu.add_command(label = "Open", command = self.open_file) # add item/command to the menu
        file_menu.add_command(label = "Save", command = self.save_file) # add item/command to the menu
        file_menu.add_separator() # used for grouping commands
        file_menu.add_command(label = "Quit", command = self.quit_app) # menu item that allows user to quit the program
        the_menu.add_cascade(label = "File", menu = file_menu) # Add the pull down menu to the menu bar

        help_menu = Menu(the_menu, tearoff = 0) # creates the help menu

        def show_about(event=None):
            messagebox.showwarning("About", "This program was made to help the creator learn more about Python. It is still a work in progress!")

        help_menu.add_command(label = "About The Program", command = show_about)

        the_menu.add_cascade(label = "Help", menu = help_menu) # adds the help menu to the entire menu "the_menu"

        root.config(menu = the_menu) # displays the menu bar

root = Tk()
text_editor = TextEditor(root)
root.mainloop()
