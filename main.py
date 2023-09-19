import tkinter as tk
import tkinter.ttk as ttk

#Initializes tkinter window
root = tk.Tk()
root.minsize(width=300,height=400) #set minimum height and width for root window
root.maxsize(width=600,height=800) #Set maximum height and width of root window
root.propagate(False) #Disable propagation of window widgets
root.aspect(3,4,3,4) #set desired aspect ratio (3:4)

#Configure grid weight for relative design
root.grid_rowconfigure(0,weight=0)
root.grid_rowconfigure(1,weight=2)
root.grid_columnconfigure(0,weight=1)

#Display Frame used to contain calculator display label
frm_calc_display = ttk.Frame(root,height=5)
frm_calc_display.grid(row=0,column=0,sticky="nsew")

#Creates calculator text label
lbl_calculator_display = tk.Label(master=frm_calc_display, height=5, bg="white", justify="right")
lbl_calculator_display.pack(fill="both") #fill x and ycoordinate space

#Frame acting as the master frame for the calculator button layout
frm_calc_btn_layout = ttk.Frame(root)
frm_calc_btn_layout.grid(row=1,column=0,sticky="nsew") #Fill both x and y space

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
        button.grid(row=i,column=j,sticky="nsew") #Sticks to north, south, east, and west panes

#Runs tkinter event loop
root.mainloop()