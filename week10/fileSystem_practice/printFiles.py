import os

def printFiles(path):
    # base case: file, so print its path
    if not os.path.isdir(path):
        print(path)
    # recursive case: folder
    else:
        for filename in os.listdir(path):
            printFiles(path + "/" + filename)

printFiles('sampleFiles')