"""
Assignment 1: Word Counter
Create a Python script that reads a text file and counts the frequency of each word in the file.
Store the word frequencies in a dictionary.
Print out the top 5 most common words and their frequencies.

"""

a=open("C:/Users/ADMIN/OneDrive/Documents/FinalAssignment/Assignment1/a.txt")
c=0
b=dict()
for l in a:    
    word=l.split(" ")
    for words in word:
        if words in b:
            b[words]=b[words]+1
        else:
            b[words]=1
      
l=list(b.keys())
fi=l[:4]
for i in fi:
    print(i,":",b[i])
