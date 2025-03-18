import random
import time

print("Hi welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number....")
time.sleep(2)
guess = int(input("what is your guess?:"))
correct_number = random.randint(1,100)
guess_count = 0

while guess != correct_number:
    guess_count += 1
    if guess > correct_number:
        guess = int(input("Wrong!you need to guess lower.what is your guess?:"))
    else:
        guess = int(input("Wrong!you need to guess higher.what is your guess?:"))

print(f"congrats! the answer was {correct_number}. It took you {guess_count} guesses.")






#expected output
#Hi welcome to the guessing game. I am going to pick a number between 1 and 100.
#Picking a number....
#5what is your guess?:
#Wrong!you need to guess higher.what is your guess?:5
#Wrong!you need to guess higher.what is your guess?:25
#Wrong!you need to guess higher.what is your guess?:35
#Wrong!you need to guess higher.what is your guess?:55
#Wrong!you need to guess higher.what is your guess?:65
#congrats! the answer was 65. It took you 5 guesses.
