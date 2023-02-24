import random
print(correct)
print("NUMBER GUESSING")
print("---------------------")
print("You have 10 chances to guess the number")
print("-----------------------")
chance = 10
left = 1

while chance > 0:
	guess = int(input("Guess the number: "))
	if guess == correct:
		print("Bravo..! You guessed it right! in",left,"chance(s)")
		break
	else:
		chance = chance - 1
		left = left + 1
		if guess > correct:
			print("Guessed number is large")		
		else:
			print("Guessed number is small")
		print("You have ",chance,"chances left")
			
