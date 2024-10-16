import os

def sorter(k):
    return k.split("-")[1].split(".")[0]

files = os.listdir()
files = files[2:]
files.sort(key=lambda p: sorter(p))
print(files)
    

