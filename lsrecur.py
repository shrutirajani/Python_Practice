import os

def myfunction(path):
    files = os.listdir(path)
    for file in files:
        extfile = path + '/' + file
        if os.path.isdir(extfile):
            myfunction(extfile)
        else:
            print(extfile)

myfunction(os.getcwd())
