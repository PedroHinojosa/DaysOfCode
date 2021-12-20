#Text File Reader

print ("Opening and closing the file")
text_file = open("read_it.txt", "r")
text_file.close()

print("\nReading characters from the file.")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nLooping Through the File\n")
text_file =open("read_it.txt","r")
for line in text_file:
    print(line)

#Text File Writer

text_file = open("write_it.txt","w")

lines = ["New Line 1\n", "New Line 2\n"]

text_file.writelines(lines)
text_file.close()
text_file =  open("write_it.txt", "r")
print(text_file.read())
text_file.close()