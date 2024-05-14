import tkinter as tk
from tkinter import ttk
import subprocess
import os

def run_command(command):
    
    res = subprocess.run(command, shell=True, capture_output=True, text=True)

    output_text.insert(tk.END, res.stdout)
    output_text.insert(tk.END, f"$ {command}\n")
    output_text.insert(tk.END, res.stderr)


def execute_command(event=None):
    current_directory = os.getcwd()
    input.insert(tk.END, f"Current Directory: {current_directory}\n")
    command = input.get("1.0", tk.END).strip()
    
    if command.startswith("cd "):
        directory_name = command[3:]
        try:
            os.chdir(directory_name)
        except FileNotFoundError:

            output_text.insert(tk.END, f"Directory not found: {directory_name}\n")
    if command.startswith("clear"):
            output_text.delete(1.0,tk.END)
    else:
        
        run_command(command)

    input.delete("1.0", tk.END)

root = tk.Tk()
root.title("Shell Terminal")
root.config(bg="black")
output_text = tk.Text(root, height=20, width=80)
output_text.config(bg="black",fg="white")
output_text.pack(pady=10, padx=10)
output_text.insert(tk.END, "")

input = tk.Text(root, height=1, width=80)
input.pack(pady=5, padx=10)
input.bind('<Return>', execute_command)

root.mainloop()

