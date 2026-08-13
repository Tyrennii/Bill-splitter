from tkinter import *


appmain = Tk()
appmain.title("Bill Splitter")
appmain.geometry("1200x600")


Label(appmain, text="Enter the total bill amount", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
bill_entry = Entry(appmain)
bill_entry.grid(row=1, column=0, padx=10, pady=10)

Label(appmain, text="Select Tip", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
tip_1 = Button(appmain, text="5%", command=lambda: tip_var.set("5%"))
tip_1.grid(row=3, column=1, padx=10, pady=10)

tip_2 = Button(appmain, text="10%", command=lambda: tip_var.set("10%"))
tip_2.grid(row=3, column=2, padx=10, pady=10)

tip_3 = Button(appmain, text="15%", command=lambda: tip_var.set("15%"))
tip_3.grid(row=3, column=3, padx=10, pady=10)

tip_4 = Button(appmain, text="20%", command=lambda: tip_var.set("20%"))
tip_4.grid(row=4, column=1, padx=10, pady=10)

tip_5 = Button(appmain, text="25%", command=lambda: tip_var.set("25%"))
tip_5.grid(row=4, column=2, padx=10, pady=10)

tip_6 = Button(appmain, text="30%", command=lambda: tip_var.set("30%"))
tip_6.grid(row=4, column=3, padx=10, pady=10)

no_tip = Button(appmain, text="No Tip", command=lambda: tip_var.set("0%"))
no_tip.grid(row=5, column=0, padx=10, pady=10)


Label(appmain, text="Enter the number of people to split the bill with", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=10)
people_entry = Entry(appmain)
people_entry.grid(row=7, column=0, padx=10, pady=10)

def calculate_split():
    total = float(bill_entry.get())
    num_people = int(people_entry.get())
    tip_percentage = float(tip_var.get().strip('%'))

    result1 = total / num_people
    result2 = tip_percentage / 100
    amount_per_person = result1 + (result1 * result2)

    result_label.config(text=f"Amount to pay per person: ${amount_per_person:.2f}")

calculate_button = Button(appmain, text="Calculate", command=calculate_split, bg="blue", fg="white")
calculate_button.grid(row=7, column=1, padx=10, pady=10)

final_label = Label(appmain, text="", relief="sunken", width=30, font=("Arial", 12))
final_label.grid(row=8, column=0, padx=10, pady=10)

appmain.mainloop()



## add config to place the result in the final_label 