class BattleShip:
    def __init__(self,playerScore={"A":0,"B":0},ships={"carrier":5,"battleship":4,"cruiser":3,"submarine":3,"destroyer":2},playerShips={"A":[],"B":[]},currentPlayer="A",remainingShipsA={"carrier":1,"battleship":1,"cruiser":1,"submarine":1,"destroyer":1},remainingShipsB={"carrier":1,"battleship":1,"cruiser":1,"submarine":1,"destroyer":1}):
        self.__playerScore=playerScore
        self.__board1=self.listBoard()
        self.__board2=self.listBoard()
        self.__targBoard1=self.listBoard()
        self.__targBoard2=self.listBoard()
        self.__ships=ships
        self.__playerShips=playerShips
        self.__currentPlayer=currentPlayer
        self.__remainingShipsA=remainingShipsA
        self.__remainingShipsB=remainingShipsB
    def instructions(self):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("x Welcome to Battle Ship! Secretly place your fleet of 5 ships on your ocean      x")
        print("x grid. To place each ship input a coordinate to represent the back end of the    x")
        print("x ship and input a direction for the remainder of your ship to be positioned.     x")
        print("x After you and your opponent have placed your fleet, you will select a           x")
        print("x coordinate to drop a missle on. If you drop a missle on a ship a X will appear. x")
        print("x Once you have sunk an entire ship a + mark will appear around the ship. Once    x")
        print("x all 5 of your opponents ships have been sunk you win!                           x")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    def listBoard(self):
        lst=[]
        for i in range(10):
            lst.append([])
            for j in range(10):
                lst[i].append(".")
        return lst
    def printBoards(self,board):
        for i in range(10):
            for j in range(10):
                print(board[i][j],"",end="")
            print()
    def currPlayer(self):
        return self.__currentPlayer
    def currSetBoard(self):
        if self.currPlayer()=="A":
            return self.__board1
        elif self.currPlayer()=="B":
            return self.__board2
    def currBoard(self):
        if self.currPlayer()=="A":
            return self.__board2
        elif self.currPlayer()=="B":
            return self.__board1
    def currTargBoard(self):
        if self.currPlayer()=="A":
            return self.__targBoard1
        elif self.currPlayer()=="B":
            return self.__targBoard2
    def switchPlayer(self):
        if self.__currentPlayer=="A":
            self.__currentPlayer="B"
        elif self.__currentPlayer=="B":
            self.__currentPlayer="A"
    def setRemainingShips(self):
        if self.__currentPlayer=="A":
            return self.__remainingShipsA
        elif self.__currentPlayer=="B":
            return self.__remainingShipsB
    def validShipType(self,shipType):
        if shipType not in self.__ships:
            print()
            print("There is no ship called " + str(shipType) + ". Please try again.")
            return False
        elif  shipType in self.__ships:
            if self.setRemainingShips()[shipType]!=0:
                self.setRemainingShips()[shipType]-=1
                return True
            else:
                print("There are no remaining " + str(shipType) + "'s. Please try again.")
                return False
        else:
            print("There are no remaining " + str(shipType) + "'s. Please try again.")
            return False
    def validCoord(self,c):
        if len(c)==5 and c[0]=="(" and c[1].isdigit()==True and c[2]=="," and  c[3].isdigit()==True and c[4]==")":
            coord=(int(c[1]),int(c[3]))
            if len(coord)==2 and str(coord[0]).isdigit()==True and str(coord[1]).isdigit()==True and 0<=coord[0]<=9 and 0<=coord[1]<=9 and self.currSetBoard()[coord[0]][coord[1]]==".":
                return True
            else:
                print("This is an invalid coordinate. Please try again.")
                return False    
        else:
            print("This is an invalid coordinate. Please try again.")
            return False
    def validDirec(self,direc):
        if direc=="n" or direc=="s" or direc=="e" or direc=="w":
            return True
        else:
            print("This is an invalid direction. Please try again.")
            return False
    def noSurrondingShips(self,x,y):
        if x!=0 and y!=0:
            if self.currSetBoard()[x-1][y-1]!=".":
                return False
        if y!=0:
            if self.currSetBoard()[x][y-1]!=".":
                return False
        if x!=9 and y!=0:
            if self.currSetBoard()[x+1][y-1]!=".":
                return False
        if x!=0:
            if self.currSetBoard()[x-1][y]!=".":
                return False
        if x!=9:
            if self.currSetBoard()[x+1][y]!=".":
                return False
        if y!=9 and x!=0:
            if self.currSetBoard()[x-1][y+1]!=".":
                return False
        if y!=9:
            if self.currSetBoard()[x][y+1]!=".":
                return False
        if x!=9 and y!=9:
            if self.currSetBoard()[x+1][y+1]!=".":
                return False
        return True
    def validShipLocation(self,shipType,direc,x,y):
        for i in range(self.__ships[shipType]):
            if direc=="n":
                if (x-i)-self.__ships[shipType]<0 or self.noSurrondingShips(x-i,y)==False:
                    print("This direction is invalid because it goes off the grid or there is a surronding ship.")
                    return False
            elif direc=="s":
                if (x+i)+self.__ships[shipType]>9  or self.noSurrondingShips(x+i,y)==False:
                    print("This direction is invalid because it goes off the grid or there is a surronding ship.")
                    return False
            elif direc=="e":
                if (y+i)+self.__ships[shipType]>9  or self.noSurrondingShips(x,y+i)==False:
                    print("This direction is invalid because it goes off the grid or there is a surronding ship.")
                    return False
            elif direc=="w":
                if (y-i)-self.__ships[shipType]<0  or self.noSurrondingShips(x,y-i)==False:
                    print("This direction is invalid because it goes off the grid or there is a surronding ship.")
                    return False
        return True
    def setShipLocation(self,board,shipType,direc,x,y):
        self.__playerShips[self.__currentPlayer].append([])
        for i in range(self.__ships[shipType]):
            if direc=="n":
                board[x-i][y]=self.__currentPlayer
                self.__playerShips[self.__currentPlayer][len(self.__playerShips[self.__currentPlayer])-1].append((x-i,y))
            elif direc=="s":
                board[x+i][y]=self.__currentPlayer
                self.__playerShips[self.__currentPlayer][len(self.__playerShips[self.__currentPlayer])-1].append((x+i,y))
            elif direc=="e":
                board[x][y+i]=self.__currentPlayer
                self.__playerShips[self.__currentPlayer][len(self.__playerShips[self.__currentPlayer])-1].append((x,y+i))
            elif direc=="w":
                board[x][y-i]=self.__currentPlayer
                self.__playerShips[self.__currentPlayer][len(self.__playerShips[self.__currentPlayer])-1].append((x,y-i))
    def validCoord2(self,c):
        if len(c)==5 and c[0]=="(" and c[1].isdigit()==True and c[2]=="," and  c[3].isdigit()==True and c[4]==")":
            coord=(int(c[1]),int(c[3]))
            if len(coord)==2 and str(coord[0]).isdigit()==True and str(coord[1]).isdigit()==True and 0<=coord[0]<=9 and 0<=coord[1]<=9 and self.currTargBoard()[coord[0]][coord[1]]!="X" and self.currTargBoard()[coord[0]][coord[1]]!="+":
                return True
            else:
                print("This is an invalid coordinate. Please try again.")
                return False    
        else:
            print("This is an invalid coordinate. Please try again.")
            return False
    def takeTurn(self,Board,targBoard,x,y):
        if Board[x][y]==".":
            targBoard[x][y]="X"
        elif Board[x][y]=="A" or Board[x][y]=="B":
            targBoard[x][y]="+"
            for i in self.__playerShips[self.oppPlayer()]:
                if (x,y) in i:
                    count=0
                    for j in i:
                        if targBoard[j[0]][j[1]]=="+":
                            count+=1
                    break
            if count==len(i):
                self.sinkShip(targBoard,x,y)
    def emptySpaces(self,targBoard,x,y):
        if x!=0 and y!=0:
            if targBoard[x-1][y-1]==".":
                targBoard[x-1][y-1]="X"
        if y!=0:
            if targBoard[x][y-1]==".":
                targBoard[x][y-1]="X"
        if x!=9 and y!=0:
            if targBoard[x+1][y-1]==".":
                targBoard[x+1][y-1]="X"
        if x!=0:
            if targBoard[x-1][y]==".":
                targBoard[x-1][y]="X"
        if x!=9:
            if targBoard[x+1][y]==".":
                targBoard[x+1][y]="X"
        if y!=9 and x!=0:
            if targBoard[x-1][y+1]==".":
                targBoard[x-1][y+1]="X"
        if y!=9:
            if targBoard[x][y+1]==".":
                targBoard[x][y+1]="X"
        if y!=9 and x!=9:
            if targBoard[x+1][y+1]==".":
                targBoard[x+1][y+1]="X"
    def oppPlayer(self):
        if self.__currentPlayer=="A":
            return "B"
        elif self.__currentPlayer=="B":
            return "A"
    def sinkShip(self,targBoard,x,y):
        for i in self.__playerShips[self.oppPlayer()]:
            if (x,y) in i:
                for j in i:
                    self.emptySpaces(targBoard,j[0],j[1])
                #self.sunkenShipType(i)
                self.__playerShips[self.oppPlayer()].remove(i)
                break 
    def sunkenShipType(self,i):
        for s in self.__ships:
            if self.__ships[s]==len(i):
                print("You hit a " + s + " ship!")
    def winner(self):
        if self.__playerShips[self.oppPlayer()]==[]:
            self.__playerScore[self.__currentPlayer]+=1
            return True
        else:
            return False
    def finalWinner(self):
        if self.__playerScore["A"]>self.__playerScore["B"]:
            print("Congratulations player 1 you won Battleship!")
        elif self.__playerScore["A"]<self.__playerScore["B"]:
            print("Congratulations player 2 you won Battleship!")
        elif self.__playerScore["A"]==self.__playerScore["B"]:
            print("It's a tie!")
    def playerScoreCheck(self):
        print("player 1's score is "+str(self.__playerScore["A"])+" and player 2's score is "+str(self.__playerScore["B"]))
    def resetRound(self):
        self.__board1=self.listBoard()
        self.__board2=self.listBoard()
        self.__targBoard1=self.listBoard()
        self.__targBoard2=self.listBoard()
        self.__ships={"carrier":5,"battleship":4,"cruiser":3,"submarine":3,"destroyer":2}
        self.__playerShips={"A":[],"B":[]}
        self.__remainingShipsA={"carrier":1,"battleship":1,"cruiser":1,"submarine":1,"destroyer":1}
        self.__remainingShipsB={"carrier":1,"battleship":1,"cruiser":1,"submarine":1,"destroyer":1}
