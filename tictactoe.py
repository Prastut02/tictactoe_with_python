#ticitactoe(PvP)
#game board
while True:
    l=[]
    for i in range(1,10):
        l.append(i)
    def disp_board():
        c=0
        for a in l:
            print(str(a), end='')
            c+=1
            if c%3==0:
                print()

                           
    # Prompt to allow users to enter their names
    global p1,p2
    p1=input("Player1's name: ")
    p2=input("Player2's name: ")

    # A funtion that decides 'X' and 'O'
    def decider(p1,p2):
        global p,y
        import random
        r=random.randint(0,2)
        if r==0:
            print(p1 + " is 'O'" + " and " + p2 + " is 'X'")
            p='O'
            y='X'
        else:
            print(p1 + " is 'X'" + " and " + p2 + " is 'O'")
            p='X'
            y='O'
            
    decider(p1,p2)
    disp_board()

    # Prompt users for their moves
    print("Use the numbers from 1-9 to specify your moves")
    def moves():
        w=0
        global p1,p2
        global p,y
        count=1
        n=1
        while count<10:
                if n%2==1:
                    while True:
                        try:
                            mv1=int(input(p1+"'s turn: "))
                            if type(mv1)!=str and mv1>0 and mv1<10:
                                break
                            else:
                                print("Invalid input. Enter numbers from 1-9")
                        except ValueError:
                            print("Invalid input. Enter numbers from 1-9")       
                    if l[mv1-1]=='X' or l[mv1-1]=='O':
                        print("The position's occupied")
                        mv1=int(input(p1+" enter again: "))
                    l[mv1-1]=p
                    disp_board()
                    print()
                else:
                    while True:
                        try:
                            mv1=int(input(p2+"'s turn: "))
                            if type(mv1)!=str and mv1>0 and mv1<10:
                                break
                            else:
                                print("Invalid input. Enter numbers from 1-9")
                        except ValueError:
                            print("Invalid input. Enter numbers from 1-9")
                    if l[mv1-1]=='X' or l[mv1-1]=='O':
                        print("The position's occupied")
                        mv1=int(input(p2+" enter again: "))
                    l[mv1-1]=y
                    disp_board()
                    print()
                n+=1
                count+=1
                if count>5:
                    if l[0]==l[1]==l[2]:
                        if n%2==0:
                            print(f"{p1} wins")
                            w=1
                            break
                        else:
                            print(f"{p2} wins")
                            w=1
                            break
                    elif l[3]==l[4]==l[5]:
                        if n%2==0:
                            print(f"{p1} wins")
                            w=1
                            break
                        else:
                            print(f"{p2} wins")
                            w=1
                            break
                    elif l[6]==l[7]==l[8]:
                        if n%2==0:
                            print(f"{p1} wins")
                            w=1
                            break
                        else:
                            print(f"{p2} wins")
                            w=1
                            break
                    elif l[0]==l[3]==l[6]:
                        if n%2==0:
                            print(f"{p1} wins")
                            w=1
                            break
                        else:
                            print(f"{p2} wins")
                            w=1
                            break
                    elif l[1]==l[4]==l[7]:
                        if n%2==0:
                            print(f"{p1} wins")
                            w=1
                            break
                        else:
                            print(f"{p2} wins")
                            w=1
                            break
                    elif l[2]==l[5]==l[8]:
                        if n%2==0:
                            print(f"{p1} wins")
                            w=1
                            break
                        else:
                            print(f"{p2} wins")
                            w=1
                            break
                    elif l[0]==l[4]==l[8]:
                        if n%2==0:
                            print(f"{p1} wins")
                            w=1
                            break
                        else:
                            print(f"{p2} wins")
                            w=1
                            break
                    elif l[2]==l[4]==l[6]:
                        if n%2==0:
                            print(f"{p1} wins")
                            w=1
                            break
                        else:
                            print(f"{p2} wins")
                            w=1
                            break
        if w==0:
            print("It's a draw.")
                    
                
    moves()
    ak=input("Play Again?[y/n]")
    if ak.upper()=='N':
        break
        


