from WordleGame import *
from ConnectGame import *
from BattleGame import *
from SorryGame import *
def main():
    print("Welcome to the Mini game system.")
    while(True):
        print()
        print("Choose what game you would like to play.")
        print("  0. Quit Mini Game System")
        print("  1. Connect Four")
        print("  2. Battle Ship")
        print("  3. Sorry")
        print("  4. Wordle")
        while(True):
            option=input("Enter 0, 1, 2, 3, or 4: ")
            print()
            if str(option).isdigit()==True and float(option)%1==0:
                option=int(option)
                if option==0 or option==1 or option==2 or option==3 or option==4:
                    break
            print("Please input an option ranging from 0-3.")
            print()
        if option==0:
            print("Thank you for using the Mini Game System!")
            break
        elif option==1:
            C=ConnectFour()
            C.instructions()
            while(True):
                print()
                roundNum=input("How many rounds would you like to play: ")
                if str(roundNum).isdigit()==True and float(roundNum)%1==0:
                    roundNum=int(roundNum)
                    break
                print("The number of rounds have to be a whole number greater than zero. Please try again.")
            for i in range(1,roundNum+1):
                print()
                print("Round " + str(i))
                print()
                for j in range(42):
                    C.printBoard()
                    if C.currentPlayer()=="A":
                        print("It's player A's turn to play.")
                    elif C.currentPlayer()=="B":
                        print("It's player B's turn to play.")
                    while(True):
                        print()
                        col=input("Enter the column that you would like your letter to fall (columns range from 0-6). ")
                        if str(col).isdigit()==True and float(col)%1==0:
                            col=int(col)
                            if 0<=col<=6:
                                break
                        print("This is an invalid column number. Please try again.")
                    print()
                    while(True):
                        if C.fullColumn(col)==True:
                            print("This column is already full. Please try again.")
                            while(True):
                                print()
                                col=input("Enter the column that you would like your letter to fall (columns range from 0-6). ")
                                if str(col).isdigit()==True and float(col)%1==0:
                                    col=int(col)
                                    if 0<=col<=6:
                                        break  
                                print("This is an invalid column number. Please try again.")
                        else:
                            C.takeTurn(col)
                            break
                    if j==41 and C.winner()==False:
                        print("It's a tie!")
                        C.resetRound()
                    elif C.winner()==True:
                        C.printBoard()
                        C.scoreCount()
                        C.getScore()
                        print("Congratulations " + C.previousPlayer() + " you won the round!")
                        C.resetRound()
                        break
            print()
            C.finalWinner()
            print("Thank you for playing Connect Four!")     
        elif option==2:
            B=BattleShip()
            B.instructions()
            while(True):
                print()
                rounds=input("How many rounds would you like to play: ")
                if str(rounds).isdigit()==True and float(rounds)%1==0:
                    rounds=int(rounds)
                    break
                print("The number of rounds have to be a whole number greater than zero. Please try again.")
            for i in range(1,rounds+1):
                print()
                print("Round "+str(i))
                for playerTurn in range(2):
                    print()
                    print("It's " + B.currPlayer() + "'s turn to play.")
                    for turn in range(5):
                        B.printBoards(B.currSetBoard())
                        while(True):
                            print()
                            print("Ship types: Carrier(5 spaces), Battleship(4 spaces), Cruiser(3 spaces), Submarine(3 spaces), Destroyer(2 spaces)")
                            shipType=(input("Please select a ship type: ")).lower()
                            if B.validShipType(shipType)==True:
                                break
                        while(True):
                            print()
                            c=input("Please select a coordinate on the grid to represent the back of the ship (rows and columns range from 0-9): ")
                            if B.validCoord(c)==True:
                                coord=(int(c[1]),int(c[3]))
                                print()
                                direc=(input("Please select a direction (N(North),S(South),E(East),W(West)) for the remainder of your ship to be positioned: ")).lower()
                                if B.validDirec(direc)==True:
                                    x=coord[0]
                                    y=coord[1]
                                    if B.validShipLocation(shipType,direc,x,y)==True:
                                        break
                        B.setShipLocation(B.currSetBoard(),shipType,direc,x,y)
                        print()
                    B.switchPlayer()
                while(True):
                    print()
                    print("It's " + B.currPlayer() + "'s turn to play.")
                    B.printBoards(B.currTargBoard())
                    while(True):
                        print()
                        B.playerScoreCheck()
                        c=input("Please select a coordinate on the grid to drop a missle (rows and columns range from 0-9): ")
                        if B.validCoord2(c)==True:
                            coord=(int(c[1]),int(c[3]))
                            x=coord[0]
                            y=coord[1]
                            B.takeTurn(B.currBoard(),B.currTargBoard(),x,y)
                            break
                    print()
                    B.printBoards(B.currTargBoard())
                    if B.winner()==True:
                        print("Congratulations " + B.currPlayer() + " you sunk all the battleships!")
                        break
                    B.switchPlayer()
                B.resetRound()
                B.playerScoreCheck()
            B.finalWinner()
            print("Thank you for playing Battleship!")
        elif option==3:
            s=Sorry()
            s.instructions()
            while(True):
                print()
                rounds=input("How many rounds would you like to play: ")
                if str(rounds).isdigit()==True and float(rounds)%1==0:
                    rounds=int(rounds)
                    break
                print("This is an invalid round number. Please try again.")
            for i in range(1,rounds+1):
                print()
                print("Round " + str(i)) 
                while(True):
                    print()
                    s.printBoard()
                    card=s.cardGenerator()
                    print("The card generated was: " + str(card))
                    if ((card==1 or card==2) and s.pawnAtStart()==False) or ((card!="Sorry") and s.pawnOnBoard()==True) or (card=="Sorry" and s.otherPawnOnBoard()==True):
                        while(True):
                            print("Choose what you would like to do.")
                            print("  1. Move pawn from start")
                            print("  2. Move piece from board")
                            print("  3. Skip turn")
                            option=input("Enter 1, 2, or 3 ")
                            if option=="1" and ((card!=1 and card!=2) or s.pawnAtStart()==True):
                                print()
                                print("You need to generate a card that says 1 or 2 in order to move a pawn from the start or you do not have any pawns at the start.")
                            elif option=="2" and s.pawnOnBoard()==False and card!="Sorry":
                                print()
                                print("You don't have any pawns on the board. Please try again.")
                            elif option!="1" and option!="2" and option!="3":
                                print()
                                print("You must select the option 1, 2, or 3. Please try again.")
                            else:
                                break
                            print()
                        if option=="1":
                            s.moveFromStart()
                        elif option=="2":
                            if card=="Sorry":
                                while(True):
                                    print()
                                    c1=input("Select a coordinate to replace another player's pawn and send their pawn to the start: ")
                                    if s.validSorryCoord(c1)==True:
                                        if (s.validCoord(c1)[0]==0 or s.validCoord(c1)[0]==15) or (s.validCoord(c1)[1]==0 or s.validCoord(c1)[1]==15):
                                            s.sorryCard(s.validCoord(c1))
                                            break
                                    print("This coordinate is invalid. Please Try again.")
                            elif str(card).isdigit()==True:
                                lst=[]
                                while(True):
                                    print()
                                    c=input("Select a coordinate to move one of your pawns on the board: ")
                                    if s.validCoord(c)!=False:
                                        if s.validLetter(s.validCoord(c))==True:
                                            if c not in lst:
                                                lst.append(c)
                                            if s.takeTurn(s.validCoord(c),card)==True:
                                                break
                                    if len(lst)==s.pawnNumber():
                                        print()
                                        print("You cannot make any moves.")
                                        break
                                    print("This coordinate is invalid. Please Try again.")
                    else:
                        print("You cannot make any moves.")      
                    if s.winner()==True:
                        print()
                        print("Congratulations player " + s.currentPlayer() + " you won the round!")
                        break
                    s.switchPlayer()
                s.resetRound()
                s.playerScoreCheck()
            s.finalWinner()
        elif option==4:
            w=Wordle()
            w.instructions()
            print()
            print("Choose wheter you would like to play single or multi player.")
            print("  1. Single Player")
            print("  2. Two Player")
            while(True):
                option=input("Enter 1 or 2: ")
                print()
                if str(option).isdigit()==True and float(option)%1==0:
                    option=int(option)
                    if option==1 or option==2:
                        break
                print("Please input an option ranging from 1-2.")
                print()
            while(True):
                rounds=input("How many rounds would you like to play?: ")
                print()
                if option==1 and rounds.isdigit()==True and float(rounds)%1==0:
                    rounds=int(rounds)
                    break
                elif option==2 and rounds.isdigit()==True and float(rounds)%1==0 and float(rounds)%2==0:
                    rounds=int(rounds)
                    break
                print("This is an invalid round number. If you chose option 2 make sure to enter an even number. Please try again.")
                print()
            for i in range (1,rounds+1):
                print("Round "+ str(i))
                print()
                if option==2:
                    w.currentPlayer()
                    print()
                word=w.randomWord(w.wordList())
                for i in range(1,7):
                    while(True):
                        guess=input("Enter your guess "+"("+str(i)+"): ").lower()
                        if w.validGuess(w.wordList(),guess)==True:
                            break
                    mark=w.takeTurn(guess,word)
                    if w.winner(mark)==True:
                        print()
                        break
                    elif i==6:
                        print()
                        w.loser(word)
                        break
                if option==2:
                    print()
                    w.score()
                    w.switchPlayer()
                    print()
                w.resetRound()
            if option==2:
                w.finalWinner()
            print()
            print("Thank you for playing Wordle!")
main()
