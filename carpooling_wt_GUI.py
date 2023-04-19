from tkinter import *
import tkinter




travelers = {}
def addrider():
    rider_name = nameentry.get()
    rider_dest = destentry.get()
    if rider_name != "" and rider_dest != "":
        travelers[rider_name] = rider_dest
        nameentry.delete(0, END)
        destentry.delete(0, END)
        statuslabel.config(text="Rider added!")
    else:
        statuslabel.config(text="Please enter both a name and destination.")

def viewriders():
    if len(travelers) == 0:
        riderslistbox.delete(0, END)
        riderslistbox.insert(END, "No riders yet.")
    else:
        riderslistbox.delete(0, END)
        for rider, dest in travelers.items():
            riderslistbox.insert(END, f"{rider} => {dest}.")

# Create GUI
root = Tk()
root.title("Carpooling demo")

# Labels
namelabel = Label(root, text="Name:")
destlabel = Label(root, text="Destination:")
statuslabel = Label(root, text="")
riderslabel = Label(root, text="Riders and Destinations:")

# Entries
nameentry = Entry(root)
destentry = Entry(root)

# Buttons
addbutton = Button(root, text="Add Rider", command=addrider)
viewbutton = Button(root, text="View Riders", command=viewriders)

# Listbox
riderslistbox = Listbox(root)

# Grid layout
namelabel.grid(row=0, column=0, padx=5, pady=5)
nameentry.grid(row=0, column=1, padx=5, pady=5)
destlabel.grid(row=1, column=0, padx=5, pady=5)
destentry.grid(row=1, column=1, padx=5, pady=5)
addbutton.grid(row=2, column=0, padx=5, pady=5)
viewbutton.grid(row=2, column=1, padx=5, pady=5)
statuslabel.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
riderslabel.grid(row=4, column=0, padx=5, pady=5)
riderslistbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

