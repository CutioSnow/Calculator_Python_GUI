import tkinter as tk
import tkinter.ttk as ttk

#Initializes tkinter window
root = tk.Tk()

#Creates calculator text label
solution = tk.Label(height=2, width=50, bg="white")
solution.pack()

#Frame acting as a grid container for buttons
frame = ttk.Frame(root)
frame.pack()

#Creates 4x4 grid of buttons
for i in range(4):
    for j in range(4):
        button = ttk.Button(frame,text=f"{i+1}x{j+1}")
        button.grid(row=i,column=j,padx=10,pady=10)

#Runs tkinter event loop
root.mainloop()