import tkinter as tk
import tkinter.ttk as ttk

#Initializes tkinter window
root = tk.Tk()

#Creates calculator text label
lbl_calculator_display = tk.Label(height=2, bg="white")
lbl_calculator_display.pack(fill=tk.X)

#Frame acting as the master frame for the calculator button layout
frm_calc_btn_layout = ttk.Frame(root)
frm_calc_btn_layout.pack()

#Array defining calculator button layout
calc_btn_set = [["%", "7", "8", "9", "÷"],
                ["+/-", "4", "5", "6", "X"],
                ["C", "1", "2", "3", "-"],
                ["AC", "0", ".", "=", "+"]]

#TODO: Stylize button layout
#Generates a grid of buttons within the button layout master frame
for i in range(len(calc_btn_set)):
    for j in range(len(calc_btn_set[i])):
        button = ttk.Button(frm_calc_btn_layout,text=calc_btn_set[i][j])
        button.grid(row=i,column=j,padx=10,pady=10)

#Runs tkinter event loop
root.mainloop()