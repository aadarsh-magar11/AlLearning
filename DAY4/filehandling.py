#opening a file in file is done using open() and opening file for reading can be done just by writing the name of the file
f = open("fileONE.txt","r")

'''
there are 4 different opening modes 'r' for reading
'w' for writing
'a' for appending a file
'x' for creating a new file and if the file already exists returns error

in addition files can be opened in binary modes using 'b' and in text mode using 't'
'''

#the contents of the file is read using .read() method
print(f.read())
f.close()
#file opens but first the directory must be changed

print("\n")

#File can be opened with "with" statement too 
with open("fileONE.txt") as new:
    print(new.read(9))

#it is always a good practice to close a file after it has been opened
# .readline() can be used to read a line of the file

naya = open("fileONE.txt")
print(naya.readline())
print(naya.readline())
naya.close()
#by repeating the .readline() with a certain amount of numbers we can read that number of lines that exist in the txt file
print("\n")

aarko = open("fileONE.txt")
for x in aarko:
    print(x)
aarko.close()

#appending in a file
with open("fileTWO.txt","a") as f:
    f.write("a new line has been added to the file")

with open("fileTWO.txt","r") as f:
    print(f.read())

#overwriting a file can be done using file opening method "w"
with open("fileTWO.txt","w") as file:
    file.write("ooh no!, i over wrote the file")

with open("fileTWO.txt","r") as file:
    print(file.read())

#a new file can be opened using "x" while opening a file 
with open("textonly.txt","x") as text:
    text.write("this is a new file just created")
with open("textonly.txt","r") as text:
    print(text.read())

# a file can be deleted by first importing os and them using os.remove("file_name.txt")

'''
to check whether a file exists of not
import os
if os.path.exists("file name"):
    os.remove("file name")
else:
    print("the file doesnot exist")
'''

# a folder can also be deleted using os.rmdir("folderName")