import sys
import random
def soFar(word,guessed):
 
  print
   

wordsFile = open('long-words.txt').read()
words = wordsFile.split("\n")
numOfLine = random.randint(0, len(words))
word = words[numOfLine]

guess = ''
plays = 0
while (guess != "quit"):
	# pick a new word from the library
	numOfLine = random.randint(0, len(words))
	word = words[numOfLine]
	
	if (plays = 0):
		print"\n*** New Game! ***"
		badGuess=""
		guessed= ""
		match = ["_"*len(word)]
	plays +=1
	guess=""
	
	#a loop of one game
	while (guess!=word) and (guess != "quit"):
	goodtry = False
		if (len(guessed)> 0):
			print "guessed: %d, " %(len(guessed))
		print "steps from gallows: %d," %(len(badGuess))
		print "word so far: "+match+"\n"
		guess = input("Guess a letter: ")
		out = False
		if (len(guess)>1):
			print"Uh oh: You can only guess a single letter at a time\n"
		else:
			for i in range(len(guessed)-1):
				if guess == guessed[i]:
					print "Uh oh: You have already tried "+guess+"\n"
					out = True
			if !out:
				for i in range(len(word)-1):
					if guess == word[i]:
						match[i] = guess
						goodtry = True
      
		
exit
		