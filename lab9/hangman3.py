import sys
import random
  

wordsFile = open('long-words.txt').read()
words = wordsFile.split("\n")
numOfLine = random.randint(0, len(words))
word = words[numOfLine]

guess = ''

while (guess != "quit"):
	# pick a new word from the library
	numOfLine = random.randint(0, len(words))
	word = words[numOfLine]
	print("the word is:  %s\n" %word)
	print"\n*** New Game! ***"
	badGuess="" # all bad guesseed letters
	guessed= "" #all guessed letters, wrong and right
	match = '-'*len(word) #the partial match
	guess="" #current guess
	
	#a loop of one game
	while (match!=word) and (guess != "quit"):
		goodtry = False
		if (len(guessed)> 0): 
			print "guessed: %s, " %(guessed)
		print "steps from gallows: %d," %(6- (len(badGuess)))
		print "word so far: %s\n" %match
		guess = raw_input("Guess a letter: ")
		print ("****  the letter you guessed is %s  ***\n" %guess)
		out = False
		
		if (len(guess)>1):#if  incorrect input
			if (guess != "quit"):
				print"Uh oh: You can only guess a single letter at a time\n"
		else: 
			guessed = guessed + guess
			for i in range(len(guessed)-1): #check if the letter is in the guessed list
				if guess == guessed[i]:
					print "Uh oh: You have already tried "+guess+"\n"
					out = True
			if (out == False):
				for i in range(len(word)):
					if guess == word[i]: # change the __ to the letter
						matchnew = list(match) #TODO problam with assignment
						matchnew[i] = guess
						match = "".join(matchnew)
						print"**********\n"
						print match
						print"\n"
						goodtry = True
				if (goodtry):
				  if (match == word):
				    print "** You've been pardoned!! Well done!  The word was %s\n" %(word)
				  else:
				    print "* Great! The letter "+guess+" appears in the word!\n"
				else:  #the letter does not apear in the word
				  badGuess = badGuess +guess
				  if(len (badGuess) == 0):
				    print "** Uh oh: you've run out of steps. You're on the platform.. and <SNAP!>\n"
				    print "** The word you were trying to guess was "+match+"\n"
				  else:
				    print "* Nope, "+guess+" does not appear in the word."

				  
exit 
		 
