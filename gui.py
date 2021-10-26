import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import interface

class MainWindow(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.jobs = []

        self.create_buttons()
        self.create_treeview()
        self.grid_definitions()

    def create_buttons(self):
        self.browse_files_button = ttk.Button(self, text="browse files", command=self.action_browse_files_button)

        self.convert_button = ttk.Button(self, text="convert", command=self.action_convert_button)

        self.new_job_button = ttk.Button(self, text="create new job", command=self.action_new_job_button)

    def create_treeview(self):
        self.jobs_display = ttk.Treeview(self, columns=("directories", "output_format", "options"), show="headings")

        self.jobs_display.heading("directories", text="directories")
        self.jobs_display.heading("output_format", text="output format")
        self.jobs_display.heading("options", text="options")
    
    def grid_definitions(self):
        self.jobs_display.grid(column=0, row=0)
        self.new_job_button.grid(column=0, row=1)
        self.convert_button.grid(column=1, row=1)
        self.browse_files_button.grid(column=2, row=1)

    def action_new_job_button(self):
        CJW = Create_Job_Window(self)

    def action_browse_files_button(self):
        self.directory = askopenfilename()
    
    def action_convert_button(self):
        interface.convert_list(self.jobs)

# handles the creation and configuration of data pertaining to a new job, then passes the completed
# Conversion class back to main window and destroys itself
class Create_Job_Window(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.input_directory = ""
        self.output_format = ""
        self.output_method = ""
        self.options = ""

        self.create_buttons()
        self.grid_definitions()

    def create_buttons(self):
        self.confirm_job_button = ttk.Button(self, text="confirm job", command=lambda: self.action_confirm_job_button(self.parent))

    def grid_definitions(self):
        self.confirm_job_button.grid(column=0, row=0)

    def action_confirm_job_button(self, parent):
        parent.jobs_display.insert("", "end", values=(self.input_directory, self.output_format, self.output_method, self.options))
        parent.jobs.append(interface.Conversion(self.input_directory, self.output_format, self.output_method, self.options))

        print(parent.jobs) # TESTING
        self.destroy()

def init():
    root = tk.Tk()
    MainWindow(root).grid()
    root.mainloop()

init()