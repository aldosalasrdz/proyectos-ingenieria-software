"""Actividad 13. Weight tokens"""
import time
import sys
import os

folder = "NewFiles"
absolute_path = os.path.abspath(folder)

FilesTuple = []
Files = {}
args = list()

def sort_key(weight):
    return weight[1]

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

#Se reciben los argumentos
numArgs = len(sys.argv)
for arg in range(1, numArgs):
    args.append(sys.argv[arg].lower())

#Se sacan los archivos en los que estan las palabras
for word in args:
    for line in DicLines:
        rowWord = line.split(";")[0]
        if word == rowWord:
            rowRep = int(line.split(";")[1])
            rowPos = int(line.split(";")[2])
            
            for i in range (rowPos, (rowPos+rowRep)):
                fileId = int(PosLines[i].split()[0]) - 1
                fileWeight = float(PosLines[i].split()[1])
                file = DocLines[fileId].split()[1]
                
                #Se suma el peso si el archivo se repite
                if file in Files:
                    Files[file] = Files[file] + fileWeight
                else:
                    Files[file] = fileWeight
                
            break

for file in Files:
    FilesTuple.append((file, Files[file]))

#Se hace el top 10 de los archivos
FilesTuple.sort(key=lambda a: a[1], reverse=True)
FilesTuple = FilesTuple[:10]
for a in FilesTuple:
    print(a[0])