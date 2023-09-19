import tkinter as tk
import tkinter.ttk as ttk

#Initializes tkinter window
root = tk.Tk()

#Configure grid weight for relative design
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)

#Creates calculator text label
lbl_calculator_display = tk.Label(height=2, bg="white")
lbl_calculator_display.grid(row=0,column=0)

#Frame acting as the master frame for the calculator button layout
frm_calc_btn_layout = ttk.Frame(root)
frm_calc_btn_layout.grid(row=1,column=0)



#Array defining calculator button layout
calc_btn_set = [["%", "7", "8", "9", "÷"],
                ["+/-", "4", "5", "6", "X"],
                ["C", "1", "2", "3", "-"],
                ["AC", "0", ".", "=", "+"]]

#TODO: Stylize button layout
#Generates a grid of buttons within the button layout master frame
for i in range(len(calc_btn_set)):
    frm_calc_btn_layout.grid_rowconfigure(i,weight=1) #Allows row to use relative layout
    for j in range(len(calc_btn_set[i])):
        frm_calc_btn_layout.grid_columnconfigure(j, weight=1) #Allows columns to use relative layout

        #Creates button at specified grid location based on the calculator layout
        button = ttk.Button(frm_calc_btn_layout,text=calc_btn_set[i][j])
        button.grid(row=i,column=j,sticky="nsew")

#Runs tkinter event loop
root.mainloop()