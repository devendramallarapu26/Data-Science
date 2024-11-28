import os 
os.getcwd() # its give the path of the file
os.chdir("d://Textfile") # to change the path file by using chdir. chdir means change directory
fp = open('d://Textfile/sample.txt',encoding='utf-8') # opening the file there are two parameters 1.path 2.operation like read and write operation but use encoding its fit for every server like windows lunxs
print(fp.tell()) # its print the position of the pointer
print(fp.read(5)) # its read the 5 chars
print(fp.tell())
fp.seek(0,1) # its set the position of the its 0 again start
print(fp.tell())
print(fp.read())
fp.seek(0,0)
print(fp.tell())
print(fp.read(10))
fp.close() # close the file
