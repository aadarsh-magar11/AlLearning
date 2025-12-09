import os
currdir = os.getcwd()
print(currdir)
with open("Original.JPG", "rb") as original:
    with open("Copy.JPG", "wb") as copy:
        copy.write(original.read())