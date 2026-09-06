f=open("demo.txt","r") #open("file_name","mode")
data=f.read()  #f.read() takes the contents of the file and stores it in data, like the scanf function
print(data,type(data)) 
f.close()