import tkinter as tk

CHARACTER_BANNER = "Character Banner"
WEAPON_BANNER = "Weapon Banner"

def calculate_probability():
    try:
        pulls = int(entry.get())
        banner_type = banner_choice.get()

        if pulls <= 0:
            result_label.config(text="Please enter a valid number of pulls.")
        elif banner_type == CHARACTER_BANNER:
            probability = calculate_probability_for_banner(pulls, CHARACTER_BANNER)
            result_label.config(text=f"Character Banner: Probability of a 5-star character: {probability:.2%}")
        elif banner_type == WEAPON_BANNER:
            probability = calculate_probability_for_banner(pulls, WEAPON_BANNER)
            result_label.config(text=f"Weapon Banner: Probability of a 5-star weapon: {probability:.2%}")
        else:
            result_label.config(text="Please select a banner type.")

    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

def calculate_probability_for_banner(pulls, banner_type):
    if banner_type == CHARACTER_BANNER:
        if pulls < 73:
            return 0.006
        elif pulls < 90:
            return 0.006 + (pulls - 73) * 0.006 * 10
        else:
            return 1.0
        
    elif banner_type == WEAPON_BANNER:
        if pulls < 62:
            return 0.007
        elif pulls < 77:
            return 0.007 + (pulls - 62) * 0.007 * 10  # Increasing by 0.093 over 14 pulls
        else:
            return 1.0

window = tk.Tk()
window.title("Genshin Impact 5 star Calculator")

instruction_label = tk.Label(window, text="Enter the number of pulls:")
instruction_label.pack(pady = 10)

entry = tk.Entry(window)
entry.pack(pady = 5)

banner_choice = tk.StringVar()
character_banner_checkbox = tk.Radiobutton(window, text=CHARACTER_BANNER, variable=banner_choice, value=CHARACTER_BANNER)
character_banner_checkbox.pack()
weapon_banner_checkbox = tk.Radiobutton(window, text=WEAPON_BANNER, variable=banner_choice, value=WEAPON_BANNER)
weapon_banner_checkbox.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_probability)
calculate_button.pack(pady = 10)


result_label = tk.Label(window, text="")
result_label.pack(pady = 10)

entry.bind("<Return>", calculate_probability)

window.mainloop()
