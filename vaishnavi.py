import sqlite3 as sq1
from tkinter import *
from tkinter import messagebox

# Initialize global variables
tasks = []

# Function to add a task
def add_task():
    task_string = task_field.get()
    if task_string:
        tasks.append(task_string)  # Add the task to the list
        try:
            the_cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task_string,))
            the_connection.commit()  # Commit the transaction
            list_update()  # Update the listbox
            task_field.delete(0, 'end')  # Clear the entry field
        except Exception as e:
            messagebox.showerror('Database Error', f'Error adding task: {e}')
    else:
        messagebox.showinfo('Error', 'Field is Empty.')  # Show error message

# Function to update the task list in the Listbox
def list_update():
    clear_list()  # Clear the current listbox
    for task in tasks:
        task_listbox.insert('end', task)  # Insert tasks into the listbox

# Function to delete a selected task
def delete_task():
    try:
        task_to_delete = task_listbox.get(task_listbox.curselection())  # Get selected task
        tasks.remove(task_to_delete)  # Remove task from the list
        try:
            the_cursor.execute('DELETE FROM tasks WHERE title = ?', (task_to_delete,))
            the_connection.commit()  # Commit the transaction
            list_update()  # Update the listbox  
        except Exception as e:
            messagebox.showerror('Database Error', f'Error deleting task: {e}')
    except:
        messagebox.showinfo('Error', 'No Task Selected.')  # Show error if no task is selected

# Function to delete all tasks
def delete_all_tasks():
    if messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?'):
        tasks.clear()  # Clear the task list in memory
        try:
            the_cursor.execute('DELETE FROM tasks')  # Remove all tasks from the database
            the_connection.commit()  # Commit the transaction
            list_update()  # Update the listbox
        except Exception as e:
            messagebox.showerror('Database Error', f'Error deleting all tasks: {e}')

# Function to clear the Listbox
def clear_list():
    task_listbox.delete(0, 'end')  # Remove all items from the listbox

# Function to close the application
def close():
    try:
        the_connection.commit()  # Commit any changes before closing
    finally:
        the_cursor.close()  # Close the cursor
        the_connection.close()  # Close the database connection
        guiwindow.destroy()  # Close the window

# Function to retrieve tasks from the database
def retrieve_database():
    global tasks
    tasks.clear()  # Clear the current task list
    try:
        for row in the_cursor.execute('SELECT title FROM tasks'):  # Retrieve tasks from the database
            tasks.append(row[0])
    except Exception as e:
        messagebox.showerror('Database Error', f'Error retrieving tasks: {e}')

# Main GUI setup
if _name_ == "_main_":  # Corrected the condition here
    # Initialize Tkinter window
    guiwindow = Tk()
    guiwindow.title("To-Do List")
    guiwindow.geometry("665x400+500+250")
    guiwindow.resizable(False, False)  # Disable resizing the window
    guiwindow.configure(bg="#ADD8E6")  # Light Blue Background color

    # Connect to SQLite database
    try:
        the_connection = sq1.connect('listofTasks.db')
        the_cursor = the_connection.cursor()
        the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')  # Create tasks table if not exists
    except Exception as e:
        messagebox.showerror('Database Error', f'Error connecting to the database: {e}')
        guiwindow.destroy()

    # Retrieve tasks from the database
    retrieve_database()

    # GUI Frame with new background color
    function_frame = Frame(guiwindow, bg="#87CEFA")  # Light blue for the frame
    function_frame.pack(side="top", expand=True, fill="both")

    # Task label with updated foreground and background colors
    task_label = Label(function_frame, text="To-Do LIST \n Enter the Task Title:", font=("arial", "14", "bold"),
                       background="#87CEFA", foreground="#FF4500")  # Orange text for the label
    task_label.place(x=20, y=30)

    # Task entry field with a new background color
    task_field = Entry(function_frame, font=("Arial", "14"), width=42, foreground="black", background="#FFFFFF")  # White background for entry field
    task_field.place(x=180, y=30)

    # Add task button with orange color
    Button(function_frame, text="Add", width=15, bg='#FFA500', font=("arial", "14", "bold"), command=add_task).place(x=18, y=80)
    # Remove task button with orange color
    Button(function_frame, text="Remove", width=15, bg='#FFA500', font=("arial", "14", "bold"), command=delete_task).place(x=240, y=80)
    # Delete all tasks button with orange color
    Button(function_frame, text="Remove All", width=15, bg='#FFA500', font=("arial", "14", "bold"), command=delete_all_tasks).place(x=462, y=80)

    # Listbox to display tasks with a white background
    task_listbox = Listbox(function_frame, font=("arial", "14"), width=42, height=14, bg="#FFFFFF", fg="black", selectbackground="#FFD700")  # White background for listbox
    task_listbox.place(x=20, y=150)

    list_update()  # Update the listbox with current tasks

    # Scrollbar for the listbox with updated position
    task_scrollbar = Scrollbar(function_frame)
    task_scrollbar.place(x=640, y=150, height=232)
    task_listbox.config(yscrollcommand=task_scrollbar.set)
    task_scrollbar.config(command=task_listbox.yview)

    # Close button with orange color
    Button(function_frame, text="Close", width=15, bg='#FFA500', font=("arial", "14", "bold"), command=close).place(x=462, y=365)

    # Start the GUI loop
    guiwindow.mainloop()