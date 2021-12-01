import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import interface
import os
from collections.abc import Callable

class Main_Window(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.jobs: list[interface.Conversion] = []

        self.create_buttons()
        self.create_treeview()
        self.grid_definitions()

    def create_buttons(self) -> None:
        self.convert_button = ttk.Button(self, text="convert", command=self.action_convert_button)

        self.new_job_button = ttk.Button(self, text="create new job", command=self.action_new_job_button)

    def create_treeview(self) -> None:
        self.jobs_display = ttk.Treeview(self, columns=("directories", "output_format", "options"), show="headings")

        self.jobs_display.heading("directories", text="directories")
        self.jobs_display.heading("output_format", text="output format")
        self.jobs_display.heading("options", text="options")
    
    def grid_definitions(self) -> None:
        self.jobs_display.grid(column=0, row=0, columnspan=20, rowspan=8,)
        self.new_job_button.grid(column=0, row=9)
        self.convert_button.grid(column=19, row=9)

    def action_new_job_button(self) -> None:
        self.CJW: JobWindow = JobWindow(self)

    def action_convert_button(self) -> None:
        interface.convert_list(self.jobs)

class JobWindow(tk.Toplevel):
    """Handles creation and configuration of a new conversion job, then passes the completed interface.Conversion object back to the Main_Window."""
    def __init__(self, parent, *args, **kwargs) -> None:
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.title("Create Job")
        self.resizable(False, False)
        self.input_directory: str = ""
        self.output_format: str = ""
        self.output_method: Callable[[str, str], str] = interface.output_method_keep_name_path
        self.options: str = ""

        self.create_directorybar()
        self.create_confirmcancelbuttons()
        self.grid_definitions()

    def create_directorybar(self) -> None:
        self.input_directory_textbox: ttk.Entry = ttk.Entry(self, width=50)
        self.input_directory_textbox.bind("<Return>", self.action_confirm_job_enter)
        self.input_directory_textbox.bind("<KP_Enter>", self.action_confirm_job_enter)
        self.browse_files_button: ttk.Button = ttk.Button(self, text="browse files", command=self.action_browse_files_button)

    def create_confirmcancelbuttons(self) -> None:
        self.confirm_job_button: ttk.Button = ttk.Button(self, text="confirm job", command=self.action_confirm_job_button)
        self.cancel_button: ttk.Button = ttk.Button(self, text="cancel", command=self.action_cancel_button) 

    def grid_definitions(self) -> None:
        self.confirm_job_button.grid(column=0, row=0)
        self.cancel_button.grid(column=1, row=0)
        self.browse_files_button.grid(column=9, row=2)
        self.input_directory_textbox.grid(column=0, row=2, columnspan=8)

    def action_browse_files_button(self) -> None:
        self.input_directory_textbox.delete(0, "end")
        self.input_directory_textbox.insert(0, askopenfilename())

    def get_data(self) -> None:
        self.input_directory = self.input_directory_textbox.get()

    def validate_data(self) -> str:
        """Validate the entered data."""
        #TODO: do this better with some error enum or something
        if not os.path.isfile(self.input_directory):
            return "invalid path error"
        return "valid"

    def action_confirm_job_enter(self, e) -> None:
        self.action_confirm_job_button()
    def action_confirm_job_button(self) -> None:
        self.get_data()
        if self.validate_data() == "valid":
            self.parent.jobs_display.insert("", "end", values=(self.input_directory, self.output_format, self.output_method, self.options))
            self.parent.jobs.append(interface.Conversion(self.input_directory, self.output_format, self.output_method, self.options))
        print(self.parent.jobs) # TESTING
        print(self.validate_data())
        self.destroy()

    def action_cancel_button(self) -> None:
        self.destroy()

def init() -> None:
    root: tk.Tk = tk.Tk()
    root.title("buccaneer")
    Main_Window(root).grid()
    root.mainloop()

if __name__ == "__main__":
    init()
