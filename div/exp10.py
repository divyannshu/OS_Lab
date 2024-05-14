import os
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.file_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.file_listbox.bind("<Double-Button-1>", self.open_directory)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.file_listbox.yview)

        self.back_button = tk.Button(self.root, text="Back", command=self.navigate_back)
        self.back_button.pack(pady=5)

        self.directory_stack = []  # Stack to store directory history
        # self.current_directory = os.path.expanduser('~')  # Initial directory set to home directory
        self.populate_listbox()
        # Buttons
        self.create_dir_button = tk.Button(self.root, text="Create Directory", command=self.create_directory, bg="blue", fg="white")
        self.create_dir_button.pack(side="left", padx=5, pady=5)

        self.delete_dir_button = tk.Button(self.root, text="Delete Directory", command=self.delete_directory, bg="red", fg="white")
        self.delete_dir_button.pack(side="left", padx=5, pady=5)

        self.create_file_button = tk.Button(self.root, text="Create File", command=self.create_file, bg="blue", fg="white")
        self.create_file_button.pack(side="left", padx=5, pady=5)

        self.delete_file_button = tk.Button(self.root, text="Delete File", command=self.delete_file, bg="red", fg="white")
        self.delete_file_button.pack(side="left", padx=5, pady=5)

        self.edit_file_button = tk.Button(self.root, text="Edit File", command=self.edit_file, bg="orange", fg="white")
        self.edit_file_button.pack(side="left", padx=5, pady=5)

    def populate_listbox(self):
        # Clear existing items
        self.file_listbox.delete(0, tk.END)

        # Get list of files in current directory
        # directory_name="C:\Users\Divyanshu"

        current_dir = os.getcwd()
        files = os.listdir(current_dir)

        # Add files to listbox
        for file in files:
            self.file_listbox.insert(tk.END, file)

    def create_directory(self):
        directory_name = simpledialog.askstring("Create Directory", "Enter directory name:")
        if directory_name:
            try:
                os.mkdir(directory_name)
                messagebox.showinfo("Success", f"Directory '{directory_name}' created successfully.")
                self.populate_listbox()  # Refresh list after creation
            except OSError as e:
                messagebox.showerror("Error", f"Failed to create directory: {e}")

    def delete_directory(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            directory_name = self.file_listbox.get(selected_index)
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{directory_name}'?")
            if confirm:
                try:
                    os.rmdir(directory_name)
                    messagebox.showinfo("Success", f"Directory '{directory_name}' deleted successfully.")
                    self.populate_listbox()  # Refresh list after deletion
                except OSError as e:
                    messagebox.showerror("Error", f"Failed to delete directory: {e}")
        else:
            messagebox.showwarning("Warning", "Please select a directory to delete.")

    def create_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            directory_name = self.file_listbox.get(selected_index)
        else:
            directory_name=os.getcwd()
        file_name = simpledialog.askstring("Create File", f"Enter file name in '{directory_name}':")
        if file_name:
            try:
                    if directory_name:
                     with open(os.path.join(directory_name, file_name), 'w'):
                        pass  # Create an empty file
                    else:
                        directory_name=os.getcwd()
                        with open(os.path.join(directory_name, file_name), 'w'):
                         pass 
                    messagebox.showinfo("Success", f"File '{file_name}' created successfully in '{directory_name}'.")
                    self.populate_listbox()  # Refresh list after creation
            except OSError as e:
                    messagebox.showerror("Error", f"Failed to create file: {e}")
        # else:
        #     messagebox.showwarning("Warning", "Please select a directory to create a file inside.")

    def delete_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            file_name = self.file_listbox.get(selected_index)
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{file_name}'?")
            if confirm:
                try:
                    os.remove(file_name)
                    messagebox.showinfo("Success", f"File '{file_name}' deleted successfully.")
                    self.populate_listbox()  # Refresh list after deletion
                except OSError as e:
                    messagebox.showerror("Error", f"Failed to delete file: {e}")
        else:
            messagebox.showwarning("Warning", "Please select a file to delete.")

    def edit_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            file_name = self.file_listbox.get(selected_index)
            try:
                os.system(f'notepad "{file_name}"')  # Open file in Notepad for editing
            except OSError as e:
                messagebox.showerror("Error", f"Failed to edit file: {e}")
        else:
            messagebox.showwarning("Warning", "Please select a file to edit.")

    def open_directory(self, event):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            directory_name = self.file_listbox.get(selected_index)
            self.directory_stack.append(os.getcwd())  # Push current directory to stack
            os.chdir(directory_name)
            self.populate_listbox()

    def navigate_back(self):
        if self.directory_stack:
            previous_directory = self.directory_stack.pop()  # Pop previous directory from stack
            os.chdir(previous_directory)
            self.populate_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()
