import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import interface
import os

class Main_Window(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.jobs = []

        self.create_buttons()
        self.create_treeview()
        self.grid_definitions()

    def create_buttons(self):
        self.convert_button = ttk.Button(self, text="convert", command=self.action_convert_button)

        self.new_job_button = ttk.Button(self, text="create new job", command=self.action_new_job_button)

    def create_treeview(self):
        self.jobs_display = ttk.Treeview(self, columns=("directories", "output_format", "options"), show="headings")

        self.jobs_display.heading("directories", text="directories")
        self.jobs_display.heading("output_format", text="output format")
        self.jobs_display.heading("options", text="options")
    
    def grid_definitions(self):
        self.jobs_display.grid(column=0, row=0, columnspan=20, rowspan=8,)
        self.new_job_button.grid(column=0, row=9)
        self.convert_button.grid(column=19, row=9)

    def action_new_job_button(self):
        CJW = Create_Job_Window(self)

    def action_convert_button(self):
        interface.convert_list(self.jobs)

# handles the creation and configuration of data pertaining to a new job, then passes the completed
# Conversion class back to main window and destroys itself
class Create_Job_Window(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.title("Create Job")
        self.resizable(False, False)
        self.input_directory = ""
        self.output_format = ""
        self.output_method = ""
        self.options = ""

        self.create_buttons()
        self.create_textboxes()
        self.grid_definitions()

    def create_buttons(self):
        self.browse_files_button = ttk.Button(self, text="browse files", command=self.action_browse_files_button)

        self.confirm_job_button = ttk.Button(self, text="confirm job", command=self.action_confirm_job_button)

    def create_textboxes(self):
        self.input_directory_textbox = ttk.Entry(self, width=10)
        self.input_directory_textbox.bind("<Return>", self.action_confirm_job_enter)
        self.input_directory_textbox.bind("<KP_Entry>", self.action_confirm_job_enter)
    # input path box is too small
    def grid_definitions(self):
        self.confirm_job_button.grid(column=0, row=0)
        self.browse_files_button.grid(column=9, row=2)
        self.input_directory_textbox.grid(column=0, row=2, columnspan=8)

    def action_browse_files_button(self):
        self.input_directory_textbox.delete(0, "end")
        self.input_directory_textbox.insert(0, askopenfilename())

    def get_data(self):
        self.input_directory = self.input_directory_textbox.get()

    def validate_data(self):
        if not os.path.isfile(self.input_directory):
            return "invalid path error" # in future do something better
        return "valid"

    def action_confirm_job_enter(self, e):
        self.action_confirm_job_button()
    def action_confirm_job_button(self):
        self.get_data()
        if self.validate_data() == "valid":
            self.parent.jobs_display.insert("", "end", values=(self.input_directory, self.output_format, self.output_method, self.options))
            self.parent.jobs.append(interface.Conversion(self.input_directory, self.output_format, self.output_method, self.options))
        print(self.parent.jobs) # TESTING
        print(self.validate_data())
        self.destroy()

def init():
    root = tk.Tk()
    root.title("buccaneer")
    Main_Window(root).grid()
    root.mainloop()

if __name__ == "__main__":
    init()
