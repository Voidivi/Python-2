#!/usr/bin/env python3
# Assignment Week 7 - GUI Tip Calculator
# Author: Lyssette  Williams

#importing the built-in python gui library

import tkinter as tk
from tkinter import ttk


# sample frame of Tip Calculator GUI
# this class defines the GUI dimensions, buttons and labels
class TipCalcFrame(ttk.Frame):
    def __init__(self, parent):

        ttk.Frame.__init__(self, parent, padding="20 20 20 20")
        self.pack()

        self.mealCost = tk.StringVar() #holds a string with default value of empty
        self.tipPercent = tk.IntVar() #holds a integer with a default value of 0
        self.tiptotal = tk.StringVar()
        self.billtotal = tk.StringVar()


        ttk.Label(self, text="***TIP CALCULATOR***").grid(column=1, row=0, sticky=tk.E)

        ttk.Label(self, text="Cost of Meal: ").grid(column=0, row=1, sticky=tk.E)  #Label for userinput field
        ttk.Entry(self, width=30, textvariable=self.mealCost).grid(column=1, row=1) #Actual field for user input for meal cost

        ttk.Label(self, text="Tip Percent: ").grid(column=0, row=2, sticky=tk.E) #Label for tip percent field
        #ttk.Entry(self, width=30, textvariable=self.tipPercent).grid(column=1, row=2)
        ttk.Entry(self, width=30, textvariable=self.tipPercent, state="readonly").grid(column=1, row=2) #not an input field, read only which references the radio buttons further down

        ttk.Label(self, text="Total Tip: ").grid(column=0, row=3, sticky=tk.E) #label for Total tip field
        #ttk.Entry(self, width=30, textvariable=self.tiptotal).grid(column=1, row=2)
        ttk.Entry(self, width=30, textvariable=self.tiptotal, state="readonly").grid(column=1, row=3) #read only field which references the tip total calculation in the calculate function

        ttk.Label(self, text="Total Bill: ").grid(column=0, row=4, sticky=tk.E) #label for total bill
        #ttk.Entry(self, width=30, textvariable=self.billtotal, state="readonly").grid(column=1, row=2)
        ttk.Entry(self, width=30, textvariable=self.billtotal, state="readonly").grid(column=1, row=4) #read only field which references the total calculation in the calculate function

        ttk.Button(self, text="Calculate",command=self.calculate).grid(column=1, row=5, sticky=tk.E) #calculate button which the user presses to find out their total bill

        ttk.Label(self, text="Tip Percent:").grid(column=2, row=1, sticky=tk.E)  #Label for the 3 radio buttons
        ttk.Radiobutton(self, text="15%", variable = self.tipPercent,value = 15).grid(column=2, row=2, sticky=tk.E)
        ttk.Radiobutton(self, text="18%", variable = self.tipPercent,value = 18).grid(column=2, row=3, sticky=tk.E)
        ttk.Radiobutton(self, text="20%", variable = self.tipPercent,value = 20).grid(column=2, row=4, sticky=tk.E)


        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

#this function actually does the calculation of the tip with userinput
    def calculate(self):

        tip = self.tipPercent.get()
        tiptotal = round(float(self.mealCost.get()) * (tip/100),2)
        total = round(float(self.mealCost.get()) + tiptotal,2)

        self.tiptotal.set("$ " + str(tiptotal))
        self.billtotal.set("$ " + str(total))


if __name__ == "__main__":

#the below code creates the actual box that all the buttons and fields go into
    tipcalculator = tk.Tk()
    #the below title goes in the window frame
    tipcalculator.title("Tip Calculator")

    TipCalcFrame(tipcalculator)
    tipcalculator.mainloop()
