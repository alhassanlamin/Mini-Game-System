class ConnectFour:
   def __init__(self,player1={"A":0},player2={"B":0},player="A"):
      self.__player1=player1
      self.__player2=player2
      self.__player=player
      self.__board=self.listBoard()
   def instructions(self):
      print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
      print("x Welcome to Connect 4! Choose a player to be A and another player to be B    x")
      print("x Try to build a row of four checkers while keeping your opponent from doing  x")
      print("x the same. If you're the first player to get four of your checkers in a row, x")
      print("x you win the game!                                                           x")
      print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
   def listBoard(self):
      lst=[]
      for i in range(6):
         lst.append([])
         for j in range(7):
            lst[i].append(".")
      return lst
   def printBoard(self):
      for i in range(6):
         for j in range(7):
            print(self.__board[i][j],"",end="")
         print()
   def fullColumn(self,col):
      if self.__board[0][col]=="A" or self.__board[0][col]=="B":
         return True
      else:
         return False
   def currentPlayer(self):
      return self.__player
   def previousPlayer(self):
      if self.__player=="A":
         return "B"
      elif self.__player=="B":
         return "A"
   def switchPlayer(self):
      if self.__player=="A":
         self.__player="B"
      elif self.__player=="B":
         self.__player="A"
   def takeTurn(self,col):
      for row in range(5,-1,-1):
         if self.__board[row][col]==".":
            self.__board[row][col]=self.__player
            self.switchPlayer()
            break
   def winner(self):
      for i in self.__board:
         count=0
         for j in i:
            if j==self.previousPlayer():
               count+=1
            elif j!=self.previousPlayer():
               count=0
            if count==4:
               return True
      for i in range(7):
         count=0
         for j in range(6):
            if self.__board[j][i]==self.previousPlayer():
               count+=1
            elif self.__board[j][i]!=self.previousPlayer():
               count=0
            if count==4:
               return True
      for i in range(3):
         for j in range(4):
            count=0
            if self.__board[i][j]==self.previousPlayer():
               count+=1
            if self.__board[i+1][j+1]==self.previousPlayer():
               count+=1
            if self.__board[i+2][j+2]==self.previousPlayer():
               count+=1
            if self.__board[i+3][j+3]==self.previousPlayer():
               count+=1
            if count==4:
               return True
      for i in range(3):
         for j in range(6,2,-1):
            count=0
            if self.__board[i][j]==self.previousPlayer():
               count+=1
            if self.__board[i+1][j-1]==self.previousPlayer():
               count+=1
            if self.__board[i+2][j-2]==self.previousPlayer():
               count+=1
            if self.__board[i+3][j-3]==self.previousPlayer():
               count+=1
            if count==4:
               return True     
      return False
   def finalWinner(self):
      if self.__player1["A"]>self.__player2["B"]:
         print("The winner is A!")
      elif self.__player1["A"]==self.__player2["B"]:
         print("It's a tie!")
      else:
         print("The winner is B!")
   def scoreCount(self):
      if self.previousPlayer()=="A":
         self.__player1["A"]+=1
      elif self.previousPlayer()=="B":
         self.__player2["B"]+=1
   def resetRound(self):
      self.__board=self.listBoard()
      self.__player="A"
   def getScore(self):#str method
      print("player A's score is "+str(self.__player1["A"])+" and player B's score is "+str(self.__player2["B"])+".")
