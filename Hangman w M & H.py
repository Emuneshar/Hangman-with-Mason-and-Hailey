import os


def wordChecker(secretWordTwo, correctLetters):
  for x in secretWordTwo:
    if x not in correctLetters:
      return False



rightLetters = []
wrongLetters = []

print("Welcome to Hangman\n")
print("One player will enter a secret word\n")
print("The second player will have to guess the secret word\n")

secretWord = input("What is the secret word?\n")
secretWord = secretWord.lower()

hint = input("Please enter a hint\n")

os.system('cls')

lives = 7

while True:
  guess = input("Please guess a letter\n")
  

  if lives < 0:
    break

  if guess == "hint!":
    print("The hint is", hint)
    continue

  if len(guess) > 1:
    if guess == secretWord:
      print("You got it right! Great job!\n")
    else:
      print("You got it wrong, sorry!\n")
      lives -= 1

  if guess in rightLetters:
    print("You've already guessed this letter, try again\n")

  elif guess in wrongLetters:
    print("You've guessed this letter already and it was incorrect")

  
  if guess in secretWord:
    print("You got that letter correct!\n")
    rightLetters.append(guess)

  if guess not in secretWord:
    print("That letter is wrong")
    lives -=1
    wrongLetters.append(guess)
    print("You  have", lives, "lives left")

  if guess == secretWord:
    print("You guessed the word correctly! You Win!")

  if wordChecker(secretWord, rightLetters) != False:
    print("You guessed the word correctly!\n")
    print("The secret word was", secretWord, "!\n")
    print("You win!")
    break

  