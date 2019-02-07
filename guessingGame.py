import time
import random

MIN_ANSWER = 1
MAX_ANSWER = 100

def ask_for_number():
	try:
		answer = int(input(f"Guess a number between {MIN_ANSWER} and {MAX_ANSWER}: "))
		return answer
	except:
		print("You have to enter an integer number, please try again.")
		return ask_for_number()
		

def make_a_guess(guess, answer):
	print(f"Is your number {guess}?")
	if guess != answer:
		print("No, that's not it.")
		time.sleep(0.5)
		print("Hmm...",)
		if guess > answer:
			guess = guess - random.randint(1,guess-MIN_ANSWER)
		elif guess < answer:
			guess = guess + random.randint(1,MAX_ANSWER-guess)
		time.sleep(0.5)
		return make_a_guess(guess, answer)
	else:
		return guess
		

def main():
	answer = int(ask_for_number())
	guess = int(MAX_ANSWER / 2)
	correct_answer = make_a_guess(guess, answer)
	print(f"Oh yeah, it's {correct_answer}!  I win")
	time.sleep(2)
	exit()
	
main()
	
		
		
		
	