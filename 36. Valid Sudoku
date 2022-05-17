class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        


        def valid(boo,itm,pos):
            #check Row
            for i in range(len(boo[0])):
                if boo[pos[0]][i] == itm and pos[1]!=i:
                    return False
            
            #check column
            for i in range(len(boo)):
                if boo[i][pos[1]] == itm and pos[0] !=i:
                    return False
            #check for box
            box_x=pos[1]//3
            box_y =pos[0]//3
            
            for i in range(box_y*3,box_y*3+3):
                for j in range(box_x*3,box_x*3+3):
                    if boo[i][j] == itm and (i,j) != pos:
                        return False
            return True
        
        def checkElement(boo):
            for i in range(len(boo)):
                for j in range (len(boo[0])):
                    if boo[i][j] != '.':
                        print( valid(boo,boo[i][j],(i,j)) ,boo[i][j])
                        if valid(boo,boo[i][j],(i,j)):
                            continue
                        else:
                            return False
            return True
                
        return checkElement(board)
