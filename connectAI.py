#
#
#
#
# Name: Fabio Amendola

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        
        # and the numbers underneath here
        s += '\n'
        for i in range(W):
            s+= ' ' + str(i)
        
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ This method takes two inputs: the first input col represents 
            the index of the column to which the checker will be added; 
            the second input ox will be a 1-character string representing 
            the checker to add to the board. That is, ox should either be 
            'X' or 'O' (again, capital O, not zero).
        """
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col] = ox

    def clear(self):
    	""" clears board
    	"""
    	for row in range(len(b.data)):
    		for col in range(len(b.data[row])):
    			b.data[row][col] = ' '

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self,c):
        """ This method should return True if the calling object 
            (of type Board) does allow a move into column c. It returns 
            False if column c is not a legal column number for the calling 
            object. It also returns False if column c is full.
        """
        H = self.height
        W = self.width
        D = self.data
        if c >= W or c < 0:
            return False
        elif D[0][c] != ' ':
            return False
        else:
            return True


    def isFull(self):
        """ This method should return True if the calling object 
            (of type Board) is completely full of checkers. It should 
            return False otherwise.
        """
        H = self.height
        W = self.width
        D = self.data
        for row in range(H):
            for col in range(W):
                if D[row][col] == ' ':
                    return False
        return True


    def delMove(self, c):
        """ This method should do the opposite of addMove. It should 
            remove the top checker from the column c. If the column is 
            empty, then delMove should do nothing.
        """
        H = self.height
        for row in range(0,H):
            if self.data[row][c] != ' ':
                self.data[row][c] = ' '

    def winsFor(self,ox):
        H = self.height
        W = self.width
        D = self.data
        # check for horizontal wins
        
        for row in range(0,H):
            for col in range(0,W-3):
                """if D[row][col] == ox and \
                    D[row][col+1] == ox and \
                    D[row][col+2] == ox and \
                    D[row][col+3] == ox:
                    return True"""
                if D[row][col] == ox:
                    if inarow_Neast(ox, row,col,D,4) == True:
                        return True
                    elif inarow_Nsouth(ox,row,col,D,4) == True:
                        return True
                    elif inarow_Nnortheast(ox,row,col,D,4):
                        return True
                    elif inarow_Nsoutheast(ox,row,col,D,4):
                        return True
        return False

    def hostGame(self):
        """ This method brings everything together into the familiar game... 
            It should host a game of connect four, using the methods listed 
            above to do so.
        """
        print "Welcome to Connect Four!"
        print
        while True:
            print self
            print

            x_col = -1
            while self.allowsMove( x_col ) == False:
                x_col = input("X's Choice: ")
            self.addMove(x_col, 'X')
            if self.winsFor('X') == True:
                print
                print "X wins ----- Congratulations"
                print self
                break
            print self
            print

            o_col = -1
            while self.allowsMove( o_col ) == False:
                o_col = input("O's Choice: ")
            self.addMove(o_col, 'O')
            if self.winsFor('O') == True:
                print "O wins ----- Congratulations"
                print self
                break
            print self
            print





def inarow_Neast(ch, r_start,c_start,A,N):
    """ should start from r_start and c_start and check for N-in-a-row eastward 
        of element ch, returning True or False, as appropriate
    """
    if c_start < len(A[r_start]) - N+1:
        for i in range(c_start, c_start+N):
            if ch != A[r_start][i]:
                return False
        return True
    else:
        return False


def inarow_Nsouth(ch,r_start,c_start,A,N):
    """ should start from r_start and c_start and check for N-in-a-row 
        southward of element ch, returning True or False, as appropriate
    """
    if r_start < len(A) - N+1:
        for i in range(r_start, r_start+N):
            if ch != A[i][c_start]:
                return False
        return True
    else:
        return False

def inarow_Nsoutheast(ch,r_start,c_start,A,N):
    """ should start from r_start and c_start and check for N-in-a-row 
        southeastward of element ch, returning True or False, as appropriate
    """
    if r_start < len(A) - N+1 and c_start < len(A[r_start]) - N+1:
        for i in range(0,N):
            if ch != A[r_start+i][c_start+i]:
                return False
        return True
    else:
        return False


def inarow_Nnortheast(ch,r_start,c_start,A,N):
    """ this should start from r_start and c_start and check for N-in-a-row 
        northeastward of element ch, returning True or False, as appropriate
    """
    if r_start > len(A) - N+1 and c_start < len(A[r_start]) - N+1:
        for i in range(N):
            if ch != A[r_start-i][c_start+i]:
                return False
        return True
    else:
        return False