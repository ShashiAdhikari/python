import difflib
import docx2txt
import os
from collections import Counter

text = docx2txt.process("D:\Python\wordsim\word1.docx")
#print(text)


arr = text.split(" ")
#
#store = len(arr)
store1 = []
for x in arr:
    if x not in store1:
        print(x, '=', arr.count(x))
        store1.append(x)















