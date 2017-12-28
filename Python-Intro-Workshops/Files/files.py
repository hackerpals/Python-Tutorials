'''
FILES

r   -- Opens in read only
rb  -- open in read only in binary format
r++ -- Opens a file for both reading anad writing
rb+ -- Opens a file for both reading and writing only in binary formart
w   -- Opens a file for writing only
wb  -- Opens a file for writing only in binary format
w+  -- Opens a file for both writing and reading
wb+ -- Open a file for both reading and writing only in binary format
a   -- opens a file for appending
ab  -- Opens a file for appending in binary format
a+  -- Opens a file for both appending and reading
ab+ -- Opens a file for both appending and reading in binary format

'''
# #Open a file
# fo = open("foo.text", "wb")
# print("Name of the file: ", fo.name)
# print("Closed or Not: ", fo.closed)
# print("Opening Mode: ", fo.mode )
# print("Softspace flag: ",fo.softspace)
#
#
'''
close() -- Close method closes files so nothing can be written after
fileObject.close()
'''

# fo = open("foo.txt","wb")
# print()
#
'''
write() -- method writes any string to an open file
fileObject.write("string")
'''
# fo = open("foo.txt", "wb")
# fo.write("Python is a great language.\nYeah its great!!\n")
#
# fo.close()

'''
read() -- Method reads a string from an open file
fileObject.read([count])
'''

# fo = open("foo.txt","r+")
# str = fo.read()
# print("Read string is: ", str)
#
# #fo.close()
#
'''
tell() method tells you the current position within the file
'''
# # Check current position
# position = fo.tell()
# print("Current file position : ", position)
#
# # Reposition pointer at the beginning once again
# position = fo.seek(0, 0)
# str = fo.read(10);
# print( "Again read String is : ", str)
# # Close opend file
# fo.close()
#
#
'''
rename()
os.rename(current_file_name, new_file_name)
'''

import os

#Rename a file foo.txt to foo2.text
#os.rename("foo.txt","foo2.txt")

#Now delete the  file
#os.remove("foo.text")


'''
mkdir()
os.mkdir("newdir")
'''

os.mkdir("test")


'''
chdir()
os.chdir("newdir")
'''
os.chdir("/home/newdir")

'''
getcwd()
os.getcwd()
'''

os.getcwd()


'''
rmdir()
os.rmdir()
'''

os.rmdir("/temp/test")
