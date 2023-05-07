"""Actividad 12. Weight tokens"""
import time
import os

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

#Lista de palabras
wordList = ["Gauch", "elephants", "CSCE", "Arkansas", "gift", "abcdef", "20", "20.07", "123-456-7890", "lawyer consumers", "garden computer", "garden computer", "United Ststes laws"]

#Se lee el diccionario
with open("dictionary.txt", "r") as Dic:
    DicLines = Dic.readlines()
    Dic.close()

#Se lee el posting
with open("newPosting.txt", "r") as Pos:
    PosLines = Pos.readlines()
    Pos.close()

#Se lee el documents
with open("Documents.txt", "r") as Doc:
    DocLines = Doc.readlines()
    Doc.close()

#word = "cdt"
print("Ingresar palabra de Token: ")
word = input()
word = word.lower()

for line in DicLines:
    rowWord = line.split(";")[0]
    if word == rowWord:
        rowRep = int(line.split(";")[1])
        rowPos = int(line.split(";")[2])
        
        for i in range (rowPos, (rowPos+rowRep)):
            fileId = int(PosLines[i].split()[0]) - 1
            file = DocLines[fileId].split()[1]
            
            print(file)
        break
    