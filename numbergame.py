import random

# generate a random number betwee 1 and 10
secret_num = random.randint(1,10)
guesses = []

while len(guesses) < 5:
	# get a guess from the player
		guess = int(raw_input('Guess a number betwixt 1 and 10: '))

	# compare guess with secret number
		if secret_num == guess:

	# print the hit or miss
			print('You nailed it! My number was {}!'.format(secret_num))
			break

		elif secret_num > guess:
			print('Too low!')
			continue

		elif secret_num < guess:
			print('Too high!')
			continue

		else:
			print('That is not a number')
			continue

			guesses.append(guess)

# limit the number of guesses
# ask if they would like to start
# allow for continued play


