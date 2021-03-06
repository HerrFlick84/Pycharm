import random
import Hangman_words
import Hangman_art

chosen_word = random.choice(Hangman_words.word_list)
lives = Hangman_art.stages
result = ["_"] * len(chosen_word)
print(Hangman_art.logo)
print(chosen_word)
print(result)
while "_" in result and len(lives) > 0:
    gues = input("Please gues letter: ").lower()
    print("letter chosen: :" + gues)
    i = 0
    for l in chosen_word:
        if gues == l:
            result[i] = l
        i += 1
    if not gues in result:
        print(lives.pop())
    print(result)
if not "_" in result:
    print("You won")
else:
    print("You lost")
