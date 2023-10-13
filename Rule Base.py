import tkinter as tk

CHARACTER_BANNER = "Character Banner"
WEAPON_BANNER = "Weapon Banner"

def calculate_probability(event=None):
    try:
        pulls = int(entry.get())
        if pulls <= 0:
            result_label.config(text="Please enter a valid number of pulls.")
        elif pulls > 90:
            result_label.config(text=f"Invalid pull amount! Pulls cannot exceed 90 (count pulls from 
                                last obtained 5 star)")
        else:
            probability = calculate(pulls)
            result_label.config(text=f"Probability of Obtaining a 5-Star Character: {probability:.2%}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

def calculate(pulls):
    if pulls < 73:
        return 0.006
    elif pulls < 90:
        return 0.006 + (pulls - 73) * 0.006 * 10
    else:
        return 1.0
    
def calculate_weapon_probability(pulls):
    if pulls < 63:
        return 0.007
    elif pulls < 80:
        return 0.007 + (pulls - 63) * 0.007 * 10
    else:
        return 1.0    

window = tk.Tk()
window.title("Genshin Impact 5 star Calculator")

instruction_label = tk.Label(window, text="Enter the number of pulls:")
instruction_label.pack(pady = 10)

entry = tk.Entry(window)
entry.pack(pady = 5)

calculate_button = tk.Button(window, text="Calculate", command=calculate_probability)
calculate_button.pack(pady = 10)

result_label = tk.Label(window, text="")
result_label.pack(pady = 10)

entry.bind("<Return>", calculate_probability)

window.mainloop()
