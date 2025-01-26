import random
import tkinter as tk
from tkinter import ttk, messagebox

# Function to check the user's guess
def check_guess():
    try:
        user_guess = int(guess_entry.get())
        global attempts
        attempts += 1

        if user_guess < random_number:
            result_label.config(text="Too low! Try again.", foreground="blue")
        elif user_guess > random_number:
            result_label.config(text="Too high! Try again.", foreground="blue")
        else:
            result_label.config(
                text=f"Congratulations! You guessed it in {attempts} attempts!",
                foreground="green",
            )
            messagebox.showinfo(
                "Success", f"You guessed the number! It was {random_number}."
            )
            reset_game()
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number!")

# Function to reset the game
def reset_game():
    global random_number, range_start, range_end, attempts
    range_start = random.randint(1, 50)
    range_end = random.randint(range_start + 1, range_start + 50)
    random_number = random.randint(range_start, range_end)
    attempts = 0
    result_label.config(
        text=f"Guess a number between {range_start} and {range_end}.", foreground="black"
    )
    hint_label.config(text="")
    guess_entry.delete(0, tk.END)

# Function to show a hint
def show_hint():
    hint = f"The number is {'even' if random_number % 2 == 0 else 'odd'}."
    hint_label.config(text=hint)

# Create the GUI window
window = tk.Tk()
window.title("Advanced Number Guessing Game")
window.geometry("500x400")
window.resizable(False, False)

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12))

# Game instructions
instruction_label = ttk.Label(
    window,
    text="I’m thinking of a number within a random range. Can you guess it?",
    font=("Arial", 14, "bold"),
    anchor="center",
)
instruction_label.pack(pady=10)

# Entry widget for user's guess
guess_frame = ttk.Frame(window)
guess_frame.pack(pady=10)
guess_entry = ttk.Entry(guess_frame, font=("Arial", 14), width=10, justify="center")
guess_entry.grid(row=0, column=0, padx=5)

submit_button = ttk.Button(guess_frame, text="Submit", command=check_guess)
submit_button.grid(row=0, column=1, padx=5)

# Label to display results
result_label = ttk.Label(
    window, text="", font=("Arial", 12), anchor="center", foreground="black"
)
result_label.pack(pady=10)

# Hint label
hint_label = ttk.Label(window, text="", font=("Arial", 12), anchor="center")
hint_label.pack(pady=5)

# Buttons for additional functionality
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

hint_button = ttk.Button(button_frame, text="Hint", command=show_hint)
hint_button.grid(row=0, column=0, padx=10)

reset_button = ttk.Button(button_frame, text="Reset Game", command=reset_game)
reset_button.grid(row=0, column=1, padx=10)

# Initialize the game with a random range
attempts = 0
reset_game()

# Start the GUI event loop
window.mainloop()
