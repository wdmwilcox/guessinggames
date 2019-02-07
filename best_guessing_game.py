import time

def main():
	numbers = []
	print('How many numbers do you want to guess from?')
	amount_of_numbers = int(input(' > '))
	print('What is your number?')
	player_number = int(input(' > '))
	print('Let me guess your number.')
	time.sleep(1)
	guess = 0
	while guess != player_number:
		guess = player_number
	print(f'Is it {guess}?')
	time.sleep(1)
	print(f'Yup, that\'s it!')
	exit(0)
	
main()
	
	