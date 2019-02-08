import time

def main():
	print('What is your number?')
	player_number = int(input(' > '))
	print('Let me guess your number.')
	time.sleep(3)
	guess = 0
	while guess != player_number:
		time.sleep(1)
		guess = player_number
		print(f'Is it {guess}?')
	if guess == player_number:
		time.sleep(1)
		print(f'Yup, that\'s it!')
	else:
		print('This feature is not implemented.')
		time.sleep(1)
		exit(1)
	exit(0)
	
main()
	
	