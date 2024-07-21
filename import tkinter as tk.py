import tkinter as tk

def roll_dice():
    num_dice = int(dice_entry.get())
    num_sides = int(sides_entry.get())
    
    # generate random numbers
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    
    # display the results
    result_label.config(text="Rolls: " + ", ".join(str(r) for r in rolls))

# create the GUI
root = tk.Tk()
root.title("Dice Roller")

dice_label = tk.Label(root, text="Number of Dice:")
dice_label.pack()

dice_entry = tk.Entry(root)
dice_entry.pack()

sides_label = tk.Label(root, text="Number of Sides:")
sides_label.pack()

sides_entry = tk.Entry(root)
sides_entry.pack()

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
import random

num_dice = 3
num_sides = 6

rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
print(rolls)
result_label.config(text="Rolls: " + ", ".join(str(r) for r in rolls))
