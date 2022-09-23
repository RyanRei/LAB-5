#1
a=open('readfile.txt','r')
text=a.read()
print(text)
a.close()
#2
fa=open('test.txt',"r")
fb=open('writefile.txt','w')
readContent=fa.read();
fb.write(readContent);
fa.close()
fb.close()
#3
openfile=open('temps.txt',"r")
outfile=open('tempsout.txt','w')

for line in openfile:
    outfile.write(str(int(line)*9/5+32))
    outfile.write('\n')
openfile.close()
outfile.close()
