fw = open("sample.txt","w")
fw.write("Hello World!\n")
fw.write("Writing a file from python is fun and easy\n")
fw.close()

fr = open("sample.txt","r")
text = fr.read()
print(text)
fr.close()
