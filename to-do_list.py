import tkinter as tk
import tkinter.messagebox
from typing import List

def save_tasks(tasks: List[str], filename: str) -> None:
    """Saves the list of tasks to a text file."""
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks(filename: str) -> List[str]:
    """Loads tasks from a text file, handling potential errors."""
    tasks = []
    try:
        with open(filename, "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # Ignore file not found error
    return tasks

def entertask():
    """Opens a new window to take task input and adds it to the list."""
    input_text = ""

    def add():
        nonlocal input_text  # Use `nonlocal` to modify variable from outer scope
        input_text = entry_task.get(1.0, "end-1c")
        if not input_text:
            tkinter.messagebox.showwarning("Warning!", "Please enter some text")
        else:
            listbox_task.insert(tk.END, input_text)
            tasks.append(input_text)  # Add task to tasks list
            save_tasks(tasks, "tasks.txt")  # Save updated tasks
            root1.destroy()  # Close the input window

    root1 = tk.Tk()
    root1.title("Add Task")
    entry_task = tk.Text(root1, width=40, height=4)
    entry_task.pack()
    button_add = tk.Button(root1, text="Add Task", command=add)
    button_add.pack()
    root1.mainloop()

def deletetask():
    """Deletes the selected task from the listbox and tasks list."""
    selected = listbox_task.curselection()
    if selected:
        index = selected[0]
        listbox_task.delete(index)
        del tasks[index]  # Remove task from tasks list
        save_tasks(tasks, "tasks.txt")  # Save updated tasks

def markcompleted():
    """Marks the selected task as completed with a checkmark."""
    selected = listbox_task.curselection()
    if selected:
        index = selected[0]
        temp_marked = listbox_task.get(index) + " ✔"
        listbox_task.delete(index)
        listbox_task.insert(index, temp_marked)

# Main window setup
window = tk.Tk()
window.title("DataFlair Python To-Do List APP")

tasks = load_tasks("tasks.txt")  # Load tasks from file on startup

frame_task = tk.Frame(window)
frame_task.pack()

listbox_task = tk.Listbox(
    frame_task, bg="white", fg="black", height=15, width=50, font="Helvetica"
)
listbox_task.pack(side=tk.LEFT)

scrollbar_task = tk.Scrollbar(frame_task)
scrollbar_task.pack(side=tk.RIGHT, fill=tk.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Populate listbox with loaded tasks
for task in tasks:
    listbox_task.insert(tk.END, task)

# Button widgets
entry_button = tk.Button(window, text="Add Task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = tk.Button(window, text="Delete Selected Task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = tk.Button(window, text="Mark as Completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
