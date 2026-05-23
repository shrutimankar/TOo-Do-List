import sqlite3 as sq1
from tkinter import *
from tkinter import messagebox


tasks = []


def add_task():
    task_string = task_field.get()
    if task_string:
        tasks.append(task_string)  
        the_cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task_string,))
        list_update()  
        task_field.delete(0, 'end')  
    else:
        messagebox.showinfo('Error', 'Field is Empty.')  


def list_update():
    clear_list()  
    for task in tasks:
        task_listbox.insert('end', task)  


def delete_task():
    try:
        task_to_delete = task_listbox.get(task_listbox.curselection())  
        tasks.remove(task_to_delete)  
        the_cursor.execute('DELETE FROM tasks WHERE title = ?', (task_to_delete,))
        list_update()  
    except:
        messagebox.showinfo('Error', 'No Task Selected.') 


def delete_all_tasks():
    if messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?'):
        tasks.clear()  
        the_cursor.execute('DELETE FROM tasks') 
        list_update()  


def clear_list():
    task_listbox.delete(0, 'end')  


def close():
    the_connection.commit()  
    the_cursor.close()  
    the_connection.close() 
    guiwindow.destroy()  


def retrieve_database():
    global tasks
    tasks.clear()  
    for row in the_cursor.execute('SELECT title FROM tasks'):  
        tasks.append(row[0])


if __name__ == "__main__":
    
    guiwindow = Tk()
    guiwindow.title("To-Do List")
    guiwindow.geometry("665x400+500+250")
    guiwindow.resizable(False, False)  
    guiwindow.configure(bg="#B5E5CF")  

    
    the_connection = sq1.connect('listofTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)') 

    
    retrieve_database()

    
    function_frame = Frame(guiwindow, bg="#8EE5EE")
    function_frame.pack(side="top", expand=True, fill="both")

    
    task_label = Label(function_frame, text="To-Do LIST \n Enter the Task Title:", font=("arial", "14", "bold"),
                       background="#8EE5EE", foreground="#FF6103")
    task_label.place(x=20, y=30)

    
    task_field = Entry(function_frame, font=("Arial", "14"), width=42, foreground="black", background="white")
    task_field.place(x=180, y=30)


    Button(function_frame, text="Add", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=add_task).place(x=18, y=80)
    
    Button(function_frame, text="Remove", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=delete_task).place(x=240, y=80)
    
    Button(function_frame, text="Remove All", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=delete_all_tasks).place(x=462, y=80)

    
    task_listbox = Listbox(function_frame, font=("arial", "14"), width=42, height=14, bg="white", fg="black", selectbackground="#f8dcaf")
    task_listbox.place(x=20, y=150)

    list_update() 


    task_scrollbar = Scrollbar(function_frame)
    task_scrollbar.place(x=640, y=150, height=232)
    task_listbox.config(yscrollcommand=task_scrollbar.set)
    task_scrollbar.config(command=task_listbox.yview)

    Button(function_frame, text="Close", width=15, bg='#D4AC0D', font=("arial", "14", "bold"), command=close).place(x=462, y=365)


    guiwindow.mainloop()

