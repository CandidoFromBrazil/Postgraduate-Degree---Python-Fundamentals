import tkinter as tk
from tkinter import messagebox

def show_popup():
    """Function to trigger the message box."""
    messagebox.showinfo("Greeting", "Hello! This is your Tkinter message.")

def main():
    # 1. Initialize the main window
    root = tk.Tk()
    root.title("Python Message App")
    root.geometry("300x200")

    # 2. Add a label for some context
    label = tk.Label(root, text="Click the button below:", pady=20)
    label.pack()

    # 3. Create a button that calls show_popup when clicked
    msg_button = tk.Button(
        root, 
        text="Show Message", 
        command=show_popup,
        bg="#4CAF50", 
        fg="white",
        padx=10,
        pady=5
    )
    msg_button.pack(pady=10)

    # 4. Start the application's event loop
    root.mainloop()

if __name__ == "__main__":
    main()