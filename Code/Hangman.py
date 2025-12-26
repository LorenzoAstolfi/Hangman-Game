import random
import hangman_words
import hangman_styles

print(hangman_styles.logo)

lives = 6

chosen_word = ""
language = input("\nChoose the language you would like to use (English/Italian): ").lower()
if language == "english":
    chosen_word = random.choice(hangman_words.word_list_en)

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print(f"Word to guess: {placeholder}, length -> {len(chosen_word)}")

    game_over = False
    correct_letters = []

    while not game_over:

        print(f"****************************{lives} LIVES LEFT****************************")
        guess = input("Guess a letter: ").lower()

        if guess in correct_letters:
            print("You already guessed a: " + guess)

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if guess not in chosen_word:
            lives -= 1
            print("You guessed" + guess + ", that's not in the word. You lose a life.")
            if lives == 0:
                game_over = True

                print("IT WAS " + chosen_word + "! YOU LOSE")
                print("***********************YOU LOSE**********************")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        print(hangman_styles.stages[lives])

elif language == "italian":
    chosen_word = random.choice(hangman_words.word_list_it)

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print(f"Parola da indovinare: {placeholder}, lunghezza -> {len(chosen_word)}")

    game_over = False
    correct_letters = []

    while not game_over:

        print(f"****************************{lives} VITE RIMANENTI****************************")
        guess = input("Indovina una lettera: ").lower()

        if guess in correct_letters:
            print("Hai già indovinato la lettera: " + guess)

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Parola da indovinare: " + display)

        if guess not in chosen_word:
            lives -= 1
            print("Hai provato con la lettera" + guess + ", non c'è nella parola. Hai perso una vita!")
            if lives == 0:
                game_over = True

                print("LA PAROLA ERA " + chosen_word + "! HAI PERSO")
                print("***********************HAI PERSO**********************")

        if "_" not in display:
            game_over = True
            print("****************************HAI VINTO****************************")

        print(hangman_styles.stages[lives])
