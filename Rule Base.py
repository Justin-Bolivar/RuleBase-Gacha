import tkinter as tk

C_BANNER = "Character Banner"
W_BANNER = "Weapon Banner"

def calculate_probability(event = None):
    try:
        pulls = int(entry.get())
        banner_type = banner_choice.get()

        if pulls <= 0:
            result_label.config(text = "Please enter a valid number of pulls.")
        elif banner_type == C_BANNER:
            probability = calculate_probability_for_banner(pulls, C_BANNER)
            result_label.config(text = f"Character Banner: Probability of a 5-star character: {probability:.2%}")
        elif banner_type == W_BANNER:
            probability = calculate_probability_for_banner(pulls, W_BANNER)
            result_label.config(text = f"Weapon Banner: Probability of a 5-star weapon: {probability:.2%}")
        else:
            result_label.config(text = "Please select a banner type.")

    except ValueError:
        result_label.config(text = "Invalid input. Please enter a valid number.")

def calculate_probability_for_banner(pulls, banner_type):
    if banner_type == C_BANNER:
        if pulls < 73:
            return 0.006
        elif pulls < 90:
            return 0.006 + (pulls - 73) * 0.006 * 10
        else:
            return 1.0
        
    elif banner_type == W_BANNER:
        if pulls < 62:
            return 0.007
        elif pulls < 77:
            return 0.007 + (pulls - 62) * 0.007 * 10
        else:
            return 1.0

window = tk.Tk()
window.title("Genshin Impact 5 star Calculator")

instruction_label = tk.Label(window, text = "Enter the number of pulls:")
instruction_label.pack(pady = 10)

entry = tk.Entry(window)
entry.pack(pady = 5)

banner_choice = tk.StringVar()
character_banner_checkbox = tk.Radiobutton(window, text = C_BANNER, variable = banner_choice, value = C_BANNER)
character_banner_checkbox.pack()
weapon_banner_checkbox = tk.Radiobutton(window, text = W_BANNER, variable = banner_choice, value = W_BANNER)
weapon_banner_checkbox.pack()

calculate_button = tk.Button(window, text = "Calculate", command = calculate_probability)
calculate_button.pack(pady = 10)


result_label = tk.Label(window, text="")
result_label.pack(pady = 10)

entry.bind("<Return>", calculate_probability)

window.mainloop()
