import random
from Hangman_art import stages, logo
from Hangman_words import word_list
lives = 6
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

placeholder = ""
for i in range(word_length):
  placeholder += "_"
print(f"Word to guess: {placeholder}")
  
game_over = False
correct_letters = []

while not game_over:
  display = ""
  print(f"***********************{lives}/6 LIVES LEFT****************************")
  guess = input("Guess any letter: ").lower()
  
  if guess in correct_letters:
    print(f"You already guessed {guess}")
  
  for i in chosen_word:
    if guess == i:
      display += i
      correct_letters.append(i)
    elif i in correct_letters:
      display += i
    else:
      display += "_"
      
  print(f"Word to guess: {display}")
  print(stages[lives])
  
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
      game_over = True
      print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
  
  if "_" not in display:
    game_over = True
    print("****************************YOU WIN****************************")