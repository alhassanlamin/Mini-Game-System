class Sorry:
    def __init__(self,currentPlayer="B",score={"R":0,"B":0,"Y":0,"G":0},cards=[1,2,3,4,5,6,7,8,9,10,11,12,"Sorry"],playerPieces={"R":["R","R","R"],"B":["B","B","B"],"Y":["Y","Y","Y"],"G":["G","G","G"]},homePawn={"R":0,"B":0,"Y":0,"G":0},startPawn={"R":(11,1),"B":(1,4),"Y":(4,14),"G":(14,11)},startSpace={"R":(11,0),"B":(0,4),"Y":(4,15),"G":(15,11)},boardSpace=[".","→","←","↑","↓"],safeSpace={"R":(13,1),"B":(1,2),"Y":(2,14),"G":(14,13)}):
        self.__board=self.listBoard()
        self.__currentPlayer=currentPlayer
        self.__score=score
        self.__cards=cards
        self.__playerPieces=playerPieces
        self.__homePawn=homePawn
        self.__startPawn=startPawn
        self.__startSpace=startSpace
        self.__boardSpace=boardSpace
        self.__safeSpace=safeSpace
    def instructions(self):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("x Welcome to Sorry! Have each player choose between Blue(B), Yelllow(Y), Green(G),     x")
        print("x or Red(R). The order will go B,Y,G, then R. A card will be generated for each.       x")
        print("x turn. In order for a pawn to be removed from the start space, a card labeled 1 or 2  x")
        print("x must be generated. If a 'Sorry' card is drawn, move one of the pieces from your      x")
        print("x start space and take another players pawn's position. This players pawn will then be x")
        print("x moved to their start space. If you land on a slider on a row or column where your    x")
        print("x start space doesn't lie, then you will slide to the end of the slider, while         x")
        print("x bumping other players pawns back to the start. Once you have reach the safe zone,    x")
        print("x you will need to generate the exact card number that allows you to reach the home    x")
        print("x space. Once all 3 of your pawns have reached the home space, you win! remember that  x")
        print("x The Sorry board is based on a 15x15 grid. The row numbers range from 0-15 from top   x")
        print("x of the grid to the bottom. The column numbers range from 0-15 from the right side of x")
        print("x the grid to the left. So make sure to input your coordinates accordingly.            x")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    def listBoard(self):
        lst=[]
        for i in range(16):
            lst.append([])
            for j in range(16):
                if i==10 and j==5:
                    lst[i].append("S")
                elif i==9 and j==6:
                    lst[i].append("O")
                elif i==8 and j==7:
                    lst[i].append("R")
                elif i==7 and j==8:
                    lst[i].append("R")
                elif i==6 and j==9:
                    lst[i].append("Y")
                elif i==5 and j==10:
                    lst[i].append("!")
                elif i==0:
                    if 1<=j<=3 or 9<=j<=12:
                        lst[i].append("→")
                    else:
                        lst[i].append(".")
                elif i==15:
                    if 3<=j<=6 or 12<=j<=14:
                        lst[i].append("←")
                    else:
                        lst[i].append(".")
                elif j==0:
                    if 3<=i<=6 or 12<=i<=14:
                        lst[i].append("↑")
                    else:
                        lst[i].append(".")
                elif j==15:
                    if 1<=i<=3 or 9<=i<=12:
                        lst[i].append("↓")
                    else:
                        lst[i].append(".")
                elif j==2 and i<=6:
                    lst[i].append(".")
                elif j==4 and i<=3:
                    lst[i].append("B")
                elif j==13 and i>=9:
                    lst[i].append(".")
                elif j==11 and i>=12:
                    lst[i].append("G")
                elif i==2 and j>=9:
                    lst[i].append(".")
                elif i==4 and j>=12:
                    lst[i].append("Y")
                elif i==13 and j<=6:
                    lst[i].append(".")
                elif i==11 and j<=3:
                    lst[i].append("R")
                else:
                    lst[i].append(" ")
        return lst
    def printBoard(self):
        print("It's your turn player " + self.__currentPlayer)
        for i in range (16):
            for j in range (16):
                print(self.__board[i][j],"",end="")
            print()
    def currentPlayer(self):
        return self.__currentPlayer
    def switchPlayer(self):
        if self.__currentPlayer=="B":
            self.__currentPlayer="Y"
        elif self.__currentPlayer=="Y":
            self.__currentPlayer="G"
        elif self.__currentPlayer=="G":
            self.__currentPlayer="R"
        elif self.__currentPlayer=="R":
            self.__currentPlayer="B"
    def validCoord(self,c):
        if len(c)==5 or len(c)==6 or len(c)==7:
            if c[0]=="(" and c[2]=="," and c[-1]==")":
                if (len(c)==5 and c[1].isdigit()==True and c[3].isdigit()==True) or (len(c)==6 and c[1].isdigit()==True and c[3].isdigit()==True and c[4].isdigit()==True):
                    if (len(c)==5 and float(c[1])%1==0 and float(c[3])%1==0) or (len(c)==6 and float(c[1])%1==0 and float((float(c[3])*10)+float(c[4]))%1==0):
                        if len(c)==5:
                            coord=(int(c[1]),int(c[3]))
                        elif len(c)==6:
                            coord=(int(c[1]),int((float(c[3])*10)+float(c[4])))
                        if coord[0]==0 or coord[0]==15 or coord[1]==0 or coord[1]==15:
                            return coord
                        elif coord[0]==2 and 10<=coord[1]<=14:
                            return coord
                        elif coord[0]==13 and 1<=coord[1]<=5:
                            return coord
                        elif coord[1]==2 and 1<=coord[0]<=5:
                            return coord
                        elif coord[1]==13 and 10<=coord[0]<=14:
                            return coord
            elif c[0]=="(" and c[3]=="," and c[-1]==")":
                if (len(c)==6 and c[1].isdigit()==True and c[2].isdigit()==True and c[4].isdigit()==True) or (len(c)==7 and c[1].isdigit()==True and c[2].isdigit()==True and c[4].isdigit()==True and c[5].isdigit()==True):
                    if (len(c)==6 and float((float(c[1])*10)+float(c[2]))%1==0 and float(c[4])%1==0) or (len(c)==7 and float((float(c[1])*10)+float(c[2]))%1==0 and float((float(c[4])*10)+float(c[5]))%1==0):
                        if len(c)==6:
                            coord=(int((float(c[1])*10)+float(c[2])),int(c[4]))
                        elif len(c)==7:
                            coord=(int((float(c[1])*10)+float(c[2])),int((float(c[4])*10)+float(c[5])))
                        if coord[0]==0 or coord[0]==15 or coord[1]==0 or coord[1]==15:
                            return coord
                        elif coord[0]==2 and 10<=coord[1]<=14:
                            return coord
                        elif coord[0]==13 and 1<=coord[1]<=5:
                            return coord
                        elif coord[1]==2 and 1<=coord[0]<=5:
                            return coord
                        elif coord[1]==13 and 10<=coord[0]<=14:
                            return coord
        return False
    def validLetter(self,coord):
        if self.__board[coord[0]][coord[1]]==self.__currentPlayer:
            return True
        else:
            return False
    def moveFromStart(self):
        if self.__board[self.__startSpace[self.__currentPlayer][0]][self.__startSpace[self.__currentPlayer][1]]!=self.__currentPlayer and self.__board[self.__startSpace[self.__currentPlayer][0]][self.__startSpace[self.__currentPlayer][1]]!=".":
            self.moveToStart(self.__board[self.__startSpace[self.__currentPlayer][0]][self.__startSpace[self.__currentPlayer][1]],self.__startSpace[self.__currentPlayer])
        if self.__currentPlayer=="B":
            x=1
            y=4
            if self.__board[x][y]=="B":
                self.__board[0][4]="B"
                while(True):
                    if self.__board[x+1][y]!="B":
                        self.__board[x][y]=" "
                        break
                    x+=1
        elif self.__currentPlayer=="Y":
            x=4
            y=14
            if self.__board[x][y]=="Y":
                self.__board[4][15]="Y"
                while(True):
                    if self.__board[x][y-1]!="Y":
                        self.__board[x][y]=" "
                        break
                    y-=1
        elif self.__currentPlayer=="G":
            x=14
            y=11
            if self.__board[x][y]=="G":
                self.__board[15][11]="G"
                while(True):
                    if self.__board[x-1][y]!="G":
                        self.__board[x][y]=" "
                        break
                    x-=1   
        elif self.__currentPlayer=="R":
            x=11
            y=1
            if self.__board[x][y]=="R":
                self.__board[11][0]="R"
                while(True):
                    if self.__board[x][y+1]!="R":
                        self.__board[x][y]=" "
                        break
                    y+=1
    def pawnAtStart(self):
        if self.__board[self.__startPawn[self.__currentPlayer][0]][self.__startPawn[self.__currentPlayer][1]]==self.__currentPlayer:
            if self.__board[self.__startSpace[self.__currentPlayer][0]][self.__startSpace[self.__currentPlayer][1]]=="." or self.__board[self.__startSpace[self.__currentPlayer][0]][self.__startSpace[self.__currentPlayer][1]]!=self.__currentPlayer:
                return False
        return True
    def moveToStart(self,player,coord):
        if player=="B":
            x=1
            y=4
            while(True):
                if self.__board[x][y]!=player:
                    self.__board[x][y]=player
                    return True
                x+=1
        elif player=="Y":
            x=4
            y=14
            while(True):
                if self.__board[x][y]!=player:
                    self.__board[x][y]=player
                    return True
                y-=1
        elif player=="G":
            x=14
            y=11
            while(True):
                if self.__board[x][y]!=player:
                    self.__board[x][y]=player
                    return True
                x-=1
        elif player=="R":
            x=11
            y=1
            while(True):
                if self.__board[x][y]!=player:
                    self.__board[x][y]=player
                    return True
                y+=1
        if coord[0]==0 and (1<=coord[1]<=3 or 9<=coord[1]<=12):
            self.__board[coord[0]][coord[1]]="→"
        elif coord[0]==15 and (3<=coord[1]<=6 or 12<=coord[1]<=14):
            self.__board[coord[0]][coord[1]]="←"
        elif coord[1]==0 and (3<=coord[0]<=6 or 12<=coord[0]<=14):
            self.__board[coord[0]][coord[1]]="↑"
        elif coord[1]==15 and (1<=coord[0]<=3 or 9<=coord[0]<=12):
            self.__board[coord[0]][coord[1]]="↓"
        else:
            self.__boord[coord[0]][coord[1]]="."
    def cardGenerator(self):
        import random
        card=random.choice(self.__cards)
        return card
    def validSorryCoord(self,c):
        if self.validCoord(c)!=False and self.validOtherLetter(self.validCoord(c))==True:
            return True
        else:
            return False
    def validOtherLetter(self,coord):
        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
            return True
        else:
            return False
    def sorryCard(self,coord):
        self.moveToStart(self.__board[coord[0]][coord[1]],coord)
        if self.__currentPlayer=="B":
            x=1
            y=4
            if self.__board[x][y]=="B":
                while(True):
                    if self.__board[x+1][y]!="B":
                        self.__board[x][y]=" "
                        break
                    x+=1
        elif self.__currentPlayer=="Y":
            x=4
            y=14
            if self.__board[x][y]=="Y":
                while(True):
                    if self.__board[x][y-1]!="Y":
                        self.__board[x][y]=" "
                        break
                    y-=1
        elif self.__currentPlayer=="G":
            x=14
            y=11
            if self.__board[x][y]=="G":
                while(True):
                    if self.__board[x-1][y]!="G":
                        self.__board[x][y]=" "
                        break
                    x-=1   
        elif self.__currentPlayer=="R":
            x=11
            y=1
            if self.__board[x][y]=="R":
                while(True):
                    if self.__board[x][y+1]!="R":
                        self.__board[x][y]=" "
                        break
                    y+=1
        self.__board[coord[0]][coord[1]]=self.__currentPlayer
    def pawnOnBoard(self):
        lst=[0,15]
        for i in lst:
            for j in range(16):
                if self.__board[i][j]==self.__currentPlayer or self.__board[j][i]==self.__currentPlayer:
                    return True
        x=self.__safeSpace[self.__currentPlayer][0]
        y=self.__safeSpace[self.__currentPlayer][1]
        for k in range(5):
            if self.__currentPlayer=="B":
                if self.__board[x][y]==self.__currentPlayer:
                    return True
                x+=1
            elif self.__currentPlayer=="Y":
                if self.__board[x][y]==self.__currentPlayer:
                    return True
                y-=1
            elif self.__currentPlayer=="G":
                if self.__board[x][y]==self.__currentPlayer:
                    return True
                x-=1
            elif self.__currentPlayer=="R":
                if self.__board[x][y]==self.__currentPlayer:
                    return True
                y+=1
        else:
            return False
    def otherPawnOnBoard(self):
        lst=[0,15]
        for i in lst:
            for j in range(16):
                if (self.__board[i][j]!=self.__currentPlayer and self.__board[i][j] not in self.__boardSpace) or (self.__board[j][i]!=self.__currentPlayer and self.__board[j][i] not in self.__boardSpace):
                    return True
        else:
            return False
    def pawnNumber(self):
        num=0
        lst=[0,15]
        for i in lst:
            for j in range(16):
                if self.__board[i][j]==self.__currentPlayer:
                    num+=1
                if self.__board[j][i]==self.__currentPlayer:
                    num+=1
        x=self.__safeSpace[self.__currentPlayer][0]
        y=self.__safeSpace[self.__currentPlayer][1]
        for k in range(5):
            if self.__currentPlayer=="B":
                if self.__board[x][y]==self.__currentPlayer:
                    num+=1
                x+=1
            elif self.__currentPlayer=="Y":
                if self.__board[x][y]==self.__currentPlayer:
                    num+=1
                y-=1
            elif self.__currentPlayer=="G":
                if self.__board[x][y]==self.__currentPlayer:
                    num+=1
                x-=1
            elif self.__currentPlayer=="R":
                if self.__board[x][y]==self.__currentPlayer:
                    num+=1
                y+=1
        return num
    def takeTurn(self,coord,card):
        orgBoard=self.__board
        orgCoord=coord
        x=1
        y=1
        if coord[0]==0 and coord[1]!=15:
            for i in range(card):
                if self.__currentPlayer=="B" and 0<=coord[0]<=6 and coord[1]==2:
                    if coord[0]+(card-i)<=6:
                        coord=(coord[0]+x,coord[1])
                    else:
                        return False
                elif self.__currentPlayer=="Y" and 9<=coord[1]<=15 and coord[0]==2:
                    if coord[1]-(card-i)>=9:
                        coord=(coord[0],coord[1]-y)
                    else:
                        return False
                elif self.__currentPlayer=="G" and 9<=coord[0]<=15 and coord[1]==13:
                    if coord[0]-(card-i)>=9:
                        coord=(coord[0]-x,coord[1])
                    else:
                        return False
                elif coord[0]!=0 and coord[1]==15 and coord[0]!=15:
                    coord=(coord[0]+x,coord[1])
                elif coord[0]==0 and coord[1]==15:
                    coord=(1,15)
                elif coord[0]==15 and coord[1]==15:
                    coord=(15,14)
                elif coord[0]==15:
                    coord=(coord[0],coord[1]-y)
                else:
                    coord=(coord[0],coord[1]+y)
                if self.__currentPlayer!="B" and self.__board[coord[0]][coord[1]]=="→":
                    while(self.__board[coord[0]][coord[1]]=="→"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0],coord[1]+y)
                elif self.__currentPlayer!="Y" and self.__board[coord[0]][coord[1]]=="↓":
                    while(self.__board[coord[0]][coord[1]]=="↓"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0]+x,coord[1])
                elif self.__currentPlayer!="G" and self.__board[coord[0]][coord[1]]=="←":
                    while(self.__board[coord[0]][coord[1]]=="←"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0],coord[1]-y)
        elif coord[1]==15 and coord[0]!=15:
            for i in range(card):
                if self.__currentPlayer=="Y" and 9<=coord[1]<=15 and coord[0]==2:
                    if coord[1]-(card-i)>=9:
                        coord=(coord[0],coord[1]-y)
                    else:
                        return False
                elif self.__currentPlayer=="G" and 9<=coord[0]<=15 and coord[1]==13:
                    if coord[0]-(card-i)>=9:
                        coord=(coord[0]-x,coord[1])
                    else:
                        return False
                elif self.__currentPlayer=="R" and 0<=coord[1]<=6 and coord[0]==13:
                    if coord[1]+(card-i)<=6:
                        coord=(coord[0],coord[1]+y)
                    else:
                        return False
                elif coord[0]==15 and coord[1]!=15 and coord[1]!=0:
                    coord=(coord[0],coord[1]-y)
                elif coord[0]==15 and coord[1]==15:
                    coord=(15,14)
                elif coord[0]==15 and coord[1]==0:
                    coord=(14,0)
                elif coord[1]==0:
                    coord=(coord[0]-x,coord[1])
                else:
                    coord=(coord[0]+x,coord[1])
                if self.__currentPlayer!="Y" and self.__board[coord[0]][coord[1]]=="↓":
                    while(self.__board[coord[0]][coord[1]]=="↓"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0]+x,coord[1])
                elif self.__currentPlayer!="G" and self.__board[coord[0]][coord[1]]=="←":
                    while(self.__board[coord[0]][coord[1]]=="←"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0],coord[1]-y)
                elif self.__currentPlayer!="R" and self.__board[coord[0]][coord[1]]=="↑":
                    while(self.__board[coord[0]][coord[1]]=="↑"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0]-x,coord[1])
        elif coord[0]==15 and coord[1]!=0:
            for i in range(card):
                if self.__currentPlayer=="G" and 9<=coord[0]<=15 and coord[1]==13:
                    if coord[0]-(card-i)>=9:
                        coord=(coord[0]-x,coord[1])
                    else:
                        return False
                elif self.__currentPlayer=="R" and 0<=coord[1]<=6 and coord[0]==13:
                    if coord[1]+(card-i)<=6:
                        coord=(coord[0],coord[1]+y)
                    else:
                        return False
                elif self.__currentPlayer=="B" and 0<=coord[0]<=6 and coord[1]==2:
                    if coord[0]+(card-i)<=6:
                        coord=(coord[0]+x,coord[1])
                    else:
                        return False
                elif coord[0]!=15 and coord[1]==0 and coord[0]!=0:
                    coord=(coord[0]-x,coord[1])
                elif coord[0]==15 and coord[1]==0:
                    coord=(14,0)
                elif coord[0]==0 and coord[1]==0:
                    coord=(0,1)
                elif coord[0]==0:
                    coord=(coord[0],coord[1]+y)   
                else:
                    coord=(coord[0],coord[1]-y)
                if self.__currentPlayer!="G" and self.__board[coord[0]][coord[1]]=="←":
                    while(self.__board[coord[0]][coord[1]]=="←"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0],coord[1]-y)
                elif self.__currentPlayer!="R" and self.__board[coord[0]][coord[1]]=="↑":
                    while(self.__board[coord[0]][coord[1]]=="↑"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0]-x,coord[1])
                elif self.__currentPlayer!="B" and self.__board[coord[0]][coord[1]]=="→":
                    while(self.__board[coord[0]][coord[1]]=="→"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0],coord[1]+y)
        elif coord[1]==0 and coord[0]!=0:
            for i in range(card):
                if self.__currentPlayer=="R" and 0<=coord[1]<=6 and coord[0]==13:
                    if coord[1]+(card-i)<=6:
                        coord=(coord[0],coord[1]+y)
                    else:
                        return False
                elif self.__currentPlayer=="B" and 0<=coord[0]<=6 and coord[1]==2:
                    if coord[0]+(card-i)<=6:
                        coord=(coord[0]+x,coord[1])
                    else:
                        return False
                elif self.__currentPlayer=="Y" and 9<=coord[1]<=15 and coord[0]==2:
                    if coord[1]-(card-i)>=9:
                        coord=(coord[0],coord[1]-y)
                    else:
                        return False
                elif coord[0]==0 and coord[1]!=0 and coord[1]!=15:
                    coord=(coord[0],coord[1]+y)
                elif coord[0]==0 and coord[1]==0:
                    coord=(0,1)
                elif coord[0]==0 and coord[1]==15:
                    coord=(1,15)
                elif coord[1]==15:
                    coord=(coord[0]+x,coord[1])
                else:
                    coord=(coord[0]-x,coord[1])
                if self.__currentPlayer!="R" and self.__board[coord[0]][coord[1]]=="↑":
                    while(self.__board[coord[0]][coord[1]]=="↑"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0]-x,coord[1])
                elif self.__currentPlayer!="B" and self.__board[coord[0]][coord[1]]=="→":
                    while(self.__board[coord[0]][coord[1]]=="→"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0],coord[1]+y)
                elif self.__currentPlayer!="Y" and self.__board[coord[0]][coord[1]]=="↓":
                    while(self.__board[coord[0]][coord[1]]=="↓"):
                        if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                            self.moveToStart(self.__board[coord[0]][coord[1]],coord)
                        coord=(coord[0]+x,coord[1])
        elif 1<=coord[0]<=6 and coord[1]==2:
            if coord[0]+card<=6:
                coord=(coord[0]+card,coord[1])
            else:
                return False
        elif 10<=coord[1]<=14 and coord[0]==2:
            if coord[1]-card>=9:
                coord=(coord[0],coord[1]-card)
            else:
                return False
        elif 10<=coord[0]<=14 and coord[1]==13:
            if coord[0]-card>=9:
                coord=(coord[0]-card,coord[1])
            else:
                return False
        elif 1<=coord[1]<=6 and coord[0]==13:
            if coord[1]+card<=6:
                coord=(coord[0],coord[1]+card)
            else:
                return False
        if self.__board[coord[0]][coord[1]]==self.__currentPlayer:
            self.__board=orgBoard
            return False
        else:
            if self.__board[coord[0]][coord[1]]!=self.__currentPlayer and self.__board[coord[0]][coord[1]] not in self.__boardSpace:
                self.moveToStart(self.__board[coord[0]][coord[1]],coord)
            if coord==(6,2) or coord==(2,9) or coord==(9,13) or coord==(13,6):
                self.home()
                self.__board[coord[0]][coord[1]]="."
                self.__board[orgCoord[0]][orgCoord[1]]="."
                return True
            else:
                self.__board[coord[0]][coord[1]]=self.__currentPlayer
                if orgCoord[0]==0 and (1<=orgCoord[1]<=3 or 9<=orgCoord[1]<=12):
                    self.__board[orgCoord[0]][orgCoord[1]]="→"
                elif orgCoord[0]==15 and (3<=orgCoord[1]<=6 or 12<=orgCoord[1]<=14):
                    self.__board[orgCoord[0]][orgCoord[1]]="←"
                elif orgCoord[1]==0 and (3<=orgCoord[0]<=6 or 12<=orgCoord[0]<=14):
                    self.__board[orgCoord[0]][orgCoord[1]]="↑"
                elif orgCoord[1]==15 and (1<=orgCoord[0]<=3 or 9<=orgCoord[0]<=12):
                    self.__board[orgCoord[0]][orgCoord[1]]="↓"
                else:
                    self.__board[orgCoord[0]][orgCoord[1]]="."
                return True
    def home(self):
        self.__homePawn[self.__currentPlayer]+=1
    def winner(self):
        if self.__homePawn[self.__currentPlayer]==3:
            score[s.currentPlayer()]+=1
            return True
        else:
            return False
    def resetRound(self):
        self.__board=self.listBoard()
        self.__currentPlayer="B"
        self.__cards=[1,2,3,4,5,6,7,8,9,10,11,12,"Sorry"]
        self.__playerPieces={"R":["R","R","R"],"B":["B","B","B"],"Y":["Y","Y","Y"],"G":["G","G","G"]}
        self.__homePawn={"R":0,"B":0,"Y":0,"G":0}
        self.__startPawn={"R":(11,1),"B":(1,4),"Y":(4,14),"G":(14,11)}
        self.__startSpace={"R":(11,0),"B":(0,4),"Y":(4,15),"G":(15,11)}
        self.__boardSpace=[".","→","←","↑","↓"]
        self.__safeSpace={"R":(13,1),"B":(1,2),"Y":(2,14),"G":(14,13)}
    def playerScoreCheck(self):
        print("Player B's score is " + str(self.__score["B"]) + "Player Y's score is " + str(self.__score["Y"]) + "Player G's score is " + str(self.__score["G"]) + "Player R's score is " + str(self.__score["R"]))
    def finalWinner(self):
        maxi=0
        for i in self.__score:
            if self.__score[i]>maxi:
                maxi=self.__score[i]
                winner=i
        print("Congratulations player " + winner + " you won Sorry!")
    
