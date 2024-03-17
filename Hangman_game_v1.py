import random

def choose_word() :
    words = [
    "AFGHANISTAN", "ARMENIA", "AZERBAIJAN", "BAHRAIN", "BANGLADESH", 
    "BHUTAN", "BRUNEI", "CAMBODIA", "CHINA", "CYPRUS", "GEORGIA", 
    "INDIA", "INDONESIA", "IRAN", "IRAQ", "ISRAEL", "JAPAN", "JORDAN", 
    "KAZAKHSTAN", "KUWAIT", "KYRGYZSTAN", "LAOS", "LEBANON", "MALAYSIA", 
    "MALDIVES", "MONGOLIA", "MYANMAR", "NEPAL", "NORTH KOREA", 
    "OMAN", "PAKISTAN", "PALESTINE", "PHILIPPINES", "QATAR", "RUSSIA", 
    "SAUDI ARABIA", "SINGAPORE", "SOUTH KOREA", "SRI LANKA", "SYRIA", 
    "TAIWAN", "TAJIKISTAN", "THAILAND", "TIMOR-LESTE", 
    "TURKEY", "TURKMENISTAN", "UNITED ARAB EMIRATES", "UZBEKISTAN", 
    "VIETNAM", "YEMEN"
]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
            displayed_word += " " 
    return displayed_word

def display_hangman(wrong_guesses):
    stages = [
        '''
          -----
         |     |
         |     
         |     
         |     
         |
        -----
        ''',
        '''
          -----
         |     |
         |     O
         |     
         |     
         |
        -----
        ''',
        '''
          -----
         |     |
         |     O
         |     |
         |     
         |
        -----
        ''',
        '''
          -----
         |     |
         |     O
         |    /|
         |     
         |
        -----
        ''',
        '''
          -----
         |     |
         |     O
         |    /|\\
         |     
         |
        -----
        ''',
        '''
          -----
         |     |
         |     O
         |    /|\\
         |    /
         |
        -----
        ''',
        '''
          -----
         |     |
         |     O
         |    /|\\
         |    / \\
         |
        -----
        '''
    ]
    return stages[wrong_guesses]

def hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while wrong_guesses < 7:
        print("\n" + display_word(word, guessed_letters))
        print(display_hangman(wrong_guesses))
        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Incorrect! You have {} attempts left.".format(7 - wrong_guesses))
            if wrong_guesses == 7:
                print("\nSorry, you're out of attempts. The word was '{}'.".format(word))
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word: '{}'.".format(word))
            break

if __name__ == "__main__":
    hangman()
