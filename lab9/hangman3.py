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
	
	if (plays == 0):
		print"\n*** New Game! ***"
		badGuess="" # all bad guesseed letters
		guessed= "" #all guessed letters, wrong and right
		match = ["_"*len(word)] #the partial match
	plays +=1
	guess="" #current guess
	
	#a loop of one game
	while (guess!=word) and (guess != "quit"):
		goodtry = False
		if (len(guessed)> 0): 
			print "guessed: %d, " %(len(guessed))
		print "steps from gallows: %d," %(6- (len(badGuess)))
		print "word so far: "+match+"\n"
		guess = input("Guess a letter: ")
		out = False
		
		if (len(guess)>1):#if  incorrect input
			print"Uh oh: You can only guess a single letter at a time\n"
		else: 
			for i in range(len(guessed)-1): #check if the letter is in the guessed list
				if guess == guessed[i]:
					print "Uh oh: You have already tried "+guess+"\n"
					out = True
			if (out == False):
				for i in range(len(word)-1):
					if guess == word[i]: # change the __ to the letter
						match[i] = guess
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
		 
