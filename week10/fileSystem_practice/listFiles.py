import os

def listFiles(path):
    # base case: file
    if not os.path.isdir(path):
        return [path]
    # recursive case: folder
    else:
        result = []
        for filename in os.listdir(path):
            result += listFiles(path + "/" + filename)
        return result


print(listFiles('sampleFiles'))
