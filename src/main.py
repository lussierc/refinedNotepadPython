# -- Refined Notepad Python Code
# Christian Lussier

"""This file contains the code for the RefinedNotepadPython program.
This program is a simple notepad application for writing quick documents."""

# Imports:
from tkinter import *  # import all tkinter files
import tkinter.filedialog
from tkinter import messagebox  # imports the messagebox


class TextEditor:  # create TextEditor class
    @staticmethod
    def exit_app(event=None):
        """Function for quitting the program."""
        root.quit()  # quits the program

    def save_file(self, event=None):  # function for saving files
        """Save the file currently being worked on."""
        # Opens the save as dialog box
        file = tkinter.filedialog.asksaveasfile(
            mode="w", defaultextension=".txt"
        )
        if file is not None:  # !=
            filedata = self.text.get("1.0", END + "-1c")
            file.write(filedata)  # saves the file's data/info to the file
            file.close()  # closes the file

    def open_file(self, event=None):
        """Function for opening files. Uses a dialog/pop-up box."""
        txt_file = tkinter.filedialog.askopenfilename(
            parent=root, initialdir=""
        )  # does variety of tasks, sets the initial directory.
        if txt_file:
            self.text.delete(1.0, END)  # deletes current text
            with open(txt_file) as _file:
                self.text.insert(1.0, _file.read())
                root.update_idletasks()

    def undo(self, *args):
        """Function for undoing actions in the notepad."""
        self.text.edit_undo()  # undos an action

    def redo(self):
        """Function for redoing actions in the notepad."""
        self.text.edit_redo()  # redos an action

    def copy(self):
        """Function for copying text in the notepad."""
        copy_item = self.text.selection_get()
        self.clipboard = copy_item  # gets the copied item

    def cut(self):
        """Function for cutting text in the notepad."""
        cut_item = self.text.selection_get()  # gets the selected text to cut
        self.clipboard = cut_item  # adds the selected text to the clipboard
        self.text.delete(SEL_FIRST, SEL_LAST)  # deletes the cut text

    def paste(self):
        """Function for pasting (copied or cut) text in the notepad."""
        self.text.insert(INSERT, self.clipboard)  # inserts copied or cut text

    def __init__(self, root):
        """The program's 'driver' function. Initializes the program."""
        self.text_to_write = ""
        root.title("Refined Notepad")  # sets the program title
        root.geometry("600x550")  # sets the window size for program
        frame = Frame(root, width=600, height=550)  # sets the frame size
        scrollbar = Scrollbar(frame)  # creates a scrollbar
        self.text = Text(
            frame, width=600, height=550, yscrollcommand=scrollbar.set,
            padx=10, pady=10, undo=True
        )  # sets area where text will be, with scrollbar
        scrollbar.config(command=self.text.yview)
        scrollbar.pack(side="right", fill="y")  # sets scrollbar location
        self.text.pack(side="left", fill="both", expand=True)
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

        file_menu.add_separator()  # separator for better grouping commands

        file_menu.add_command(
            label="Exit", command=self.exit_app
        )  # menu item that allows user to quit the program

        the_menu.add_cascade(
            label="File", menu=file_menu
        )  # Add the pull down menu to the menu bar
        # -------- END File Menu --------

        # -------- Edit menu --------:
        edit_menu = Menu(the_menu, tearoff=0)  # creates menu

        edit_menu.add_command(
            label="Undo", command=self.undo
        )  # add item/command to the menu

        edit_menu.add_command(
            label="Redo", command=self.redo
        )  # add item/command to the menu

        edit_menu.add_separator()  # separator for better grouping commands

        edit_menu.add_command(
            label="Copy", command=self.copy
        )  # add item/command to the menu

        edit_menu.add_command(
            label="Cut", command=self.cut
        )  # add item/command to the menu

        edit_menu.add_command(
            label="Paste", command=self.paste
        )  # add item/command to the menu

        the_menu.add_cascade(
            label="Edit", menu=edit_menu
        )  # Add the pull down menu to the menu bar

        # -------- Help Menu --------:
        help_menu = Menu(the_menu, tearoff=0)  # creates the help menu

        def show_about_section():  # creates pop-up message for about section
            """This function shows the about section."""
            messagebox.showinfo(
                "About",
                "This program was made to help the creator "
                "learn more about Python.\n"
                "\n"
                "It is still a work in progress.",
            )  # adds content to the pop-up message

        def show_helpcontact_section():
            """This function shows the help/contact section."""
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


# Run the program:
root = Tk()
text_editor = TextEditor(root)
root.mainloop()
