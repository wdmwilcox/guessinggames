# import
import random
import time

# main
def main():
	numbers = []
	print('How many numbers do you want to guess from?')
	amount_of_numbers = int(input(' > '))
	print('What is your number?')
	player_number = int(input(' > '))
	print('Let me guess your number.')
	for i in range(amount_of_numbers):
		numbers.append(i)
	while True:
		guess = random.randint(0,len(numbers))
		print('Is your number...')
		time.sleep(1)
		print(f'{numbers[guess]}?')
		if numbers[guess] != player_number:
			print('Nope, that\'s not it..')
			continue
		else:
			break
	print('Yup, that\'s it.')
	exit(0)

main()
	