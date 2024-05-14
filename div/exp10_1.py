import tkinter as tk
from tkinter import filedialog, messagebox
from filesystem import LocalFileSystem

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File System GUI")
        self.geometry("400x300")
        
        self.file_system = LocalFileSystem()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label_path = tk.Label(self, text="Path:")
        self.label_path.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        
        self.entry_path = tk.Entry(self, width=30)
        self.entry_path.grid(row=0, column=1, padx=10, pady=10)
        
        self.button_browse = tk.Button(self, text="Browse", command=self.browse)
        self.button_browse.grid(row=0, column=2, padx=10, pady=10)
        
        self.text_output = tk.Text(self, height=10, width=50)
        self.text_output.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.button_list_files = tk.Button(self, text="List Files", command=self.list_files)
        self.button_list_files.grid(row=2, column=0, padx=10, pady=10)
        
        self.button_list_directories = tk.Button(self, text="List Directories", command=self.list_directories)
        self.button_list_directories.grid(row=2, column=1, padx=10, pady=10)
        
    def browse(self):
        path = filedialog.askdirectory()
        if path:
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, path)
    
    def list_files(self):
        path = self.entry_path.get()
        if path:
            try:
                files = self.file_system.list_files(path)
                self.text_output.delete(1.0, tk.END)
                self.text_output.insert(tk.END, "\n".join(files))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Please select a directory.")
    
    def list_directories(self):
        path = self.entry_path.get()
        if path:
            try:
                directories = self.file_system.list_directories(path)
                self.text_output.delete(1.0, tk.END)
                self.text_output.insert(tk.END, "\n".join(directories))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Please select a directory.")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
