import os

rightLetters = []
wrongLetters = []

print("Welcome to Hangman\n")
print("One player will enter a secret word\n")
print("The second player will have to guess the secret word\n")

secretWord = input("What is the secret word?\n")

hint = input("Please enter a hint\n")

os.system('clear')

lives = 7

while True:
  guess = input("Please guess a letter\n")

  if guess in rightLetters:
    print("You've already guessed this letter, try again\n")

  elif guess in wrongLetters:
    print("You've guessed this letter already and it was incorrect")

  
  if guess in secretWord:
    print("You got that letter correct!\n")
    rightLetters.append(guess)

    
CoachBob = "coach Ethan's prodige."
words = ["Eshwar, " , "should ", "buy ", "crocs."]
for word in words:
  print(word)