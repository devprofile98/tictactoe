#تابع نمايش دادن تخته بازي
def showBoard(board):
    
    for i in board:
        print (i)
    print('\n')


#تابع اصلي بازي با استفاده از مينيماکس و آلفا بتاپرونينگ
#توضيح پارامتر هاي تابع
    
#height : اين ورودي هر بار که تابع صدا زده ميشود مقدار صفر دارد در بازگشت هاي تابع مقدار اين متغير حداکثر تا 8 زياد
        # مي شود ،مي توانستيم اين متغير را فقط درون تابع صدا زنيم و به صورت متغير پاس ندهيم
#maxi :
        #اين متغير به تابع مي گويد ميخاهيم بازيکن را ماکس کنيم يا مين
#A , B :
        #اين دو متغير مقادير آلفا و بتا هستند که براي هرس درخت استفاده مي کنيم
#player :
        #متغيري است که نشان دهنده ي علامت بازيکني اسن که اخرين حرکت را انجام داده 
def ABpruning(height,maxi,A,B,player):
    #اين سه شرط برابر با يوتيليتي فانکشن هاي الگوريتم ميني ماکس هستند که به صورت بيس کيس هاي تابع نوشته شده اند
    if checkVictory(board) == 'O':
        return 10,0,0
    
    elif checkVictory(board) == 'X':    
        return -10,0,0
    
    elif height==8:
        return 0,0,0

    #اينجا پلير را به پلير بعدي تغير ميدهيم ميتوانستيم اين کار را با پاس دادن بازيکني ک بازي را انجام نداده جايگزين
    #کنيم ولي شکل اول واضح تر و روشن تر بوذ
    if player == 'O':
        player = 'X'
    else:
        player = 'O'


    #اين شرط  براي ما کا بيشينه سازي بازي به نفع پلير را انجام ميدهد    
    if maxi:
        #متغير هاي زير براي ذخيره ي سطر و ستون بهترين جوابي که به دست مي ايد استفائه ميکنيم ک ب صورت بازگشتي پر ميشوند
        x=0
        y=0
        Heval = -100000
        #با اين دو حلقه تمام حرکاتي که مي توان روي خانه هاي خالي انجام داد را توليد ميکنيم
        for i in range(3):
            for j in range(3):
                #بررسي شرط خالي بودن اين خانه از قبل
                if board[i][j] == '-':
                    #اينجا خانه را برابر با مقدار بازيکن که بالاتر تعيين کرديم قرار مي دهيم و يک بار ديگر تابع را صدا ميزنيم اما
                    #اينبار ميخاهيم که حرکات حربف را مينيمم کند پس براي متغير دوم فالس را پاس ميدهيم و ارتفاع را يک واحد افزايش
                    #مي دهيم
                    board[i][j] = player
                    childH=ABpruning(height+1,False,A,B,player)
                    #با اين شرط سعي در پيدا کردن مقدار ماکزيموم در بين فرزندان داريم
                    if Heval >=childH[0]:
                        Heval = Heval
                    else:
                        Heval = childH[0]
                        x = i
                        y = j

                    #اينجا خانه اي را با مقدار بازيکن پر کرديم خالي ميکنيم تا روي حرکت هاي بعدي تاثير نگذارد
                    board[i][j] = '-'
                    #از اين شرط براي هرس کردن درخت استفاده کرديم
                    if B <= A:
                    	return Heval,x,y   
                    A = max(A,Heval)
        return Heval,x,y
    #اين شرط براي کمينه سازي بازيکن حريف است
    else:
        x=0
        y=0
        Hmin = 100000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = player
                    childH=ABpruning(height+1,True,A,B,player)
                    if Hmin<=childH[0]:
                        Hmin = Hmin
                    else:
                        Hmin = childH[0]
                        x = i
                        y = j
                    board[i][j]= '-'
                   
                    if B<=A:
                        return Hmin,x,y
                    B = min(B,Hmin)
        return Hmin,x,y


#تابع براي چک کردن پيروزي و اتمام بازي        
def checkVictory(board):
    #در حلقه تمام حالت هاي پيروزي ستوني و سطري بازي  را بررسي مي کنيم
    for i in range(3):
        if board[i][0] == board[i][1]==board[i][2] and board[i][0]!='-' :
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]and board[0][i]!='-':
            return board[0][i]
    #ابنجا روش هاي پيروزي در حالت هاي اوريب  را بررسي مي کنيم
    if board[0][0] == board[1][1] ==board[2][2] and board[0][0]!='-':
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0]!='-':
        return board[2][0]

    #اينجا تساوي يازي را ب سادگي چک ميکنيم
    if board[0][0]!='-' and board[0][1]!='-' and board[0][2]!='-' and board[1][0]!='-' and board[1][1]!='-' and board[1][2]!='-' and board[2][0]!='-' and board[2][1]!='-' and board[2][2]!='-':
        return 'draw'


#تابع براي حلقه ايجاد بازي 
def game(board):
    print("You vs AI")
    print ("You are X")
    showBoard(board)
    for i in range(8):
        V = checkVictory(board)
        #در اين مرحله بررسي ميکنيم مقدار تابع چک کردن پيروزي تا پيروز بازي زا اعلام کنيم و حلقه را بشکنيم
        if V=='X' or V=='O':
            print (V," won the game ")
            break
        elif V == 'draw': 
            print ('DRAW')
            break
        a,b = input("your turn : ").split(",")
        #بعد از گرفتن ورودي از حريف چک ميکنيم اگر خانه با - پر شده بود يعني که هنوز قابل استفاده است
        if board[int(a)][int(b)] == '-':
            board[int(a)][int(b)] = 'X'
            response = ABpruning(0,True,-1000,1000,'X')
            
            print (response)
            board[response[1]][response[2]] = 'O'
            showBoard(board)

        else:
            print ("please choose another one")

        
#برد بازي را به اين صورت تعريف مي کنيم ک هر خانه اي که - قرار داشته باشد يعني هنوز ميتوانيم در ان مقاديري قرار دهيم
#يک ليست 2 بعدي براي تخته بازي در نظر ميگيريم
#کامپيوتر براي شروع بازي اولين مقدار خود را در خانه ي وسط قرار مي دهيم 
board =[
    ['-','-','-'],
    ['-','O','-'],
    ['-','-','-']
    ]

game(board)




