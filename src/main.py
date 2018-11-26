# -- Refined Notepad Python Code
# Christian Lussier

# Imports:
from tkinter import *  # import all tkinter files
import tkinter.filedialog
from tkinter import messagebox  # imports the messagebox


class TextEditor:  # create TextEditor class
    @staticmethod
    def exit_app(event=None):  # function for quitting the program
        root.quit()  # quits the program

    def save_file(self, event=None):  # function for saving files
        # Opens the save as dialog box
        file = tkinter.filedialog.asksaveasfile(
            mode="w", defaultextension=".txt"
        )
        if cond is not None:  # !=
            filedata = self.text_area.get("1.0", END + "-1c")
            file.write(filedata)  # saves the file's data/info to the file
            file.close()  # closes the file

    def open_file(self, event=None):  # function for openign a file
        txt_file = tkinter.filedialog.askopenfilename(
            parent=root, initialdir=""
        )  # does variety of tasks, sets the initial directory.
        if txt_file:
            self.text_area.delete(1.0, END)
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())
                root.update_idletasks()

    def __init__(self, root):  # initializes the notepad program
        self.text_to_write = ""
        root.title("Refined Notepad")  # sets the program title
        root.geometry("600x550")  # sets the window size for program
        frame = Frame(root, width=600, height=550)  # sets the window size
        scrollbar = Scrollbar(frame)  # creates a scrollbar
        self.text_area = Text(
            frame, width=600, height=550, yscrollcommand=scrollbar.set,
            padx=10, pady=10
        )  # sets area where text will be, with scrollbar
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side="right", fill="y")  # sets scrollbar location
        self.text_area.pack(side="left", fill="both", expand=True)
        frame.pack()

        the_menu = Menu(root)  # Creates the MAIN/ENTIRE Menu for the program!

        # -------- File Menu --------:
        file_menu = Menu(the_menu, tearoff=0)  # creates menu

        file_menu.add_command(
            label="Open", command=self.open_file
        )  # add item/command to the menu
        file_menu.add_command(
            label="Save", command=self.save_file
        )  # add item/command to the menu

        file_menu.add_separator()  # used for grouping commands

        file_menu.add_command(
            label="Exit", command=self.exit_app
        )  # menu item that allows user to quit the program
        the_menu.add_cascade(
            label="File", menu=file_menu
        )  # Add the pull down menu to the menu bar
        # -------- END File Menu --------

        # -------- Help Menu --------:
        help_menu = Menu(the_menu, tearoff=0)  # creates the help menu

        def show_about_section():  # creates pop-up message for about section
            messagebox.showinfo(
                "About",
                "This program was made to help the creator "
                "learn more about Python.\n"
                "\n"
                "It is still a work in progress.",
            )  # adds content to the pop-up message

        def show_helpcontact_section():
            messagebox.showinfo(
                "Issues?",
                "Please leave an issue in the projects Issue Tracker.\n"
                "\n"
                "https://github.com/lussierc/refinedNotepadPython/issues",
            )

        help_menu.add_command(
            label="About The Program", command=show_about_section
        )  # adds the about command to the help menu's cascade
        help_menu.add_command(
            label="Help", command=show_helpcontact_section
        )  # adds the help menu to the entire menu "the_menu"

        the_menu.add_cascade(
            label="Help", menu=help_menu
        )  # adds the cascading help menu to "the_menu"
        # -------- END Help Menu --------

        root.config(menu=the_menu)  # displays the menu bar


# Run everything:
root = Tk()
text_editor = TextEditor(root)
root.mainloop()
