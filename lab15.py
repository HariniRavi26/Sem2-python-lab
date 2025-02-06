import random
word_list=["cat","bird","tiger","lion","elephant","monkey","giraffe"]
guessed_letters=[]
guesses_left=6
word_to_guess=random.choice(word_list)
word_length=len(word_to_guess)
hidden_word=list("_"*word_length)
while guesses_left>0:
    print(f"\n You have {guesses_left} guesses left.")
    print(f"The word is {' '.join(hidden_word)}")
    print(f"You have guesses: {','.join(guessed_letters)}")
    guess=input("Enter a letter:").lower()
    if guess in word_to_guess:
        indices=[i for i,x in enumerate(word_to_guess) if x==guess]
        for index in indices:
            hidden_word[index]=guess
        if "_" not in hidden_word:
            print("\nCongratulations! You guessed the word correctly!")
            print(hidden_word)
            break
    else:
        guesses_left-=1
        if guesses_left==0:
            print("\nYou ran out of guesses!")
            print(f"The word was {word_to_guess}")
            break
    guessed_letters.append(guess)
