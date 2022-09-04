class Wordle:
    def __init__(self,player="1",score={"1":0,"2":0},guessList=[]):
        self.__player=player
        self.__score=score
        self.__guessList=guessList
    def switchPlayer(self):
        if self.__player=="1":
            self.__player="2"
        elif self.__player=="2":
            self.__player="1"
    def currentPlayer(self):
        print("Player "+ self.__player + " it's your turn.")
    def instructions(self):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("x Welcome to WORDLE, the popular word game. The goal is to guess a  x")
        print("x five letter word chosen at random from our wordlist. None of the  x")
        print("x words on the wordlist have any duplicate letters.                 x")
        print("x                                                                   x")
        print("x You will be allowed 6 guesses. Guesses must be from the allowed   x")
        print("x wordlist. We'll tell you if they're not.                          x")
        print("x                                                                   x")
        print("x Each letter in your guess will be marked as follows:              x")
        print("x                                                                   x")
        print("x    x means that the letter does not appear in the answer          x")
        print("x    ^ means that the letter is correct and in the correct location x")
        print("x    + means that the letter is correct, but in the wrong location  x")
        print("x                                                                   x")
        print("x Good luck!                                                        x")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    def wordList(self):
        infile = open('new-wordlist.txt', "r")
        text = infile.read().split()
        wordlist=[]
        for word in text:
            if len(word)==5:
                if self.noDuplicate(word)==True:
                    if word[4]!="s":
                        wordlist.append(word)
        return wordlist
    def noDuplicate(self,word):
        if len(word)==1:
            return True
        elif word[0] in word[1:]:
            return False
        elif word[0] not in word[1:]:
            return self.noDuplicate(word[1:])
    def randomWord(self,wordlist):
        import random
        return random.choice(wordlist)
    def validGuess(self,wordlist,guess):
        if guess not in wordlist or len(guess)!=5 or guess in self.__guessList:
            print()
            print("Guess must be a 5-letter word in the wordlist and you cannot input a word taht has already been guessed. Try again!")
            print()
            return False
        else:
            self.__guessList.append(guess)
            return True
    def takeTurn(self,guess,word):
        mark=[]
        for j in guess:
            print(j.upper()," ",end="")
        print()
        for k in range(5):
            if guess[k]==word[k]:
                mark.append("^")
            elif guess[k]!=word[k] and guess[k] in word:
                mark.append("+")
            else:
                mark.append("x")
        for h in mark:
            print(h," ",end="")
        print()
        return mark
    def winner(self,mark):
        if mark==["^","^","^","^","^"]:
            print("Congratulations you solved the word!")
            self.__score[self.__player]+=1
            return True
        else:
            return False
    def loser(self,word):
        print("Sorry! The word was " + word + ". Better luck next time!")
    def score(self):
        print("Player 1's score is " + str(self.__score["1"]) + " and Player 2's score is " +  str(self.__score["2"]))
    def finalWinner(self):
        if self.__score["1"]>self.__score["2"]:
            print("The winner is player 1!")
        elif self.__score["2"]>self.__score["2"]:
            print("The winner is player 1!")
        else:
            print("It's a tie!")
    def resetRound(self):
        self.__guessList=[]
