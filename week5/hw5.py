#################################################
# Hw5
# Your andrewID:
#################################################

import cs112_s19_week5_linter

#####################################
# COLLABORATIVE Non-Animation Problems
# Collaborators:
#####################################

def nondestructiveRemoveRowAndCol(lst, row, col):
    return [42]

def destructiveRemoveRowAndCol(lst, row, col):    
    return None    

def bestQuiz(a):
    return 42

#####################################
# Solo Non-Animation Problems
# No collaborators allowed here
#####################################

def areLegalValues(a):
    return False

def isLegalRow(board, row):
    return False

def isLegalCol(board, col):
    return False

def isLegalBlock(board, block):
    return False

def isLegalSudoku(board):
    return False 

#################################################
# ignore_rest: The autograder will not look at 
# anything below here.  The graphics problems
# will go below.
#################################################

#####################################
# Solo Animation Problem
# No collaborators allowed here
#####################################

from tkinter import *

#### Sudoku Animation ####

def init(data):
    pass

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def redrawAll(canvas, data):
    pass

def runSudoku(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed    

#################################################
# Test code is below here
#################################################

def testNondestructiveRemoveRowAndCol():
    print("Write your own tests for nondestructiveRemoveRowAndCol!")

def testDestructiveRemoveRowAndCol():
    print("Write your own tests for destructiveRemoveRowAndCol!")

def testBestQuiz():
    print("Write your own tests for bestQuiz!")

def testAreLegalValues():
    print("Write your own tests for areLegalValues!")

def testIsLegalRow():
    print("Write your own tests for isLegalRow!")

def testIsLegalCol():
    print("Write your own tests for isLegalCol!")

def testIsLegalBlock():
    print("Write your own tests for isLegalBlock!")

def testIsLegalSudoku():
    print("Write your own tests for isLegalSudoku!")

def testSudokuAnimation():
    print("Running Sudoku Animation...", end="")
    # Feel free to change the width and height!
    width = 500
    height = 500
    runSudoku(width, height)
    print("Done!")

def testAll():    
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testBestQuiz()
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()
    testSudokuAnimation()

def main():
    cs112_s19_week5_linter.lint() # check rules
    testAll()

if __name__ == '__main__':
    main()