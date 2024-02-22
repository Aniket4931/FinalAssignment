"""
Assignment 1: Word Counter
Create a Python script that reads a text file and counts the frequency of each word in the file.
Store the word frequencies in a dictionary.
Print out the top 5 most common words and their frequencies.

"""

a=open("C:/Users/ADMIN/OneDrive/Documents/FinalAssignment/Assignment1/a.txt")
Dictionary=dict()
for l in a:    
    wordSplit=l.split()
    for words in wordSplit:
        if words in Dictionary:
            Dictionary[words]=Dictionary[words]+1
        else:
            Dictionary[words]=1
      
Sorted_words=sorted(Dictionary.items(),key=lambda x:x[1],reverse=True)
for word,frequency in Sorted_words[:5]:
    print(word,":",frequency)
