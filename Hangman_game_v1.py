import random
import tkinter as tk

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.configure(background='#f0f0f0')

        self.themes = {
            "Fruits": ["apple", "pear", "fig", "kiwi", "plum", "watermelon", "pineapple", "pomegranate", "mango", "papaya", "durian", "dragonfruit", "lychee", "jackfruit", "rambutan"],
            "Countries": ["USA", "UK", "India", "Japan", "Italy", "Brazil", "Russia", "Egypt", "Mexico", "Canada", "Fiji", "Bhutan", "Monaco", "Lesotho", "Suriname"],
            "Animals": ["cat", "dog", "bat", "ant", "rat", "elephant", "giraffe", "rhinoceros", "kangaroo", "cheetah", "platypus", "okapi", "quokka", "narwhal", "axolotl"]
        }

        self.difficulty_words = {
            "Easy": {"Fruits": ["apple", "pear", "fig", "kiwi", "plum"],
                     "Countries": ["USA", "UK", "India", "Japan", "Italy"],
                     "Animals": ["cat", "dog", "bat", "ant", "rat"]},
            "Medium": {"Fruits": ["watermelon", "pineapple", "pomegranate", "mango", "papaya"],
                       "Countries": ["Brazil", "Russia", "Egypt", "Mexico", "Canada"],
                       "Animals": ["elephant", "giraffe", "rhinoceros", "kangaroo", "cheetah"]},
            "Hard": {"Fruits": ["durian", "dragonfruit", "lychee", "jackfruit", "rambutan"],
                     "Countries": ["Fiji", "Bhutan", "Monaco", "Lesotho", "Suriname"],
                     "Animals": ["platypus", "okapi", "quokka", "narwhal", "axolotl"]}
        }

        self.selected_theme = tk.StringVar()
        self.selected_theme.set("Fruits")

        self.create_widgets()

    def create_widgets(self):
        # Theme selection
        theme_frame = tk.Frame(self.master, bg='#f0f0f0')
        theme_frame.pack(pady=20)
        tk.Label(theme_frame, text="Select Theme:", font=("Helvetica", 14), bg='#f0f0f0').pack(side=tk.LEFT)
        theme_option = tk.OptionMenu(theme_frame, self.selected_theme, *self.themes.keys())
        theme_option.config(font=("Helvetica", 12))
        theme_option.pack(side=tk.LEFT, padx=10)

        # Difficulty level selection
        difficulty_frame = tk.Frame(self.master, bg='#f0f0f0')
        difficulty_frame.pack(pady=10)
        tk.Label(difficulty_frame, text="Select Difficulty:", font=("Helvetica", 14), bg='#f0f0f0').pack(side=tk.LEFT)
        self.selected_difficulty = tk.StringVar()
        self.selected_difficulty.set("Easy")
        difficulty_option = tk.OptionMenu(difficulty_frame, self.selected_difficulty, "Easy", "Medium", "Hard")
        difficulty_option.config(font=("Helvetica", 12))
        difficulty_option.pack(side=tk.LEFT, padx=10)

        # Start button and other widgets
        self.start_button = tk.Button(theme_frame, text="Start", command=self.start_game, font=("Helvetica", 12))
        self.start_button.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='#f0f0f0', highlightthickness=0)
        self.canvas.pack(pady=20)

        self.display_word_label = tk.Label(self.master, text="", font=("Helvetica", 18), bg='#f0f0f0')
        self.display_word_label.pack(pady=10)

        self.word_length_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg='#f0f0f0')
        self.word_length_label.pack()

        self.attempts_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg='#f0f0f0')
        self.attempts_label.pack()

        self.warning_label = tk.Label(self.master, text="", font=("Helvetica", 14), bg='#f0f0f0', fg='red')
        self.warning_label.pack()

        self.input_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", lambda event: self.make_guess())

        self.submit_button = tk.Button(self.master, text="Guess", command=self.make_guess, font=("Helvetica", 14))
        self.submit_button.pack()

    def start_game(self):
        self.selected_theme = self.selected_theme.get()
        difficulty = self.selected_difficulty.get()
        self.word = random.choice(self.difficulty_words[difficulty][self.selected_theme])

        self.hidden_word = ["_"] * len(self.word)
        self.guessed_letters = set()
        self.attempts = 6
        self.display_word_label.config(text=" ".join(self.hidden_word))
        self.word_length_label.config(text=f"Word Length: {len(self.word)}")
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")
        self.canvas.delete("all")

    def draw_hangman(self):
        hangman_art = [
            """
            +---+
            |   
            |   
            |   
            |   
            |   
            =========
            """,
            """
            +---+
            |   O
            |   
            |   
            |   
            |   
            =========
            """,
            """
            +---+
            |   O
            |   |
            |   
            |   
            |   
            =========
            """,
            """
            +---+
            |   O
            |  /|
            |   
            |   
            |   
            =========
            """,
            """
            +---+
            |   O
            |  /|\\
            |   
            |   
            |   
            =========
            """,
            """
            +---+
            |   O
            |  /|\\
            |  / 
            |   
            |   
            =========
            """,
            """
            +---+
            |   O
            |  /|\\
            |  / \\
            |   
            |   
            =========
            """
        ]
        center_x = self.canvas.winfo_reqwidth() / 3
        center_y = self.canvas.winfo_reqheight() / 2
        self.canvas.create_text(center_x, center_y, text=hangman_art[6 - self.attempts], font=("Courier", 18), anchor=tk.CENTER, fill="#ff0000")

    def make_guess(self):
        if not self.word:
            self.display_word_label.config(text="Please select a theme and start the game.")
            return

        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)

        if guess.isdigit():
            self.warning_label.config(text="Please enter a letter.")
            return

        if len(guess) != 1 or not guess.isalpha():
            self.warning_label.config(text="Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.warning_label.config(text="You already guessed that letter.")
            return

        self.warning_label.config(text="")
        self.guessed_letters.add(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.hidden_word[i] = guess
            self.display_word_label.config(text=" ".join(self.hidden_word))
            if "".join(self.hidden_word) == self.word:
                self.display_word_label.config(text=f"Congratulations! You guessed the word: {self.word}")
                self.selected_theme = None
                self.word = None
                self.hidden_word = []
                self.guessed_letters = set()
                self.attempts = 6
                self.word_length_label.config(text="")
                self.attempts_label.config(text="")
                self.canvas.delete("all")
        else:
            self.attempts -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts}")
            self.draw_hangman()
            if self.attempts == 0:
                self.display_word_label.config(text=f"Game over! The word was: {self.word}")
                self.selected_theme = None
                self.word = None
                self.hidden_word = []
                self.guessed_letters = set()
                self.attempts = 6
                self.word_length_label.config(text="")
                self.attempts_label.config(text="")
                self.canvas.delete("all")

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
